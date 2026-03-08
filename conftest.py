import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from tests.utils.generators import generate_unique_email, generate_password

@pytest.fixture(scope="function")
def driver():
    """Фикстура для инициализации браузера."""
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def user_credentials():
    """Фикстура для генерации учётных данных пользователя."""
    email = generate_unique_email()
    password = generate_password()
    return {"email": email, "password": password}
