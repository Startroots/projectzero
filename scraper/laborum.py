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
#jobs = job_lists.find_elements_by_tag_name('li') # return a list

"""
/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[2]
/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[3]
/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[4]
/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div[5]
"""

for job in job_lists:
    test = job
    name = test.find_element_by_css_selector('h2').get_attribute('innerText')
    
    print(name)



#ficha aviso derecha
job_lists = driver.find_element_by_id('listado-avisos')

