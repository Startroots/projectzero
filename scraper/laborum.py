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

#encontrar todos los trabajos
job_lists = driver.find_element_by_id('listado-avisos')
jobs = job_lists.find_elements_by_css_selector('a')

for job in jobs:
    try:
        name = job.find_element_by_css_selector('h2').get_attribute('innerText')
        job.click()
        print(name)
        
        
        dic = {'Title': name, 'Company': company, 'Date': time_, 'Link': link, 'Photo': photo, 'Description': desc, 'Function': func, 'Type': type_, 'Sector': sect, 'portal':'laborum'}
    except:
        print("Error")






#ficha aviso derecha
#job_lists = driver.find_element_by_id('ficha-Aviso')

