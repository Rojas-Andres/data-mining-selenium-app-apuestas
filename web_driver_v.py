from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time 
import pandas as pd
import io
encoding='UTF-8'
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
print(texto)
texto = texto.text
print(texto)
dic = dict()
equipo = 0
partidos = texto.split('Mar')
partidos.pop(0)

equipo1 = list()
equipo1_valor = list()

empate_valor = list()

equipo2 = list()
equipo2_valor = list()

for i in partidos:
    val = i.split("\n")
    equipo +=1
    new_dic = {}
    new_dic[val[2]] = val[3]
    new_dic[val[4]] = val[5]
    new_dic[val[7]] = val[8]

    equipo1.append(val[2])
    equipo1_valor.append(val[3])
    empate_valor.append(val[5])
    equipo2.append(val[7])
    equipo2_valor.append(val[8])
    
    #archivo_datos.write("{}-{}[[{}-{}[[{}-{}\n".format(val[2],val[3],val[4],val[5],val[7],val[8]))
    
    dic[str(equipo)] = new_dic
df = pd.DataFrame({'equipo1': equipo1, 'valor_eq1': equipo1_valor, 'valor_empate':empate_valor,'equipo2': equipo2, 'valor_eq2': equipo2_valor })

print(df)
df.to_csv('tiempo_hoy.csv', index=False)

archivo_datos.write(str(dic))
driver.quit()

