from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuración para evitar que se abra la ventana del navegador (modo headless)
options = Options()
options.add_argument("--headless")  # Comentar esta línea si quieres ver el navegador


driver = webdriver.Chrome(options=options)

try:
    driver.get("http://books.toscrape.com")

    # Esperar hasta que los libros estén cargados
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article.product_pod")))

    books = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")

    for book in books:
        title = book.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a").get_attribute("title")
        price = book.find_element(By.CSS_SELECTOR, "p.price_color").text
        availability = book.find_element(By.CSS_SELECTOR, "p.instock.availability").text.strip()
        print(f"Título: {title} | Precio: {price} | Disponibilidad: {availability}")

finally:
    driver.quit()
