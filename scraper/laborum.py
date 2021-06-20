import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

url = "https://www.laborum.cl/empleos-practica-profesional.html"

driver.get(url)
driver.maximize_window()

#20 por pagina
no_of_jobs = int(driver.find_element_by_css_selector('h1>span').get_attribute('innerText'))
print("Numero de anuncios: ", no_of_jobs)

for i in range(2,20):
    try:
        driver.find_element_by_xpath(f'//*[@id="listado-avisos"]/div[{i}]/a/div[1]/h3[1]').click()
        time.sleep(3)
        empresa = driver.find_element_by_xpath(f'//*[@id="listado-avisos"]/div[{i}]/a/div[1]/h3[1]').get_attribute('innerText')
        titulo = driver.find_element_by_xpath(f'//*[@id="listado-avisos"]/div[{i}]/a/div[2]/h2').get_attribute('innerText')
        print(titulo, empresa)
    except:
        print("error")
