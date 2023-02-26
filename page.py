from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
from locator import *

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    def get_cookies(self):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(MainPageLocators.COOKIES))
            cookies_text = element.text.split()[0]
            return float(cookies_text.replace(',', ''))
        except Exception as e:
            print(f'get_cookies exception: {e}')
    
    def click_big_cookie(self):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(MainPageLocators.BIG_COOKIE))
            element.click()
        except Exception as e:
            print(f'click_big_cookie exception: {e}')
    
    def click_golden_cookie(self):
        try:
            golden_cookie = self.driver.find_elements(*MainPageLocators.GOLDEN_COOKIE)
            if golden_cookie:
                golden_cookie[0].click()
        except Exception as e:
            print(f'click_golden_cookie exception: {e}')

    def upgrade(self):
        try:
            parent = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(MainPageLocators.UPGRADE_PARENT))
            upgrades_available = parent.find_elements(*MainPageLocators.UPGRADES_AVAILABLE)
            if upgrades_available:
                upgrades_available[0].click()
        except Exception as e:
            print(f'upgrade exception: {e}')

    def buy_product(self, cookies):
        try:
            game_objects = []
            for i in range(18):
                game_object = self.driver.execute_script(f'return {{price: Game.ObjectsById[{i}]["price"], storedCps: Game.ObjectsById[{i}]["storedCps"], locked: Game.ObjectsById[{i}]["locked"]}};')
                if not game_object['locked']:
                    price_per_cps = game_object['price'] / game_object['storedCps']
                    game_objects.append((i, price_per_cps, game_object['price']))

            sorted_objects = sorted(game_objects, key=lambda x: x[1], reverse=False)

            if len(sorted_objects) > 0:
                obj = sorted_objects[0]
                if obj[2] < cookies:
                    self.driver.find_element(By.ID, 'product' + str(obj[0])).click()

        except Exception as e:
            print(f'buy_product exception: {e}')
