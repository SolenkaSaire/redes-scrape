import pickle
import os

def save_cookies(driver, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as file:
        pickle.dump(driver.get_cookies(), file)

def load_cookies(driver, path):
    if os.path.exists(path):
        with open(path, "rb") as file:
            cookies = pickle.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)
        return True
    return False
