from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from . import utils
import slash
import time


class ChangeCurrency:
    def __init__(self, driver):
        self.driver = driver

    def launch(self):
        if not self.loaded():
            wait = utils.get_wait(self.driver)
            button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="header-currency-picker-trigger"]')))
            button.click()
            slash.logger.info("Currency Page launched")
        else:
            slash.logger.info("Currency Page already loaded")
        time.sleep(2)

    def loaded(self):
        try:
            wait = utils.get_wait(self.driver)
            currency_heading = wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'h2.fcab3ed991.f0d4d6a2f5.fda3b74d0d'))
            )
            return currency_heading.text.strip() == "Select your currency"
        except:
            return False

    def select_currency(self, currency_code):
        if self.loaded():
            try:
                wait = WebDriverWait(self.driver, 10)
                currency_list = wait.until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'ul.a1b3f50dcd li button')))

                for currency in currency_list:
                    if currency_code in currency.text:
                        currency.click()
                        print(f"Currency '{currency_code}' selected.")
                        break
            except:
                print(f"Failed to select currency '{currency_code}'.")
        else:
            print("Currency Page is not loaded yet. Call 'launch()' method first.")

