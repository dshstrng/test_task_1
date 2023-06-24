from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from locators.locators import LoginPageLocators as L, KeyPressesLocators as K, DropdownListLocators as DL, \
    DownloadLocators as D
from test_data.data import data, expected_options, expected_text
import requests


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()


class TestLoginPage:  # Этот класс содержит тест(ы) для страницы авторизации
    URL = 'http://the-internet.herokuapp.com/login'

    # тест проверяет успешную авторизацию с правильными учетными данными
    def test_TC_01_verify_authorization_with_valid_data(self, driver):
        driver.get(self.URL)
        username = driver.find_element(*L.INPUT_USERNAME)
        username.click()
        username.send_keys("tomsmith")
        password = driver.find_element(*L.INPUT_PASSWORD)
        password.send_keys("SuperSecretPassword!")
        driver.find_element(*L.BUTTON_LOGIN).click()
        expected_message = "You logged into a secure area!\n×"
        current_text = driver.find_element(*L.TEXT_MESSAGE).text
        assert expected_message == current_text, "Failed to verify successful authorization with valid data"


class TestKeyPresses:  # класс содержит тесты для проверки нажатия клавиш
    URL = "http://the-internet.herokuapp.com/key_presses?"

    #проверка видимости ответа при нажатии клавиши.
    @pytest.mark.parametrize("data", data)
    def test_TC_02_verify_visibility_of_the_answer(self, driver, data):
        driver.get(self.URL)
        input_frame = driver.find_element(*K.INPUT_FRAME)
        input_frame.click()
        input_frame.send_keys(data)
        expected_answer = "You entered: " + data.upper()
        result = driver.find_element(*K.TEXT_RESULT).text
        assert expected_answer == result, "The answer is not visible"


class TestDropdownList:  # класс содержит тесты для проверки выпадающего списка
    URL = "http://the-internet.herokuapp.com/dropdown"

    # доступные варианты в выпадающем списке содержат правильные значения
    def test_TC_03_verify_dropdown_options_contain_valid_value(self, driver):
        driver.get(self.URL)
        dropdown_element = driver.find_element(*DL.LIST_DROPDOWN)
        options = dropdown_element.find_elements(*DL.OPTIONS)
        actual_options = [option.text for option in options]
        assert actual_options == expected_options, "Dropdown options do not contain valid value"


class TestDownLoad:  # класс содержит тесты для проверки страницы загрузки
    URL = "http://the-internet.herokuapp.com/download"

    # проверка того, что файл успешно загружен и ожидаемый текст есть в файле
    def test_TC_04_verify_text_in_downloaded_txt_file(self, driver):
        driver.get(self.URL)
        download_link = driver.find_element(*D.LINK_DOWNLOAD).get_attribute('href')
        response = requests.get(download_link)
        assert response.status_code == 200 and len(response.content) > 0, "File download failed."
        file_content = response.text
        assert expected_text in file_content[2:6], "Expected text not found in downloaded file."
