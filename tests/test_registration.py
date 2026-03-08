import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

class TestRegistration:

    def test_successful_registration(self, driver, user_credentials):
        """Проверка успешной регистрации с уникальными данными."""
        driver.get(MAIN_PAGE_URL)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(REGISTER_LINK)
        ).click()

        # Заполняем форму с сгенерированными данными
        driver.find_element(*NAME_INPUT).send_keys("Test User")
        driver.find_element(*EMAIL_INPUT).send_keys(user_credentials["email"])
        driver.find_element(*PASSWORD_INPUT).send_keys(user_credentials["password"])
        driver.find_element(*REGISTER_BUTTON).click()

        # Проверяем успешную регистрацию
        logout_btn = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LOGOUT_BUTTON)
        )
        assert logout_btn.is_displayed()

    def test_invalid_password_error(self, driver):
        """Проверка ошибки для некорректного пароля."""
        driver.get(MAIN_PAGE_URL)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(REGISTER_LINK)
        ).click()

        # Пароль меньше 6 символов
        driver.find_element(*NAME_INPUT).send_keys("Test User")
        driver.find_element(*EMAIL_INPUT).send_keys(generate_unique_email())
        driver.find_element(*PASSWORD_INPUT).send_keys("123")
        driver.find_element(*REGISTER_BUTTON).click()

        # Проверяем сообщение об ошибке
        error_msg = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ERROR_MESSAGE)
        )
        assert "Некорректный пароль" in error_msg.text
