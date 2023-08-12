import unittest
from unittest.mock import MagicMock, patch
from my_ui_booking.booking import Booking
from my_ui_booking import constants, utils
from .CustomTestRunner import CustomTestRunner


class TestBooking(unittest.TestCase):
    def test_open_landing_page(self):
        # Set up mock driver
        mock_driver = MagicMock()

        # Create Booking instance
        booking = Booking(mock_driver)

        # Call the open_landing_page method
        booking.open_landing_page()

        # Assertions
        mock_driver.get.assert_called_once_with(constants.BASE_URL)

    @patch('my_ui_booking.booking.utils')
    @patch('my_ui_booking.booking.EC')
    @patch('my_ui_booking.booking.By')
    def test_handle_popup(self, mock_By, mock_EC, mock_utils):
        # Set up mock driver
        mock_driver = MagicMock()

        # Set up mock WebDriverWait and expected conditions
        mock_wait = MagicMock()
        mock_utils.get_wait.return_value = mock_wait

        # Create Booking instance
        booking = Booking(mock_driver)

        # Set up mock expected condition
        mock_visibility = mock_EC.visibility_of_element_located
        mock_wait.until.return_value = MagicMock()

        # Call the handle_popup method
        booking.handle_popup()

        # Assertions
        mock_utils.get_wait.assert_called_once_with(mock_driver)
        mock_visibility.assert_called_once_with((mock_By.CSS_SELECTOR, constants.CLOSE_POPUP))
        mock_wait.until.assert_called_once()

if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
