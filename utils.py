from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from my_ui_booking import constants


def get_wait(driver):
    return WebDriverWait(driver, constants.WAIT_TIMEOUT)