import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config import MAIN_PAGE_URL
from locators import *

class TestLogin:

    def test_login_via_main_button(self, driver, wait, registered_user):
        """Вход по кнопке «Войти в аккаунт» на главной."""
        driver.get(MAIN_PAGE_URL)
        wait.until(EC.element_to_be_clickable(LOGIN_BUTTON_MAIN)).click()

        # Ввод данных
        email_field = driver.find_element(*EMAIL_INPUT)
        password_field = driver.find_element(*PASSWORD_INPUT)
        login_button = driver.find_element(*LOGIN_FORM_BUTTON)

        email_field.send_keys(registered_user["email"])
        password_field.send_keys(registered_user["password"])
        login_button.click()

        # Верификация успешного входа
        logout_btn = wait.until(EC.presence_of_element_located(LOGOUT_BUTTON))
        assert logout_btn.is_displayed(), "Кнопка выхода найдена, но не отображается после входа"
        assert "Выйти" in logout_btn.text, "Текст кнопки выхода не соответствует ожидаемому"

    def test_login_via_personal_cabinet(self, driver, wait, registered_user):
        """Вход через кнопку «Личный кабинет»."""
        driver.get(MAIN_PAGE_URL)
        wait.until(EC.element_to_be_clickable(PERSONAL_CABINET_LINK)).click()

        # Ввод данных
        email_field = driver.find_element(*EMAIL_INPUT)
        password_field = driver.find_element(*PASSWORD_INPUT)
        login_button = driver.find_element(*LOGIN_FORM_BUTTON)

        email_field.send_keys(registered_user["email"])
        password_field.send_keys(registered_user["password"])
        login_button.click()

        # Верификация успешного входа
        logout_btn = wait.until(EC.presence_of_element_located(LOGOUT_BUTTON))
        assert logout_btn.is_displayed(), "Кнопка выхода найдена, но не отображается после входа через личный кабинет"
        assert "Выйти" in logout_btn.text, "Текст кнопки выхода не соответствует ожидаемому"

    def test_login_with_invalid_credentials(self, driver, wait):
        """Проверка входа с некорректными учётными данными."""
        driver.get(MAIN_PAGE_URL)
        wait.until(EC.element_to_be_clickable(LOGIN_BUTTON_MAIN)).click()

        # Ввод некорректных данных
        email_field = driver.find_element(*EMAIL_INPUT)
        password_field = driver.find_element(*PASSWORD_INPUT)
        login_button = driver.find_element(*LOGIN_FORM_BUTTON)

        email_field.send_keys("invalid@example.com")
        password_field.send_keys("wrongpassword")
        login_button.click()

        # Верификация: кнопка выхода не должна появиться
        try:
            wait.until(EC.visibility_of_element_located(LOGOUT_BUTTON))
            assert False, "Кнопка выхода появилась при вводе некорректных данных"
        except TimeoutException:
            pass  # Ожидаемое поведение: элемент не найден

        # Дополнительно проверяем появление сообщения об ошибке
        try:
            error_msg = wait.until(EC.visibility_of_element_located(ERROR_MESSAGE))
            assert error_msg.is_displayed(), "Сообщение об ошибке не отображается при некорректных данных"
            assert any(msg in error_msg.text.lower() for msg in ["некорректно", "неверный", "ошибка"]), \
                "Текст сообщения об ошибке не соответствует ожидаемому"
        except TimeoutException:
            assert False, "Сообщение об ошибке не появилось при некорректных данных"

    def test_login_with_empty_fields(self, driver, wait):
        """Проверка входа с пустыми полями."""
        driver.get(MAIN_PAGE_URL)
        wait.until(EC.element_to_be_clickable(LOGIN_BUTTON_MAIN)).click()

        # Оставляем поля пустыми
        email_field = driver.find_element(*EMAIL_INPUT)
        password_field = driver.find_element(*PASSWORD_INPUT)
        login_button = driver.find_element(*LOGIN_FORM_BUTTON)

        email_field.clear()
        password_field.clear()
        login_button.click()

        # Верификация появления сообщения об ошибке
        error_msg = wait.until(EC.visibility_of_element_located(ERROR_MESSAGE))
        assert error_msg.is_displayed(), "Сообщение об ошибке не отображается при пустых полях"
        assert any(msg in error_msg.text.lower() for msg in ["обязательное", "заполните", "пусто"]), \
            "Текст сообщения об ошибке не соответствует ожидаемому для пустых полей"

    def test_redirect_after_login(self, driver, wait, registered_user):
        """Проверка редиректа на главную страницу после входа."""
        driver.get(MAIN_PAGE_URL)
        wait.until(EC.element_to_be_clickable(LOGIN_BUTTON_MAIN)).click()

        # Ввод данных
        email_field = driver.find_element(*EMAIL_INPUT)
        password_field = driver.find_element(*PASSWORD_INPUT)
        login_button = driver.find_element(*LOGIN_FORM_BUTTON)

        email_field.send_keys(registered_user["email"])
        password_field.send_keys(registered_user["password"])
        login_button.click()

        # Ждём появления кнопки выхода как признака успешной авторизации
        logout_btn = wait.until(EC.visibility_of_element_located(LOGOUT_BUTTON))

        # Верификации
        assert logout_btn.is_displayed(), "Кнопка выхода не отображается после успешного входа"

        # Проверяем URL после входа
        current_url = driver.current_url
        assert MAIN_PAGE_URL in current_url, f"Ожидался редирект на {MAIN_PAGE_URL}, но открыт {current_url}"

        # Дополнительная верификация: проверяем видимость логотипа (признак главной страницы)
        logo = wait.until(EC.visibility_of_element_located(LOGO_STELLAR_BURGERS))
        assert logo.is_displayed(), "Логотип не отображается на главной странице после входа"
