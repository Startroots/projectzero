# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 23:52:53 2021

@author: Javiera
"""

import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

url = "https://www.linkedin.com/jobs/search/?geoId=104621616&keywords=intern&location=Chile"

driver.get(url)
driver.maximize_window()

no_of_jobs = int(driver.find_element_by_css_selector('h1>span').get_attribute('innerText'))
print("Numero de anuncios: ", no_of_jobs)

#abrir todas las paginas de empleos
i = 2
while i <= int(no_of_jobs/25)+1: 
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    i = i + 1
    try:
        driver.find_element_by_xpath('/html/body/main/div/section/button').click()
        time.sleep(5)
    except:
        pass
        time.sleep(5)


#encontrar todos los trabajos
job_lists = driver.find_element_by_class_name('jobs-search__results-list')
jobs = job_lists.find_elements_by_tag_name('li') # return a list


#detalles generales de cada trabajo
job_id= []
job_title = []
company_name = []
date = []
job_link = []

#detalles especificos
jd = []
job_func = []


cont = 0
for job in jobs:
    if cont == 5:
        pass
    
    # clicking job to view job details
    job_click_path = f'/html/body/main/div/section[2]/ul/li[{cont+1}]/img'
    job_click = driver.find_element_by_xpath(job_click_path).click()
    time.sleep(5)

    job_id0 = job.get_attribute('data-id')
    job_id.append(job_id0)
    
    job_title0 = job.find_element_by_css_selector('h3').get_attribute('innerText')
    job_title.append(job_title0)
    
    company_name0 = job.find_element_by_css_selector('h4').get_attribute('innerText')
    company_name.append(company_name0)
    
    date0 = job.find_element_by_css_selector('div>div>time').get_attribute('datetime')
    date.append(date0)
    
    job_link0 = job.find_element_by_css_selector('a').get_attribute('href')
    job_link.append(job_link0)
    
    #-------------------------------------------------

     
    #job description
    job_desc = driver.find_element_by_xpath('//div[@class="show-more-less-html__markup show-more-less-html__markup--clamp-after-5"]')
    soup = BeautifulSoup(job_desc.get_attribute('outerHTML'), 'html.parser')
    print("Job desc ready")
    jd.append(soup.get_text(separator='\n\n'))
    
     
    job_func_path = '/html/body/main/section/div[2]/section[2]/ul/li[3]/span'
    #job_func_path = '//*[@id="main-content"]/section/div[2]/section[2]/ul/li[3]'
    job_func_elements = job.find_elements_by_xpath(job_func_path)
    jf = []
    for element in job_func_elements:
        word = element.get_attribute('innerText')
        print(word)
        jf.append(word)   
    job_func_final = ', '.join(jf)
    job_func.append(job_func_final) 
    
    cont = cont + 1


#guardar en dataframe
job_data = pd.DataFrame({'ID': job_id,
'Date': date,
'Company': company_name,
'Title': job_title,
#'Location': location,
'Description': jd,
#'Level': seniority,
#'Type': emp_type,
'Function': job_func,
#'Industry': industries,
'Link': job_link
})

# cleaning description column
#job_data['Description'] = job_data['Description'].str.replace('\n',' ')

job_data.to_excel('LinkedIn_intern_jobs_2_chile.xlsx', index = False)
