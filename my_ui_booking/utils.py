from selenium.webdriver.support.ui import WebDriverWait
from my_ui_booking import constants


def get_wait(driver):
    return WebDriverWait(driver, constants.WAIT_TIMEOUT)
