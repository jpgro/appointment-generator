import time
from selenium import webdriver
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://citas.sre.gob.mx")
print(driver.title)
time.sleep(5)
elem = driver.find_element_by_xpath("/html/body/div[2]/div/main/div/div/div/div/div[1]/div/div/div/div/div/div/div/div[3]/div/div/div/button[1]")
elem.click()
driver.implicitly_wait(10)
elem_2 = driver.find_element_by_xpath("/html/body/div[2]/div/main/div/div/div/div/div[4]/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/button[2]")
elem_2.click()

email = driver.find_element_by_xpath("/html/body/div[2]/div/main/div/div/div/div/div[4]/div[2]/div[3]/div/div/div/div[2]/form/div[1]/div/input")
email.send_keys("juanpabloguerreroe@gmail.com")
password = driver.find_element_by_xpath("/html/body/div[2]/div/main/div/div/div/div/div[4]/div[2]/div[3]/div/div/div/div[2]/form/div[2]/div/input")
password.send_keys("Juan20052020@")
terms = driver.find_element_by_xpath("/html/body/div[2]/div/main/div/div/div/div/div[4]/div[2]/div[3]/div/div/div/div[2]/form/div[4]/div/div/label/input")
terms.click()
driver.implicitly_wait(10)
#SVG ELEMENT TO FIX
WebElement_m= driver.find_element_by_css_selector(".modal-body path:nth-child(3)")
WebElement_m.click()

driver.implicitly_wait(10)
ingresar = driver.find_element_by_xpath("/html/body/div[2]/div/main/div/div/div/div/div[4]/div[2]/div[4]/div/div/div/div[2]/form/div[5]/div/div/div[2]/button")
ingresar.click()

driver.implicitly_wait(10)
confirmacion_datos = driver.find_element_by_css_selector("body > div:nth-child(3) > div.container > div:nth-child(1) > div > div > div > div > div > div > div > div > div > a > span > svg > path:nth-child(3)")
confirmacion_datos.click()

programar = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[3]/div[3]/a")
programar.click()

aviso_programar = driver.find_element_by_css_selector("body > div:nth-child(3) > div.container > div:nth-child(3) > div > div > div > div:nth-child(2) > div:nth-child(1) > div > div > div > div > div > div > div > a > span > svg > path:nth-child(3)")
aviso_programar.click()

toggle_menu = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[3]/div/div/div/div[2]/div[1]/form/div[1]/div[3]/div[1]/div/div/div/div[1]")
toggle_menu.click()
driver.implicitly_wait(10)
while True:
    if "Sin opciones" in driver.page_source:
        print("No hay citas disponibles")
        time.sleep(10)
        driver.refresh()
        driver.implicitly_wait(30)
        aviso_programar = driver.find_element_by_css_selector("body > div:nth-child(3) > div.container > div:nth-child(3) > div > div > div > div:nth-child(2) > div:nth-child(1) > div > div > div > div > div > div > div > a > span > svg > path:nth-child(3)")
        aviso_programar.click()
        toggle_menu = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[3]/div/div/div/div[2]/div[1]/form/div[1]/div[3]/div[1]/div/div/div/div[1]")
        toggle_menu.click()
        driver.implicitly_wait(10)
    else:
        print('Text Absent')

# TO DO
# Enviar un mensaje de Whatsapp cuando haya una cita disponible
# Correrlo 24/7 en nube
