import random
import string
from config import MIN_PASSWORD_LENGTH

def generate_unique_email(name="test", surname="testov", cohort=1999):
    """Генерирует уникальный email по шаблону."""
    random_digits = ''.join(random.choices(string.digits, k=3))
    return f"{name}_{surname}_{cohort}_{random_digits}@yandex.ru"

def generate_password(length=None):
    """
    Генерирует случайный пароль заданной длины.
    Если длина не указана, использует MIN_PASSWORD_LENGTH из config.
    """
    if length is None:
        length = MIN_PASSWORD_LENGTH
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def get_test_user_credentials():
    """Возвращает словарь с учётными данными тестового пользователя."""
    return {
        "email": generate_unique_email(),
        "password": generate_password()
    }

def get_weak_password():
    """Возвращает пароль короче минимальной длины (для тестов ошибок)."""
    return generate_password(MIN_PASSWORD_LENGTH - 1)

def get_existing_user_credentials(registered_user):
    """
    Возвращает учётные данные уже зарегистрированного пользователя.
    Используется для тестов, проверяющих дублирование.
    """
    return registered_user
