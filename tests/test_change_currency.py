import unittest
from unittest.mock import MagicMock, patch
from my_ui_booking.change_currency import ChangeCurrency


class TestChangeCurrency(unittest.TestCase):

    @patch('my_ui_booking.change_currency.utils')
    def test_launch_currency_page(self, mock_utils):
        # Set up mock driver and elements
        mock_driver = MagicMock()
        mock_wait = MagicMock()
        mock_utils.get_wait.return_value = mock_wait
        mock_button = MagicMock()
        mock_wait.until.return_value = mock_button

        # Create ChangeCurrency instance
        change_currency = ChangeCurrency(mock_driver)

        # Call the launch method
        change_currency.launch()

        # Assertions
        mock_utils.get_wait.assert_called_once_with(mock_driver)
        mock_wait.until.assert_called_once_with(
            mock_utils.EC.element_to_be_clickable(
                (mock_utils.By.CSS_SELECTOR, mock_utils.const.CURRENCY_BUTTON)
            )
        )
        mock_button.click.assert_called_once()
        self.assertTrue(mock_utils.logger.info.called)

    @patch('my_ui_booking.change_currency.utils')
    def test_select_currency(self, mock_utils):
        # Set up mock driver and elements
        mock_driver = MagicMock()
        mock_wait = MagicMock()
        mock_utils.get_wait.return_value = mock_wait
        mock_currency = MagicMock()
        mock_currency_list = [mock_currency]
        mock_wait.until.return_value = mock_currency_list

        # Create ChangeCurrency instance
        change_currency = ChangeCurrency(mock_driver)

        # Call the select_currency method
        change_currency.select_currency("USD")

        # Assertions
        mock_utils.get_wait.assert_called_once_with(mock_driver)
        mock_wait.until.assert_called_once_with(
            mock_utils.EC.presence_of_all_elements_located(
                (mock_utils.By.CSS_SELECTOR, mock_utils.const.SELECT_CURRENCY)
            )
        )
        mock_currency.click.assert_called_once()
        self.assertTrue(mock_utils.logger.info.called)

    @patch('my_ui_booking.change_currency.utils')
    def test_launch_currency_page_when_not_loaded(self, mock_utils):
        # Set up mock driver and elements
        mock_driver = MagicMock()
        mock_wait = MagicMock()
        mock_utils.get_wait.return_value = mock_wait
        mock_button = MagicMock()
        mock_wait.until.return_value = mock_button
        mock_currency_heading = MagicMock()
        mock_currency_heading.text.strip.return_value = "Select your currency"
        mock_wait.until.side_effect = [
            mock_utils.EC.visibility_of_element_located(
                (mock_utils.By.CSS_SELECTOR, mock_utils.const.CURRENCY_PAGE)
            ),
            mock_utils.EC.element_to_be_clickable(
                (mock_utils.By.CSS_SELECTOR, mock_utils.const.CURRENCY_BUTTON)
            )
        ]

        # Create ChangeCurrency instance
        change_currency = ChangeCurrency(mock_driver)

        # Call the launch method
        change_currency.launch()

        # Assertions
        mock_utils.get_wait.assert_called_once_with(mock_driver)
        mock_wait.until.assert_called_with(
            mock_utils.EC.visibility_of_element_located(
                (mock_utils.By.CSS_SELECTOR, mock_utils.const.CURRENCY_PAGE)
            )
        )
        mock_button.click.assert_called_once()
        self.assertTrue(mock_utils.logger.info.called)

    @patch('my_ui_booking.change_currency.utils')
    def test_launch_currency_page_when_already_loaded(self, mock_utils):
        # Set up mock driver and elements
        mock_driver = MagicMock()
        mock_wait = MagicMock()
        mock_utils.get_wait.return_value = mock_wait
        mock_currency_heading = MagicMock()
        mock_currency_heading.text.strip.return_value = "Select your currency"
        mock_wait.until.return_value = mock_currency_heading

        # Create ChangeCurrency instance
        change_currency = ChangeCurrency(mock_driver)

        # Call the launch method
        change_currency.launch()

        # Assertions
        mock_utils.get_wait.assert_called_once_with(mock_driver)
        mock_wait.until.assert_called_once_with(
            mock_utils.EC.visibility_of_element_located(
                (mock_utils.By.CSS_SELECTOR, mock_utils.const.CURRENCY_PAGE)
            )
        )
        self.assertFalse(mock_utils.logger.info.called)

    @patch('my_ui_booking.change_currency.utils')
    def test_select_currency_success(self, mock_utils):
        # Set up mock driver and elements
        mock_driver = MagicMock()
        mock_wait = MagicMock()
        mock_utils.get_wait.return_value = mock_wait
        mock_currency = MagicMock()
        mock_currency_list = [mock_currency]
        mock_wait.until.return_value = mock_currency_list
        mock_currency.text = "USD"
        mock_currency_heading = MagicMock()
        mock_currency_heading.text.strip.return_value = "Select your currency"
        mock_utils.get_wait.return_value.until.side_effect = [
            mock_currency_heading,
            mock_currency_list
        ]

        # Create ChangeCurrency instance
        change_currency = ChangeCurrency(mock_driver)

        # Call the select_currency method
        change_currency.select_currency("USD")

        # Assertions
        mock_utils.get_wait.assert_called_once_with(mock_driver)
        mock_wait.until.assert_called_with(
            mock_utils.EC.presence_of_all_elements_located(
                (mock_utils.By.CSS_SELECTOR, mock_utils.const.SELECT_CURRENCY)
            )
        )
        mock_currency.click.assert_called_once()
        self.assertTrue(mock_utils.logger.info.called)

    @patch('my_ui_booking.change_currency.utils')
    def test_select_currency_failure(self, mock_utils):
        # Set up mock driver and elements
        mock_driver = MagicMock()
        mock_wait = MagicMock()
        mock_utils.get_wait.return_value = mock_wait
        mock_currency = MagicMock()
        mock_currency_list = [mock_currency]
        mock_wait.until.return_value = mock_currency_list
        mock_currency.text = "EUR"
        mock_currency_heading = MagicMock()
        mock_currency_heading.text.strip.return_value = "Select your currency"
        mock_utils.get_wait.return_value.until.side_effect = [
            mock_currency_heading,
            mock_currency_list
        ]

        # Create ChangeCurrency instance
        change_currency = ChangeCurrency(mock_driver)

        # Call the select_currency method with a currency code that doesn't exist
        change_currency.select_currency("USD")

        # Assertions
        mock_utils.get_wait.assert_called_once_with(mock_driver)
        mock_wait.until.assert_called_with(
            mock_utils.EC.presence_of_all_elements_located(
                (mock_utils.By.CSS_SELECTOR, mock_utils.const.SELECT_CURRENCY)
            )
        )
        mock_currency.click.assert_not_called()
        self.assertTrue(mock_utils.logger.info.called)

if __name__ == '__main__':
    unittest.main()