from selenium.webdriver.common.by import By

# Кнопки входа и регистрации
LOGIN_BUTTON_MAIN = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
PERSONAL_CABINET_LINK = (By.XPATH, "//a[contains(text(), 'Личный кабинет')]")
REGISTER_LINK = (By.XPATH, "//a[contains(text(), 'Зарегистрироваться')]")
FORGOT_PASSWORD_LINK = (By.XPATH, "//a[contains(text(), 'Забыли пароль?')]")

# Форма регистрации
NAME_INPUT = (By.NAME, "name")
EMAIL_INPUT = (By.NAME, "email")
PASSWORD_INPUT = (By.NAME, "password")
REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")

# Форма входа
LOGIN_FORM_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")

# Личный кабинет и выход
LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выйти')]")

# Конструктор и навигация
CONSTRUCTOR_BUTTON = (By.XPATH, "//a[contains(text(), 'Конструктор')]")
LOGO_STELLAR_BURGERS = (By.CLASS_NAME, "AppHeader_header__logo__2D_98")

# Разделы конструктора
BUNS_SECTION = (By.XPATH, "//div[contains(text(), 'Булки')]")
SAUCES_SECTION = (By.XPATH, "//div[contains(text(), 'Соусы')]")
FILLINGS_SECTION = (By.XPATH, "//div[contains(text(), 'Начинки')]")

# Сообщения об ошибках
ERROR_MESSAGE = (By.CLASS_NAME, "input__error")

# Сообщения об ошибках с конкретными текстами
ERROR_MESSAGE_INVALID_PASSWORD = (By.XPATH, "//div[contains(text(), 'Некорректный пароль')]")
ERROR_MESSAGE_EMPTY_FIELDS = (By.XPATH, "//div[contains(text(), 'Поля обязательны для заполнения')]")
ERROR_MESSAGE_EXISTING_USER = (By.XPATH, "//div[contains(text(), 'Пользователь с таким email уже существует')]")

# Универсальный локатор для любых сообщений об ошибках
ERROR_MESSAGE = (By.CLASS_NAME, "input__error")