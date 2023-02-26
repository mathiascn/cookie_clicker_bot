from selenium.webdriver.common.by import By

class MainPageLocators(object):
    COOKIES = (By.ID, 'cookies')
    BIG_COOKIE = (By.ID, 'bigCookie')
    UPGRADE_PARENT = (By.ID, 'upgrades')
    UPGRADES_AVAILABLE = (By.CLASS_NAME, 'enabled')
    GOLDEN_COOKIE = (By.CLASS_NAME, 'shimmer')
    KILL_ACHIEVEMENTS = (By.CLASS_NAME, 'close')
