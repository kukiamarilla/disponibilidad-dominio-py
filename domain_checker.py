from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
import sys

# Configuración del navegador
def setup_browser():
    # Usa Chrome con Selenium
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Ejecutar el navegador en modo headless (sin interfaz gráfica)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Instalar y utilizar ChromeDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

# Función para verificar la disponibilidad del dominio
def check_domain_availability(domain_name):
    driver = setup_browser()

    # Visitar la página del NIC
    driver.get("https://www.nic.py/")
    time.sleep(3)

    # Dividir el dominio completo en nombre y tipo
    domain_parts = domain_name.split('.')
    if len(domain_parts) < 2 or domain_parts[-1] != "py":
        raise ValueError("Invalid domain format. Domain must end with .py.")

    domain_name = domain_parts[0]
    domain_type = domain_parts[1]  # Obtener el tipo de dominio

    # Seleccionar el tipo de dominio
    domain_select = driver.find_element(By.XPATH, '//select')
    domain_select.click()  # Abre el menú de selección
    time.sleep(1)  # Esperar un momento para asegurarnos que el menú se abre

    # Seleccionar la opción correspondiente al tipo de dominio
    option = driver.find_element(By.CSS_SELECTOR, f'[value="{domain_type}"]')
    option.click()

    # Encontrar el campo de búsqueda y enviar el nombre del dominio
    search_box = driver.find_element(By.XPATH, '//input[2]')
    search_box.send_keys(domain_name)

    # Hacer clic en el botón para buscar
    search_button = driver.find_element(By.ID, 'enviar_formulario')
    search_button.click()

    # Esperar a que la página se cargue
    time.sleep(3)
    try:
        # Usar el selector CSS proporcionado para obtener el estado del dominio
        status_element = driver.find_element(By.ID, 'resultados_disponibilidad')
        status_text = status_element.text

        # Cerrar el navegador
        driver.quit()

        rows = status_text.split("\n")

        avalabilities = {}
        for row in rows:
            row_availabity = row.split(" ")

            avalabilities[row_availabity[0].strip()] = row_availabity[1].strip() == "Disponible"
        return json.dumps(avalabilities)

    except Exception as e:
        # Cerrar el navegador en caso de excepción
        driver.quit()
        raise e

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise ValueError("Domain name not provided.")
    domain_name = sys.argv[1]
    print(check_domain_availability(domain_name))