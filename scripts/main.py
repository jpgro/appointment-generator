import time
from selenium import webdriver
from twilio.rest import Client
from datetime import date
PATH = "C:\Program Files (x86)\chromedriver.exe"

accountSID = 'ACb116c9a2032bf11f36eea6983606e750'
authToken = 'a44b45fd3fc99564d3e866e4f7b57ba5'
client = Client(accountSID, authToken)
driver = webdriver.Chrome(PATH)
def enter_site():

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
def availability_check():
        time.sleep(10)
        driver.refresh()
        aviso_programar = driver.find_element_by_css_selector("body > div:nth-child(3) > div.container > div:nth-child(3) > div > div > div > div:nth-child(2) > div:nth-child(1) > div > div > div > div > div > div > div > a > span > svg > path:nth-child(3)")
        aviso_programar.click()
        toggle_menu = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[3]/div/div/div/div[2]/div[1]/form/div[1]/div[3]/div[1]/div/div/div/div[1]")
        toggle_menu.click()

def availability_loop():
    while "Sin Opciones" in driver.page_source:
        print("\nNo hay citas disponibles")
        availability_check()

    else:
        print('\nText Absent')
        message = client.messages.create(body=f"Hay citas disponibles para el pasaporte en este momento. {date}", from_='+16067663435', to='+524421171464')
        time.sleep(30)
        availability_check()

enter_site()
time.sleep(10)
availability_loop()

        

# TO DO
# Enviar un mensaje de Whatsapp cuando haya una cita disponible
# Correrlo 24/7 en nube
