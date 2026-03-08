import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from tests.utils.generators import generate_unique_email, generate_password

class TestLogin:

    @pytest.fixture(autouse=True)
    def setup_user(self, driver):
        """Предварительная регистрация пользователя перед тестами входа."""
        email = generate_unique_email()
        password = generate_password()

        driver.get(MAIN_PAGE_URL)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(REGISTER_LINK)
        ).click()

        driver.find_element(*NAME_INPUT).send_keys("Test User")
        driver.find_element(*EMAIL_INPUT).send_keys(email)
        driver.find_element(*PASSWORD_INPUT).send_keys(password)
        driver.find_element(*REGISTER_BUTTON).click()

        self.user_credentials = {"email": email, "password": password}

    def test_login_via_main_button(self, driver):
        """Вход по кнопке «Войти в аккаунт» на главной."""
        driver.get(MAIN_PAGE_URL)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LOGIN_BUTTON_MAIN)
        ).click()

        driver.find_element(*EMAIL_INPUT).send_keys(self.user_credentials["email"])
        driver.find_element(*PASSWORD_INPUT).send_keys(self.user_credentials["password"])
        driver.find_element(*LOGIN_FORM_BUTTON).click()

        logout_btn = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LOGOUT_BUTTON)
        )
        assert logout_btn.is_displayed()

    def test_login_via_personal_cabinet(self, driver):
        """Вход через кнопку «Личный кабинет»."""
        driver.get(MAIN_PAGE_URL)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(PERSONAL_CABINET_LINK)
        ).click()

        driver.find_element(*EMAIL_INPUT).send_keys(self.user_credentials["email"])
        driver.find_element(*PASSWORD_INPUT).send_keys(self.user_credentials["password"])
        driver.find_element(*LOGIN_FORM_BUTTON).click()