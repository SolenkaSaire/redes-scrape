import time
import os
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from googletrans import Translator

def scrape_facebook_profiles(driver):
    data = []
    translator = Translator()
    

    try:
        print("Iniciando scraping de página de Facebook...")

        # Esperar a que la página cargue completamente
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )

        # Extraer nombre de la cuenta
        try:
            nombre_cuenta = WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[3]/div/div/div[1]/div/div/span/h1'))
            ).text.strip()
        except TimeoutException:
            nombre_cuenta = "N/A"

        print(f"Nombre de la cuenta: {nombre_cuenta}")

        # Abrir filtros de publicaciones
        try:
            filtros_button = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div'))
            )
            filtros_button.click()
            print("Filtros abiertos.")
        except TimeoutException:
            print("No se pudo encontrar el botón de filtros.")
            return

        # Seleccionar el año 2024
        try:
            year_dropdown = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div[1]/div/div[2]/div/div/div/div[1]/div/div/div[1]/i'))
            )
            year_dropdown.click()
            time.sleep(1)

            year_2024 = driver.find_element(By.XPATH, '//span[text()="2024"]')
            year_2024.click()
            print("Año 2024 seleccionado.")
        except NoSuchElementException:
            print("No se pudo seleccionar el año 2024.")
            return
        time.sleep(5)

        # Seleccionar noviembre
        try:
            month_dropdown = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, '//span[text()="Mes"]'))
            )
            month_dropdown.click()
            time.sleep(1)

            november_option = driver.find_element(By.XPATH, '//span[text()="noviembre"]')
            november_option.click()
            print("Mes noviembre seleccionado.")
        except NoSuchElementException:
            print("No se pudo seleccionar el mes de noviembre.")
            return
        
        time.sleep(5)
        # Confirmar selección
        try:
            confirm_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[3]/div[2]/div/div[2]/div[1]')
            confirm_button.click()
            time.sleep(2)
            print("Filtros aplicados correctamente.")
        except NoSuchElementException:
            print("No se encontró el botón 'Listo' usando el XPath proporcionado.")
            return
        except Exception as e:
            print(f"Error al intentar hacer clic en el botón 'Listo': {e}")
            return

        time.sleep(15)


        # Contar publicaciones en noviembre 2024
        try:
            print("Iniciando extracción de publicaciones...")
            
            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@aria-label, "Publicación")]'))
            )
            print("Publicaciones cargadas correctamente.")

            publicaciones = driver.find_elements(By.XPATH, '//div[contains(@aria-label, "Publicación")]')
            print(f"Total de publicaciones encontradas: {len(publicaciones)}")
            
            
            
            # Iterar sobre cada publicación
            for publicacion in publicaciones:
                try:
                    # Esperar y localizar la fecha de publicación
                    fecha_element = WebDriverWait(publicacion, 10).until(
                        EC.presence_of_element_located((By.XPATH, './/div[contains(@class, "timestamp")]'))
                    )
                    fecha_texto = fecha_element.text.lower()
                    print(f"Fecha de publicación: {fecha_texto}")

                    # Verificar si la fecha corresponde a noviembre 2024
                    if "noviembre 2024" in fecha_texto:
                        contador_noviembre_2024 += 1

                except NoSuchElementException:
                    # Si no se encuentra la fecha, continuar con la siguiente publicación
                    print("Fecha no encontrada en esta publicación.")
                    continue
                except TimeoutException:
                    # Si la fecha no se encuentra dentro del tiempo esperado
                    print("Tiempo de espera agotado para obtener la fecha de la publicación.")
                    continue

            print(f"Número de publicaciones en noviembre 2024: {contador_noviembre_2024}")

        except Exception as e:
            print(f"Error al contar publicaciones: {e}")
            
        # Extraer el número de seguidores de la página
        try:
            seguidores_element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[3]/div/div/div[2]/span/a[2]')
            seguidores_texto = seguidores_element.text.strip()
            print(f"Número de seguidores de la página: {seguidores_texto}")
        except NoSuchElementException:
            seguidores_texto = "No disponible"
            print("No se pudo obtener el número de seguidores de la página.")

        # Extraer número de seguidos
        try:
            print("Antes de extraer número de seguidos...")
            seguidos_element = driver.find_element(By.XPATH, "//span[contains(text(), 'seguidos')]")
            numero_seguidos = int(seguidos_element.text.split()[0].replace(',', '').replace('.', ''))
            print("Número de seguidos extraido.")
        except Exception:
            numero_seguidos = 'N/A'

        # Extraer la descripción de la página
        try:
            descripcion_element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/span')
            descripcion_texto = descripcion_element.text.strip()
            print(f"Descripción de la página: {descripcion_texto}")

            # Traducir la descripción al español
            if descripcion_texto:
                descripcion_texto = translator.translate(descripcion_texto, src='en', dest='es').text
                print(f"Descripción traducida al español: {descripcion_texto}")
        except NoSuchElementException:
            descripcion_texto = "No disponible"
            print("No se pudo obtener la descripción de la página.")
        except Exception as e:
            descripcion_texto = "No disponible"
            print(f"Error al traducir la descripción: {e}")


        # Agregar datos recolectados
        data.append({
            "nombre_cuenta": nombre_cuenta,
            "publicaciones_noviembre_2024": contador_noviembre_2024,
            "seguidores": seguidores_texto,
            "seguidos": numero_seguidos,
            "descripcion": descripcion_texto
        })



        # Guardar datos en un archivo CSV
        df = pd.DataFrame(data)
        if not os.path.exists('data'):
            os.makedirs('data')
        df.to_csv("data/Cuentas.csv", index=False, encoding='utf-8')

        print("Scraping completado. Datos guardados en 'data/Cuentas.csv'.")

    except Exception as e:
        print(f"Error durante el scraping: {e}")



