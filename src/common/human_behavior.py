import time
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class HumanBehavior:
    @staticmethod
    def random_wait(min_time=1, max_time=3):
        """Espera un tiempo aleatorio entre min_time y max_time segundos."""
        wait_time = random.uniform(min_time, max_time)
        time.sleep(wait_time)

    @staticmethod
    def scroll_page(driver, scroll_times=2, min_scroll=300, max_scroll=800):
        """Desplaza la página hacia abajo y hacia arriba varias veces."""
        for _ in range(scroll_times):
            scroll_distance = random.randint(min_scroll, max_scroll)
            driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
            HumanBehavior.random_wait()
            driver.execute_script(f"window.scrollBy(0, {-scroll_distance // 2});")
            HumanBehavior.random_wait()

    @staticmethod
    def move_mouse_randomly(driver, times=5):
        """Mueve el ratón a posiciones aleatorias en la página."""
        actions = ActionChains(driver)
        for _ in range(times):
            x_offset = random.randint(0, 100)
            y_offset = random.randint(0, 100)
            actions.move_by_offset(x_offset, y_offset).perform()
            HumanBehavior.random_wait(0.1, 0.3)
            actions.move_by_offset(-x_offset, -y_offset).perform()

    @staticmethod
    def type_like_human(element, text, delay_range=(0.1, 0.3)):
        """Escribe en un elemento con un retraso entre cada letra."""
        for char in text:
            element.send_keys(char)
            time.sleep(random.uniform(*delay_range))

    @staticmethod
    def simulate_human_behavior(driver):
        """Simula una serie de comportamientos humanos en la página."""
        # Realizar un desplazamiento hacia abajo y hacia arriba
        HumanBehavior.scroll_page(driver, scroll_times=2)

        # Mover el ratón de forma aleatoria
        HumanBehavior.move_mouse_randomly(driver, times=3)

        # Esperar aleatoriamente entre acciones
        HumanBehavior.random_wait(min_time=2, max_time=5)