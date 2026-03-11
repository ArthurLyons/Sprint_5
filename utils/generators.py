import random
import string

def generate_unique_email(name="test", surname="testov", cohort=1999):
    """Генерирует уникальный email по шаблону."""
    random_digits = ''.join(random.choices(string.digits, k=3))
    return f"{name}_{surname}_{cohort}_{random_digits}@yandex.ru"

def generate_password(length=6):
    """Генерирует случайный пароль заданной длины."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))
