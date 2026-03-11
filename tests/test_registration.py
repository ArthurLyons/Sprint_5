import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config import MAIN_PAGE_URL, DEFAULT_NAME, MIN_PASSWORD_LENGTH
from locators import *

class TestRegistration:

    def test_successful_registration(self, driver, wait, user_credentials):
        """Проверка успешной регистрации с уникальными данными."""
        driver.get(MAIN_PAGE_URL)
        wait.until(EC.element_to_be_clickable(REGISTER_LINK)).click()

        # Заполняем форму с сгенерированными данными
        driver.find_element(*NAME_INPUT).send_keys(DEFAULT_NAME)
        driver.find_element(*EMAIL_INPUT).send_keys(user_credentials["email"])
        driver.find_element(*PASSWORD_INPUT).send_keys(user_credentials["password"])
        driver.find_element(*REGISTER_BUTTON).click()

        # Ищем элемент с таймаутом, но проверку видимости оставляем для assert
        logout_btn = wait.until(EC.presence_of_element_located(LOGOUT_BUTTON))
        assert logout_btn.is_displayed(), "Кнопка выхода найдена, но не отображается после успешной регистрации"

    def test_invalid_password_error(self, driver, wait):
        """Проверка ошибки для некорректного пароля."""
        driver.get(MAIN_PAGE_URL)
        wait.until(EC.element_to_be_clickable(REGISTER_LINK)).click()

        # Пароль меньше минимальной длины
        driver.find_element(*NAME_INPUT).send_keys(DEFAULT_NAME)
        driver.find_element(*EMAIL_INPUT).send_keys("test@example.com")
        driver.find_element(*PASSWORD_INPUT).send_keys("123")  # меньше MIN_PASSWORD_LENGTH
        driver.find_element(*REGISTER_BUTTON).click()

        # Ищем конкретное сообщение об ошибке с текстом «Некорректный пароль»
        error_msg = wait.until(
            EC.presence_of_element_located(ERROR_MESSAGE_INVALID_PASSWORD)
        )
        assert error_msg.is_displayed(), "Сообщение «Некорректный пароль» не отображается при слабом пароле"

    def test_empty_fields_error(self, driver, wait):
        """Проверка ошибки при пустых полях."""
        driver.get(MAIN_PAGE_URL)
        wait.until(EC.element_to_be_clickable(REGISTER_LINK)).click()

        # Оставляем поля пустыми
        driver.find_element(*NAME_INPUT).clear()
        driver.find_element(*EMAIL_INPUT).clear()
        driver.find_element(*PASSWORD_INPUT).clear()
        driver.find_element(*REGISTER_BUTTON).click()

        # Ищем конкретное сообщение об ошибке для пустых полей
        error_msg = wait.until(
            EC.presence_of_element_located(ERROR_MESSAGE_EMPTY_FIELDS)
        )
        assert error_msg.is_displayed(), "Сообщение о пустых полях не отображается"

    def test_existing_user_error(self, driver, wait, registered_user):
        """Проверка ошибки при регистрации с существующим email."""
        driver.get(MAIN_PAGE_URL)
        wait.until(EC.element_to_be_clickable(REGISTER_LINK)).click()

        # Пытаемся зарегистрироваться с уже существующим email
        driver.find_element(*NAME_INPUT).send_keys("Another User")
        driver.find_element(*EMAIL_INPUT).send_keys(registered_user["email"])
        driver.find_element(*PASSWORD_INPUT).send_keys(registered_user["password"])
        driver.find_element(*REGISTER_BUTTON).click()

        # Ищем сообщение об ошибке для существующего пользователя
        error_msg = wait.until(
            EC.presence_of_element_located(ERROR_MESSAGE_EXISTING_USER)
        )
        assert error_msg.is_displayed(), "Сообщение о существующем пользователе не отображается"
