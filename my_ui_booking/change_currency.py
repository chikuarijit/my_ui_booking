import slash
import time
from . import utils
from . import constants as const
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ChangeCurrency:
    def __init__(self, driver):
        self.driver = driver

    def launch(self):
        if not self.loaded():
            slash.logger.info("Launching Currency Page")
            button = utils.get_wait(self.driver).until(
                EC.element_to_be_clickable
                ((By.CSS_SELECTOR, const.CURRENCY_BUTTON)))
            slash.logger.info("Clicking on Currency Button")
            button.click()
            slash.logger.info("Currency Page launched")
        else:
            slash.logger.info("Currency Page already loaded")
        time.sleep(2)

    def loaded(self):
        try:
            currency_heading = utils.get_wait(self.driver).until(
                EC.visibility_of_element_located
                ((By.CSS_SELECTOR, const.CURRENCY_PAGE)))
            slash.logger.info("Currency Page loaded")
            return currency_heading.text.\
                strip() == const.CURRENCY_TEXT
        except:
            return False

    def select_currency(self, currency_code):
        if self.loaded():
            try:
                slash.logger.info("Selecting Currency")
                currency_list = utils.get_wait(self.driver).until(
                    EC.presence_of_all_elements_located
                    ((By.CSS_SELECTOR, const.SELECT_CURRENCY)))

                for currency in currency_list:
                    if currency_code in currency.text:
                        slash.logger.info(
                            f"Selecting {currency_code}")
                        currency.click()
                        slash.logger.info(
                            f"Currency "
                            f"'{currency_code}' selected.")
                        break
            except:
                slash.logger.info(
                    f"Failed to "
                    f"select currency "
                    f"'{currency_code}'.")
        else:
            slash.logger.info(
                "Currency Page is not "
                "loaded yet. Call 'launch()' "
                "method first.")
