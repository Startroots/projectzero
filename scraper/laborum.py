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
jobs = job_lists.find_elements_by_tag_name('li') # return a list


