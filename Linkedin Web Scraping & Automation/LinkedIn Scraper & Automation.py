import requests
import pandas as pd 
from bs4 import BeautifulSoup
import string
import re

import os
import shutil

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime

excel_data = pd.read_excel('Input.xlsx')

data = pd.DataFrame(excel_data, columns=['URL'])

data = data.head(2)

url_s = data['URL']

name_list=[]

headline_list=[]


def getData():
	linkedin_email = "" # place your linkedin login email
	linkedin_password = "" # place your linkedin login password
	
	driver = webdriver.Chrome('chromedriver.exe')
	driver.get('https://www.linkedin.com/login')

	driver.find_element("xpath", '//*[@id="username"]').send_keys(linkedin_email)
	driver.find_element("xpath", '//*[@id="password"]').send_keys(linkedin_password)
	driver.find_element("xpath", '//*[@id="organic-div"]/form/div[3]/button').click()


	for urls in url_s:

		time.sleep(2)
		
		driver.get(urls)
		driver.maximize_window()
		
		soup = BeautifulSoup(driver.page_source,'html.parser')
		table = soup.find()
		time.sleep(5)
		
		try:
			name_person = driver.find_element("xpath", '//*[@id="ember29"]/div[2]/div[2]/div[1]/div[1]/h1').text
			name_list.append(name_person)
		except:
			name_person = 'None'
			name_list.append(name_person)

		time.sleep(4)

		try:
			headline_person = driver.find_element("xpath", '//*[@id="ember29"]/div[2]/div[2]/div[1]/div[2]').text
			headline_list.append(headline_person)
		except:
			headline_person = 'None'
			headline_list.append(headline_person)

		time.sleep(3)
            
getData()

dict = {'URL': url_s, 'Name': name_list, 'Headline': headline_list}  
       
df = pd.DataFrame(dict)

csv_name = "Output Linkedin.csv"

df.to_csv(csv_name,index=False)
