# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 18:46:34 2021

@author: Javiera
"""

from bs4 import BeautifulSoup
import requests
import time
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())

url = "https://www.linkedin.com/jobs/search/?geoId=104621616&keywords=intern&location=Chile"

driver.get(url)
driver.maximize_window()

no_of_jobs = int(driver.find_element_by_css_selector('h1>span').get_attribute('innerText'))
print("Numero de anuncios: ", no_of_jobs)

#abrir todas las paginas de empleos
i = 2
while i <= int(no_of_jobs/25)+1: 
    time.sleep(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    i = i + 1
    try:
        path = '/html/body/main/div/section/button'
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, path)))
        driver.find_element_by_xpath(path).click()
    except:
        pass


#encontrar todos los trabajos
job_lists = driver.find_element_by_class_name('jobs-search__results-list')
jobs = job_lists.find_elements_by_tag_name('li') # return a list

data = []
cont = 0
for job in jobs:

    test = job
    time.sleep(3)
    name = test.find_element_by_css_selector('h3').get_attribute('innerText')
    company = test.find_element_by_css_selector('h4').get_attribute('innerText')
    time_ = test.find_element_by_css_selector('time').get_attribute('innerText')
    link = test.find_element_by_css_selector('a').get_attribute('href')
    print("NOMBRE: ", name, "TIME: ", time_, "LINK: ", link, "COMPANY: ", company)
    
    test.click()
    time.sleep(3)
    
    try:   
        photo = driver.find_element_by_xpath('/html/body/div[1]/div/section/div[2]/section[1]/div/a/img').get_attribute('src')
    except:
        photo = "https://static-exp1.licdn.com/sc/h/9a9u41thxt325ucfh5z8ga4m8"
    desc = driver.find_element_by_xpath('/html/body/div[1]/div/section/div[2]/section[2]/div/section/div').get_attribute('innerText')
    list_funciones = driver.find_element_by_xpath('/html/body/div[1]/div/section/div[2]/section[2]/ul')
    funciones = list_funciones.find_elements_by_tag_name('li')
    type_ = ""
    func = ""
    sect = ""
    for item in funciones:
        if "Tipo" in item.get_attribute("innerText"):
            type_ = item.get_attribute("innerText").split("\n")[1].replace(" ","")
        if "unción laboral" in item.get_attribute("innerText"):
            func = item.get_attribute("innerText").replace(" ","").split("\n")[1:]
        if "ectores" in item.get_attribute("innerText"):
            sect = item.get_attribute("innerText").split("\n")[1].replace(" ","")         
            
    print("DESC: ", desc, "FUNCIONES: ", list_funciones)
    dic = {'Title': name, 'Company': company, 'Date': time_, 'Link': link, 'Photo': photo, 'Description': desc, 'Function': func, 'Type': type_, 'Sector': sect, 'portal':'linkedin'}
    data.append(dic)
    cont = cont + 1    


output = pd.DataFrame()
output = output.append(data, ignore_index=True, sort=False)

output.to_excel('test1.xlsx', index = False)









