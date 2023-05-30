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
# opt.add_argument("headless")         # this will not open browser
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

def login_admin():
	driver.find_element_by_xpath("/html/body/div/div[1]/div/div/div[2]/div/div/form/fieldset/div[1]/input").send_keys("deep@admin.com")
	driver.find_element_by_xpath("/html/body/div/div[1]/div/div/div[2]/div/div/form/fieldset/div[2]/input").send_keys("d1")
	driver.find_element_by_xpath("/html/body/div/div[1]/div/div/div[2]/div/div/form/fieldset/div[3]/select/option[1]").click()
	time.sleep(5)
	driver.find_element_by_xpath("/html/body/div/div[1]/div/div/div[2]/div/div/form/fieldset/input").click()

def add_manager():
	driver.find_element_by_xpath("/html/body/section[2]/ul/li[2]/a").click()

	driver.find_element_by_xpath("/html/body/section[3]/div/div[1]/div/div/form/div/div[1]/label/input").send_keys("Rohit")
	driver.find_element_by_xpath("/html/body/section[3]/div/div[1]/div/div/form/div/div[2]/label/input").send_keys("Sharma")
	driver.find_element_by_xpath("/html/body/section[3]/div/div[1]/div/div/form/div/div[3]/label/input").send_keys("rohit@manager.com")
	driver.find_element_by_xpath("/html/body/section[3]/div/div[1]/div/div/form/div/div[4]/label/input").send_keys("9823232732")
	driver.find_element_by_xpath("/html/body/section[3]/div/div[1]/div/div/form/div/div[5]/label/input").send_keys("111")
	time.sleep(5)
	driver.find_element_by_xpath("/html/body/section[3]/div/div[1]/div/div/form/div/div[6]/input").click()
	time.sleep(5)
	driver.find_element_by_xpath("/html/body/section[2]/ul/li[3]/a").click()

def edit_manager():
	driver.find_element_by_xpath("/html/body/section[2]/ul/li[3]/a").click()
	driver.find_element_by_xpath("/html/body/section[3]/div/div[1]/div/div/table/tbody/tr[2]/td[5]/a/i").click()
	
	driver.find_element_by_xpath("/html/body/section[3]/div/div[1]/div/div/form/div/div[4]/label/input").clear()
	driver.find_element_by_xpath("/html/body/section[3]/div/div[1]/div/div/form/div/div[4]/label/input").send_keys("99999")

	time.sleep(3)
	driver.find_element_by_xpath("/html/body/section[3]/div/div[1]/div/div/form/div/div[5]/input").click()
	
	time.sleep(3)
	driver.find_element_by_xpath("/html/body/section[2]/ul/li[3]/a").click()

def delete_manager():
	driver.find_element_by_xpath("/html/body/section[2]/ul/li[3]/a").click()
	time.sleep(3)
	driver.find_element_by_xpath("/html/body/section[3]/div/div[1]/div/div/table/tbody/tr[2]/td[6]/a/i").click()
	driver.find_element_by_xpath("/html/body/section[2]/ul/li[3]/a").click()


def add_pharmacist():
	driver.find_element_by_xpath("/html/body/section[2]/ul/li[4]/a").click()

	driver.find_element_by_xpath("/html/body/section[3]/div/div[2]/div/div/form/div/div[1]/label/input").send_keys("Virat")
	driver.find_element_by_xpath("/html/body/section[3]/div/div[2]/div/div/form/div/div[2]/label/input").send_keys("Kohli")
	driver.find_element_by_xpath("/html/body/section[3]/div/div[2]/div/div/form/div/div[3]/label/input").send_keys("virat@pharmacist.com")
	driver.find_element_by_xpath("/html/body/section[3]/div/div[2]/div/div/form/div/div[4]/label/input").send_keys("8923237")
	driver.find_element_by_xpath("/html/body/section[3]/div/div[2]/div/div/form/div/div[5]/label/input").send_keys("222")
	time.sleep(5)
	driver.find_element_by_xpath("/html/body/section[3]/div/div[2]/div/div/form/div/div[6]/input").click()
	time.sleep(5)
	driver.find_element_by_xpath("/html/body/section[2]/ul/li[5]/a").click()

