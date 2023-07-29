from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Booking:
    def __init__(self, driver):
        self.driver = driver

    def open_landing_page(self):
        self.driver.get("https://www.booking.com/")

    def handle_popup(self):
        popup_locator = (By.ID, "popup-close")
        wait = WebDriverWait(self.driver, 10)

        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".fc63351294.a822bdf511.e3c025e003."
                                                               "fa565176a8.f7db01295e.c334e6f658.ae1678b153")))
        element.click()


