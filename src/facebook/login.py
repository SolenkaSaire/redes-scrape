from src.common.driver_manager import get_web_driver
from src.common.human_behavior import HumanBehavior
from selenium.webdriver.common.by import By
from src.config.settings import Config
from src.common.cookie_manager import save_cookies, load_cookies
from src.common.logger import setup_logger

logger = setup_logger("facebook_login")

def facebook_login(driver):
    
    driver.get(Config.FACEBOOK_URL)
    cookie_file = Config.COOKIE_STORAGE_PATH + "facebook.pkl"

    if load_cookies(driver, cookie_file):
        driver.refresh()
        logger.info("Login automático con cookies.")
        HumanBehavior.random_wait(2, 5)
        return driver

    try:
        username_input = driver.find_element(By.ID, "email")
        password_input = driver.find_element(By.ID, "pass")
        login_button = driver.find_element(By.NAME, "login")

        HumanBehavior.type_like_human(username_input, Config.FACEBOOK_CREDENTIALS["username"])
        HumanBehavior.random_wait()
        HumanBehavior.type_like_human(password_input, Config.FACEBOOK_CREDENTIALS["password"])
        HumanBehavior.random_wait(1, 3)
        login_button.click()

        HumanBehavior.random_wait(2, 5)
        HumanBehavior.scroll_page(driver, scroll_times=3)
        HumanBehavior.move_mouse_randomly(driver)

        save_cookies(driver, cookie_file)
        logger.info("Login exitoso y cookies guardadas.")
    except Exception as e:
        logger.error(f"Error en login de Facebook: {e}")
        raise
    return driver
