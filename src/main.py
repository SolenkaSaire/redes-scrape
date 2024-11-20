import os
import pandas as pd
from src.facebook.login import facebook_login
from src.instagram.login import instagram_login
from src.facebook.scraping import scrape_facebook_profiles
from src.facebook.scraping import scrape_facebook_posts
from src.instagram.scraping import search_instagram, scrape_instagram_profile
from src.common.driver_manager import get_web_driver
from src.config.settings import Config
import time

def save_to_excel(data, filename):
    if not os.path.exists('data'):
        os.makedirs('data')
    
    df = pd.DataFrame(data)
    df.to_excel(f'data/{filename}', index=False, engine='openpyxl')

def main():
    driver = get_web_driver()
    url_to_scrape = Config.URL_TO_SCRAPE

    if "facebook.com" in url_to_scrape:
        if facebook_login(driver):
            driver.get(url_to_scrape)
            print("URL cargada EN NVIDIA.")
            time.sleep(20)

            # Llamar a la función de scraping de Facebook
            scrape_facebook_profiles(driver)

            # Llamar a al función de scraping de publicaciones
            #scrape_facebook_posts(driver)
            
        driver.quit()

    elif "instagram.com" in url_to_scrape:
        if instagram_login(driver):
            driver.get(url_to_scrape)
            time.sleep(2)
        driver.quit()
    else:
        print("URL no válida.")

if __name__ == "__main__":
    main()
