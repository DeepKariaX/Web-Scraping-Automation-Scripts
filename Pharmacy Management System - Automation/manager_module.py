from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime


#Loads chrome with default settings
opt=Options()
opt.add_argument("start-maximized")
opt.add_argument("--disable-notifications")
opt.add_argument("--no-sandbox")
opt.add_argument("--disable-popup-window")
opt.add_argument("--disable-extensions")
# opt.add_experimental_option("useAutomationExtension", False)
# opt.add_experimental_option("excludeSwitches",["enable-automation"])
# caps = opt.to_capabilities()
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
"download_restrictions": 3,
"download.prompt_for_download": False,
"profile.default_content_setting_values.media_stream_mic": 0,
"profile.default_content_setting_values.media_stream_camera":0,
"profile.default_content_setting_values.geolocation": 0,
"profile.default_content_setting_values.notifications": 0,
"credentials_enable_service": False,
"profile.password_manager_enabled": False
})

def open_login():
	global driver
	#Gives path to chrome webdriver and loads classroom webpage
	driver=webdriver.Chrome(chrome_options=opt, executable_path='chromedriver.exe')
	driver.get('http://localhost/pms/index.php')
	time.sleep(5)
	driver.find_element_by_xpath("/html/body/main/nav/div/div/button").click()
	wait = WebDriverWait(driver, 10)

def login_manager():
	global mail_,pass__
	driver.find_element_by_xpath("/html/body/div/div[1]/div/div/div[2]/div/div/form/fieldset/div[1]/input").send_keys("disha@manager.com")
	driver.find_element_by_xpath("/html/body/div/div[1]/div/div/div[2]/div/div/form/fieldset/div[2]/input").send_keys("d2")
	driver.find_element_by_xpath("/html/body/div/div[1]/div/div/div[2]/div/div/form/fieldset/div[3]/select/option[2]").click()
	time.sleep(5)
	driver.find_element_by_xpath("/html/body/div/div[1]/div/div/div[2]/div/div/form/fieldset/input").click()


def add_pharmacist():
	driver.find_element_by_xpath("/html/body/section[2]/ul/li[3]/a").click()

	driver.find_element_by_xpath("/html/body/section[3]/div/div[2]/div/div/form/div/div[1]/label/input").send_keys("Raj")
	driver.find_element_by_xpath("/html/body/section[3]/div/div[2]/div/div/form/div/div[2]/label/input").send_keys("Patel")
	driver.find_element_by_xpath("/html/body/section[3]/div/div[2]/div/div/form/div/div[3]/label/input").send_keys("raj@pharmacist.com")
	driver.find_element_by_xpath("/html/body/section[3]/div/div[2]/div/div/form/div/div[4]/label/input").send_keys("9384343")
	driver.find_element_by_xpath("/html/body/section[3]/div/div[2]/div/div/form/div/div[5]/label/input").send_keys("123")
	time.sleep(5)
	driver.find_element_by_xpath("/html/body/section[3]/div/div[2]/div/div/form/div/div[6]/input").click()
	time.sleep(5)
	driver.find_element_by_xpath("/html/body/section[2]/ul/li[4]/a").click()

def edit_pharmacist():
	driver.find_element_by_xpath("/html/body/section[2]/ul/li[4]/a").click()
	driver.find_element_by_xpath("/html/body/section[3]/div/div[2]/div/div/table/tbody/tr[2]/td[5]/a/i").click()
	
	driver.find_element_by_xpath("/html/body/section[3]/div/div[2]/div/div/form/div/div[3]/label/input").clear()
	driver.find_element_by_xpath("/html/body/section[3]/div/div[2]/div/div/form/div/div[3]/label/input").send_keys("rajpatel@pharmacist.com")

	time.sleep(3)
	driver.find_element_by_xpath("/html/body/section[3]/div/div[2]/div/div/form/div/div[5]/input").click()
	
	time.sleep(3)
	driver.find_element_by_xpath("/html/body/section[2]/ul/li[4]/a").click()

def delete_pharmacist():
	driver.find_element_by_xpath("/html/body/section[2]/ul/li[4]/a").click()
	time.sleep(3)
	driver.find_element_by_xpath("/html/body/section[3]/div/div[2]/div/div/table/tbody/tr[2]/td[6]/a/i").click()
	driver.find_element_by_xpath("/html/body/section[2]/ul/li[4]/a").click()


def add_salesman():
	driver.find_element_by_xpath("/html/body/section[2]/ul/li[5]/a").click()

	driver.find_element_by_xpath("/html/body/section[3]/div/div[3]/div/div/form/div/div[1]/label/input").send_keys("Manan")
	driver.find_element_by_xpath("/html/body/section[3]/div/div[3]/div/div/form/div/div[2]/label/input").send_keys("Patel")
	driver.find_element_by_xpath("/html/body/section[3]/div/div[3]/div/div/form/div/div[3]/label/input").send_keys("manan@salesman.com")
	driver.find_element_by_xpath("/html/body/section[3]/div/div[3]/div/div/form/div/div[4]/label/input").send_keys("88888")
	driver.find_element_by_xpath("/html/body/section[3]/div/div[3]/div/div/form/div/div[5]/label/input").send_keys("987")
	time.sleep(5)
	driver.find_element_by_xpath("/html/body/section[3]/div/div[3]/div/div/form/div/div[6]/input").click()
	time.sleep(5)
	driver.find_element_by_xpath("/html/body/section[2]/ul/li[6]/a").click()

def edit_salesman():
	driver.find_element_by_xpath("/html/body/section[2]/ul/li[6]/a").click()
	driver.find_element_by_xpath("/html/body/section[3]/div/div[3]/div/div/table/tbody/tr[2]/td[5]/a/i").click()
	
	driver.find_element_by_xpath("/html/body/section[3]/div/div[3]/div/div/form/div/div[2]/label/input").clear()
	driver.find_element_by_xpath("/html/body/section[3]/div/div[3]/div/div/form/div/div[2]/label/input").send_keys("Shah")

	time.sleep(3)
	driver.find_element_by_xpath("/html/body/section[3]/div/div[3]/div/div/form/div/div[5]/input").click()
	
	time.sleep(3)
	driver.find_element_by_xpath("/html/body/section[2]/ul/li[6]/a").click()

def delete_salesman():
	driver.find_element_by_xpath("/html/body/section[2]/ul/li[6]/a").click()
	time.sleep(3)
	driver.find_element_by_xpath("/html/body/section[3]/div/div[3]/div/div/table/tbody/tr[2]/td[6]/a/i").click()
	driver.find_element_by_xpath("/html/body/section[2]/ul/li[6]/a").click()

def logout():
	time.sleep(4)
	driver.find_element_by_xpath("/html/body/section[1]/div[2]/div/button").click()
	time.sleep(2)
	driver.find_element_by_xpath("/html/body/section[1]/div[2]/div/div/a[3]").click()


# Login
open_login()
time.sleep(7)
login_manager()
time.sleep(2)

# Pharmacist Crud
add_pharmacist()
time.sleep(2)
edit_pharmacist()
time.sleep(2)
delete_pharmacist()
time.sleep(2)

# Salesman Crud
add_salesman()
time.sleep(2)
edit_salesman()
time.sleep(2)
delete_salesman()
time.sleep(2)

# Logout
logout()
time.sleep(10)
driver.quit()