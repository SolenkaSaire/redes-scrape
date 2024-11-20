from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from src.common.human_behavior import HumanBehavior

def search_instagram(driver, search_query):
    HumanBehavior.simulate_human_behavior(driver)
    search_icon = driver.find_element(By.XPATH, "//span[@aria-describedby and contains(@class, 'x1i10hfl')]//a[@role='link']")
    search_icon.click()
    time.sleep(1)  # Esperar a que el cuadro de búsqueda aparezca
    search_box = driver.find_element(By.XPATH, "//input[@placeholder='Buscar']")
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)  # Esperar a que los resultados carguen


def scrape_instagram_profile(driver):
    HumanBehavior.simulate_human_behavior(driver)
    # Esperamos que los resultados se carguen y seleccionamos el primer perfil
    first_result = driver.find_element(By.XPATH, "//a[contains(@href,'/')]")
    first_result.click()
    time.sleep(3)  # Esperamos a que el perfil cargue completamente
    
    # Obtener detalles del perfil
    profile_info = {}
    profile_info['username'] = driver.find_element(By.XPATH, "//h1[@class='_7UhW9']").text
    profile_info['bio'] = driver.find_element(By.XPATH, "//div[@class='-vDIg']").text
    profile_info['followers'] = driver.find_element(By.XPATH, "//a[contains(@href,'/followers/')]//span").text
    profile_info['following'] = driver.find_element(By.XPATH, "//a[contains(@href,'/following/')]//span").text
    
    return profile_info
