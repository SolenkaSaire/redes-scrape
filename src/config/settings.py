import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    COOKIE_STORAGE_PATH = "cookies/"
    FACEBOOK_URL = "https://www.facebook.com"
    INSTAGRAM_URL = "https://www.instagram.com"

    URL_TO_SCRAPE = os.getenv("URL_TO_SCRAPE")

    FACEBOOK_CREDENTIALS = {
        "username": os.getenv("FACEBOOK_USERNAME"),
        "password": os.getenv("FACEBOOK_PASSWORD")
    }
    INSTAGRAM_CREDENTIALS = {
        "username": os.getenv("INSTAGRAM_USERNAME"),
        "password": os.getenv("INSTAGRAM_PASSWORD")
    }

    # Crear carpeta de cookies automáticamente si no existe
    @staticmethod
    def ensure_cookie_directory():
        if not os.path.exists(Config.COOKIE_STORAGE_PATH):
            os.makedirs(Config.COOKIE_STORAGE_PATH)
            print(f"Carpeta creada: {Config.COOKIE_STORAGE_PATH}")
        else:
            print(f"Carpeta existente: {Config.COOKIE_STORAGE_PATH}")

# Llamada para asegurar la creación de la carpeta
Config.ensure_cookie_directory()