def edit_pharmacist():
	driver.find_element_by_xpath("/html/body/section[2]/ul/li[5]/a").click()
	driver.find_element_by_xpath("/html/body/section[3]/div/div[2]/div/div/table/tbody/tr[2]/td[5]/a/i").click()
	
	driver.find_element_by_xpath("/html/body/section[3]/div/div[2]/div/div/form/div/div[3]/label/input").clear()
	driver.find_element_by_xpath("/html/body/section[3]/div/div[2]/div/div/form/div/div[3]/label/input").send_keys("viratkohli@pharmacist.com")

	time.sleep(3)
	driver.find_element_by_xpath("/html/body/section[3]/div/div[2]/div/div/form/div/div[5]/input").click()
	
	time.sleep(3)
	driver.find_element_by_xpath("/html/body/section[2]/ul/li[5]/a").click()

def delete_pharmacist():
	driver.find_element_by_xpath("/html/body/section[2]/ul/li[5]/a").click()
	time.sleep(3)
	driver.find_element_by_xpath("/html/body/section[3]/div/div[2]/div/div/table/tbody/tr[2]/td[6]/a/i").click()
	driver.find_element_by_xpath("/html/body/section[2]/ul/li[5]/a").click()


def add_salesman():
	driver.find_element_by_xpath("/html/body/section[2]/ul/li[6]/a").click()

	driver.find_element_by_xpath("/html/body/section[3]/div/div[3]/div/div/form/div/div[1]/label/input").send_keys("Mohammad")
	driver.find_element_by_xpath("/html/body/section[3]/div/div[3]/div/div/form/div/div[2]/label/input").send_keys("Sami")
	driver.find_element_by_xpath("/html/body/section[3]/div/div[3]/div/div/form/div/div[3]/label/input").send_keys("mohammad@salesman.com")
	driver.find_element_by_xpath("/html/body/section[3]/div/div[3]/div/div/form/div/div[4]/label/input").send_keys("987654")
	driver.find_element_by_xpath("/html/body/section[3]/div/div[3]/div/div/form/div/div[5]/label/input").send_keys("666")
	time.sleep(5)
	driver.find_element_by_xpath("/html/body/section[3]/div/div[3]/div/div/form/div/div[6]/input").click()
	time.sleep(5)
	driver.find_element_by_xpath("/html/body/section[2]/ul/li[7]/a").click()

def edit_salesman():
	driver.find_element_by_xpath("/html/body/section[2]/ul/li[7]/a").click()
	driver.find_element_by_xpath("/html/body/section[3]/div/div[3]/div/div/table/tbody/tr[2]/td[5]/a/i").click()
	
	driver.find_element_by_xpath("/html/body/section[3]/div/div[3]/div/div/form/div/div[2]/label/input").clear()
	driver.find_element_by_xpath("/html/body/section[3]/div/div[3]/div/div/form/div/div[2]/label/input").send_keys("Shami")

	time.sleep(3)
	driver.find_element_by_xpath("/html/body/section[3]/div/div[3]/div/div/form/div/div[5]/input").click()
	
	time.sleep(3)
	driver.find_element_by_xpath("/html/body/section[2]/ul/li[7]/a").click()

def delete_salesman():
	driver.find_element_by_xpath("/html/body/section[2]/ul/li[7]/a").click()
	time.sleep(3)
	driver.find_element_by_xpath("/html/body/section[3]/div/div[3]/div/div/table/tbody/tr[2]/td[6]/a/i").click()
	driver.find_element_by_xpath("/html/body/section[2]/ul/li[7]/a").click()

def logout():
	time.sleep(4)
	driver.find_element_by_xpath("/html/body/section[1]/div[2]/div/button").click()
	time.sleep(2)
	driver.find_element_by_xpath("/html/body/section[1]/div[2]/div/div/a[3]").click()


# Login
open_login()
time.sleep(7)
login_admin()
time.sleep(3)

# Manager Crud
add_manager()
time.sleep(2)
edit_manager()
time.sleep(2)
delete_manager()
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