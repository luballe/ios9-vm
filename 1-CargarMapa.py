from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os

# OS client
# 1=linux
# 2=windows
typeOfOSClient = 1

# Type or portal
# 1=http://mapas.bogota.gov.co/
# 2=http://portalmapas.catastrobogota.gov.co/
typeOfPortal = 1

# Type of browser driver
# 1=Firefox
# 2=Phantomjs
typeOfDriver = 2

# Log name
logName = "1-CargarMapa.txt"

# Se inicia el driver del browser
if typeOfDriver == 1:
  driver = webdriver.Firefox()
else:
  if typeOfOSClient:
    driver = webdriver.PhantomJS()
  else:
    driver = webdriver.PhantomJS("phantomjs.exe")

# Se configura la url y xpath
if typeOfPortal == 1:
  portalURL = "http://mapas.bogota.gov.co/"
  xPath ="//*[@id='cerrar_notificacion']"
else:
  portalURL = "http://portalmapas.catastrobogota.gov.co/"
  xPath ="//*[@id='jimu_dijit_CheckBox_0']/div[1]"

# Timeout despues de la carga de liberias
timeOutAfterLibsLoad = 600

# Se inicia el cronometro
start = time.time()

# Se inicia la carga del portal de mapas
driver.get(portalURL)

# Lap 1
end = time.time()

# Imprimir el titulo
#print "Liberias cargadas en: " + str(end - start) + " secs"
#with open(logName, "a") as myfile:
#  myfile.write(str(end - start)+"\n")
#print "File written!"

try:

  # Encontrar el ultimo elemento que carga el portal (Ventana de notificacion)
  element = WebDriverWait(driver, timeOutAfterLibsLoad).until(EC.presence_of_element_located((By.XPATH, xPath)))

  # Se finaliza el cronometro
  end = time.time()

  # Se imprime el tiempo de carga del portal
  #print "Portal cargado en: " + str(end - start) + " secs"
  # print str(end - start)
  with open(logName, "a") as myfile:
    myfile.write(str(end - start)+"\n")
  #print "File written!"

except TimeoutException:
  # Se finaliza el cronometro
  end = time.time()

  # Se imprime el tiempo
  #print "Time Out: " + str(end-start) + " secs... Mala cosa!"
  with open(logName, "a") as myfile:
    myfile.write(str(end - start)+"\n")
  #print "File written!"


finally:
  driver.quit()
