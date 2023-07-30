import slash
import time
from . import utils
from . import constants as const
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ChangeLanguage:
    def __init__(self, driver):
        self.driver = driver

    def launch(self):
        if not self.loaded():
            slash.logger.info("Launching Language Page")
            button = utils.get_wait(self.driver).until(
                EC.element_to_be_clickable
                ((By.CSS_SELECTOR, const.LANGUAGE_BUTTON)))
            slash.logger.info("Clicking on Language Button")
            button.click()
            slash.logger.info("Language Page launched")
        else:
            slash.logger.info("Language Page already loaded")
        time.sleep(2)

    def loaded(self):
        try:
            language_heading = utils.get_wait(self.driver).until(
                EC.visibility_of_element_located
                ((By.CSS_SELECTOR, const.LANGUAGE_PAGE)))
            slash.logger.info("Language Page loaded")
            return language_heading.text.\
                strip() == const.LANGUAGE_TEXT
        except:
            return False

    def select_language(self, language_code):
        if self.loaded():
            try:
                slash.logger.info("Selecting Language")
                language_list = utils.get_wait(self.driver).until(
                    EC.presence_of_all_elements_located
                    ((By.CSS_SELECTOR, const.SELECT_LANGUAGE)))

                for language in language_list:
                    if language_code in language.text:
                        slash.logger.info(
                            f"Selecting {language_code}")
                        language.click()
                        slash.logger.info(
                            f"Language "
                            f"'{language_code}' selected.")
                        break
            except:
                slash.logger.info(
                    f"Failed to "
                    f"select currency "
                    f"'{language_code}'.")
        else:
            slash.logger.info(
                "Language Page is not "
                "loaded yet. Call 'launch()' "
                "method first.")