def scrape_facebook_posts(driver):
    """
    Realiza scraping de las publicaciones de una página de Facebook.
    Guarda la información en un archivo CSV llamado 'publicaciones.csv'.
    """
    data = []
    post_counter = 1
    translator = Translator()

    try:
        print("Iniciando scraping de publicaciones de Facebook...")

        # Esperar a que la página cargue completamente
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )

        # Esperar y recorrer las publicaciones
        posts = driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[3]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div")

        for post in posts:
            try:
                # Extraer descripción
                description = post.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[3]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[13]/div/div/div[3]/div[1]/div/div/div/div/span/div/div').text.strip()
                description_es = translator.translate(description, src='en', dest='es').text  # Traducir descripción

                # Extraer reacciones
                reactions = post.find_element(By.XPATH, './/div[@aria-label="Me gusta, Me encanta, Me importa, Me divierte, Me asusta, Me entristece"]').text.strip()

                # Extraer los comentarios con más reacciones
                comments_section = post.find_elements(By.XPATH, './/div[@aria-label="Comentarios"]')
                comments_reactions = []
                for comment in comments_section:
                    try:
                        comment_text = comment.find_element(By.XPATH, './/span[@dir="auto"]').text.strip()
                        comment_reactions = comment.find_element(By.XPATH, './/div[@aria-label="Reacciones"]').text.strip()
                        comments_reactions.append((comment_text, comment_reactions))
                    except NoSuchElementException:
                        continue

                # Guardar los datos en el diccionario
                post_data = {
                    'Id_publicación': post_counter,
                    'Descripcion': description_es,
                    'Reacciones': reactions,
                    'Comentarios': [c[0] for c in comments_reactions],
                    'Comentarios_reacciones': [c[1] for c in comments_reactions]
                }
                data.append(post_data)

                # Incrementar el contador de publicaciones
                post_counter += 1

            except NoSuchElementException as e:
                print(f"Error al extraer información de una publicación: {e}")
                continue

        # Guardar los datos en un archivo CSV
        df = pd.DataFrame(data)
        df.to_csv("publicaciones.csv", index=False, encoding="utf-8")
        print("Datos de publicaciones guardados en 'publicaciones.csv'.")

    except Exception as e:
        print(f"Error al realizar el scraping de publicaciones: {e}")