import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config import DEFAULT_TIMEOUT, MAIN_PAGE_URL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators
from helpers import get_test_user_credentials, get_existing_user_credentials

@pytest.fixture(scope="function")
def driver():
    """Фикстура для инициализации браузера."""
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    """Фикстура для WebDriverWait с таймаутом по умолчанию."""
    return WebDriverWait(driver, DEFAULT_TIMEOUT)

@pytest.fixture
def registered_user(driver, wait):
    """
    Фикстура для предварительной регистрации пользователя.

    Выполняет полный цикл регистрации нового пользователя и возвращает
    его учётные данные для использования в тестах авторизации.
    """
    # Получаем учётные данные через helper
    user_credentials = get_test_user_credentials()

    # Выполняем регистрацию
    driver.get(MAIN_PAGE_URL)
    wait.until(EC.element_to_be_clickable(locators.REGISTER_LINK)).click()

    driver.find_element(*locators.NAME_INPUT).send_keys("Test User")
    driver.find_element(*locators.EMAIL_INPUT).send_keys(user_credentials["email"])
    driver.find_element(*locators.PASSWORD_INPUT).send_keys(user_credentials["password"])
    driver.find_element(*locators.REGISTER_BUTTON).click()


    # Ждём успешного завершения регистрации
    wait.until(EC.visibility_of_element_located(locators.LOGOUT_BUTTON))

    return user_credentials

@pytest.fixture
def logged_in_user(driver, wait, registered_user):
    """
    Фикстура для авторизации пользователя.

    Использует уже зарегистрированного пользователя и выполняет вход в систему.
    Может использоваться в тестах, требующих авторизованного пользователя.
    """
    driver.get(MAIN_PAGE_URL)
    wait.until(EC.element_to_be_clickable(locators.LOGIN_BUTTON_MAIN)).click()

    driver.find_element(*locators.EMAIL_INPUT).send_keys(registered_user["email"])
    driver.find_element(*locators.PASSWORD_INPUT).send_keys(registered_user["password"])
    driver.find_element(*locators.LOGIN_FORM_BUTTON).click()

    # Ждём завершения авторизации
    wait.until(EC.visibility_of_element_located(locators.LOGOUT_BUTTON))
