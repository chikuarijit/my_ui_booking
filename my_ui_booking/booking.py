import slash
from . import constants as const
from . import utils
from selenium.webdriver.common.by import By
from selenium.webdriver.support import \
    expected_conditions as EC


class Booking:
    def __init__(self, driver):
        self.driver = driver

    def open_landing_page(self):
        slash.logger.info(f"Opening {const.BASE_URL}")
        self.driver.get(const.BASE_URL)
        slash.logger.info(f"{const.BASE_URL} successfully opened")

    def handle_popup(self):
        slash.logger.info("Closing Popup")
        element = utils.get_wait(self.driver).until(
            EC.visibility_of_element_located
            ((By.CSS_SELECTOR, const.CLOSE_POPUP)))
        element.click()
        slash.logger.info("Popup Closed")
