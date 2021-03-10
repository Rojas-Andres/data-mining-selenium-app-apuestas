from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time 
import pandas as pd
import io
encoding = 'UTF-8'
archivo_datos=io.open("archivo.txt","w",encoding=encoding)
#Opciones de navegacion

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')


driver_path = "D:\ASUS\Documents\PROYECTOS\selenium\chromedriver.exe"

driver = webdriver.Chrome(driver_path,chrome_options=options)

#Inicializamos el navegador
driver.get("https://www.wplay.co/")
#time.sleep(10)
#Usamos ruta absoluta
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[1]/div/div/div[2]/div/div[1]/a')))\
    .click()

#$x("//div[@class='fragment expander coupon-for-type']//h4[contains(text(),'Ligue 1')]")
#$x("//li[@class='expander expander-collapsed sport-FOOT']//span[contains(text(),'Futbol')]")

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      "//li[@class='expander expander-collapsed sport-FOOT']//span[contains(text(),'Futbol')]")))\
    .click()
#/html/body/div[1]/div/div[3]/div/div/div[1]/div[4]/ul/li[1]/ul/li[14]/div/span
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      "/html/body/div[1]/div/div[3]/div/div/div[1]/div[4]/ul/li[1]/ul/li[14]/div/span")))\
    .click()

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      "/html/body/div[1]/div/div[3]/div/div/div[1]/div[4]/ul/li[1]/ul/li[14]/ul/li/a/span")))\
    .click()

#$x("//table[@class='coupon coupon-horizontal coupon-scoreboard ']")

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      "//table[@class='coupon coupon-horizontal coupon-scoreboard ']")))\


texto = driver.find_element_by_xpath("//table[@class='coupon coupon-horizontal coupon-scoreboard ']")
#print(texto)
texto = texto.text
print("texto es:\n")
#print(texto)
dic = dict()
equipo = 0
partidos2 = texto.split('>')
equipo1 = list()
equipo1_valor = list()

empate_valor = list()

equipo2 = list()
equipo2_valor = list()
dia_partido = list()
hora_partido = list()
#Primer equipo tiene una estructura diferente
primer_partido = partidos2[0].split('\n')
hora_partido.append(primer_partido[1])
dia_partido.append(primer_partido[2])
equipo1.append(primer_partido[4])
equipo1_valor.append(primer_partido[5])
equipo2.append(primer_partido[9])
equipo2_valor.append(primer_partido[10])
empate_valor.append(primer_partido[7])

partidos2.pop(0)
for i in partidos2:
    print(i)
    val = i.split('\n')
    print("el valor es\n ",val)
    if len(val) > 7:
        hora_partido.append(val[3])
        dia_partido.append(val[4])
        equipo1.append(val[6])
        equipo1_valor.append(val[7])
        empate_valor.append(val[9])
        equipo2.append(val[11])
        equipo2_valor.append(val[12])
df = pd.DataFrame({'equipo1': equipo1, 'valor_eq1': equipo1_valor, 'valor_empate':empate_valor,'equipo2': equipo2, 'valor_eq2': equipo2_valor, 'dia_partido':dia_partido,'hora_partido':hora_partido})

print(df)
df.to_csv('partidos.csv', index=False)
driver.quit()
