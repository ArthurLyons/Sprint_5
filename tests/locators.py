# Главная страница
MAIN_PAGE_URL = "https://stellarburgers.education-services.ru/"

# Кнопки входа и регистрации
LOGIN_BUTTON_MAIN = ("xpath", "//button[contains(text(), 'Войти в аккаунт')]")
PERSONAL_CABINET_LINK = ("xpath", "//a[contains(text(), 'Личный кабинет')]")
REGISTER_LINK = ("xpath", "//a[contains(text(), 'Зарегистрироваться')]")
FORGOT_PASSWORD_LINK = ("xpath", "//a[contains(text(), 'Забыли пароль?')]")

# Форма регистрации
NAME_INPUT = ("name", "name")
EMAIL_INPUT = ("name", "email")
PASSWORD_INPUT = ("name", "password")
REGISTER_BUTTON = ("xpath", "//button[contains(text(), 'Зарегистрироваться')]")

# Форма входа
LOGIN_FORM_BUTTON = ("xpath", "//button[contains(text(), 'Войти')]")

# Личный кабинет и выход
LOGOUT_BUTTON = ("xpath", "//button[contains(text(), 'Выйти')]")

# Конструктор и навигация
CONSTRUCTOR_BUTTON = ("xpath", "//a[contains(text(), 'Конструктор')]")
LOGO_STELLAR_BURGERS = ("class_name", "AppHeader_header__logo__2D_98")

# Разделы конструктора
BUNS_SECTION = ("xpath", "//div[contains(text(), 'Булки')]")
SAUCES_SECTION = ("xpath", "//div[contains(text(), 'Соусы')]")
FILLINGS_SECTION = ("xpath", "//div[contains(text(), 'Начинки')]")

# Сообщения об ошибках
ERROR_MESSAGE = ("class_name", "input__error")
