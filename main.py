import time
from selenium import webdriver
import chromedriver_autoinstaller
from page import *

def create_driver():
    chromedriver_autoinstaller.install()
    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=C:/Selenium_cookie') 
    options.add_argument('--profile-directory=CustomProfile')
    options.add_argument('--disable-dev-shm-usage')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    return webdriver.Chrome(options=options)


driver = create_driver()
driver.get('https://orteil.dashnet.org/cookieclicker/')
c = MainPage(driver)

while True:
    c.click_golden_cookie()
    c.upgrade()
    c_count = c.get_cookies()
    c.buy_product(c_count)
    c.kill_achievements()
    c.click_big_cookie()
    time.sleep(0.01)
