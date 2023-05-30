import bs4
from bs4 import BeautifulSoup
import requests
import csv
from prettytable import PrettyTable

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.3'}

print("\nWelcome To Flipkart Scraping Tool\n")
scrap_page=input("Enter URL: ")

# scrap_page='https://www.flipkart.com/blackberry-key-2-black-64-gb/p/itm8135aea4c2c35?pid=MOBFESNVYY4FFHQY&lid=LSTMOBFESNVYY4FFHQYZ2HWBV&marketplace=FLIPKART&q=blackberry+mobiles&store=tyy%2F4io&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_na&fm=SEARCH&iid=cd7b2ef3-624d-4e6b-a3fc-512aa23ed9ab.MOBFESNVYY4FFHQY.SEARCH&ppt=hp&ppn=homepage&ssid=4998su4nsg0000001641374346704&qH=eff2982b2f6fc7da'

res = requests.get(scrap_page,headers=headers)

soup=BeautifulSoup(res.content,features="html5lib")

heading_specs = []
value_specs = []
heading_specs2 = []
value_specs2 = []
rev_specs=[]
stars_specs=[]

table = soup.find()

try:
	for title in table.findAll('span', attrs = {'class':'B_NuCI'}):
		title_mn=title.text
	
	print("\nModel: ",title_mn)

	heading_specs2.append("Model")
	value_specs2.append(title_mn)

	for price in table.findAll('div', attrs = {'class':'_30jeq3 _16Jk6d'}):
		price_mn=price.text
	
	print("\nPrice: ",price_mn)
	
	heading_specs2.append("Price")
	value_specs2.append(price_mn)
	
	for heading in table.findAll('td', attrs = {'class':'_1hKmbr col col-3-12'}):
		heading_specs.append(str(heading.text))

	
	
	tmp_vaar = 0
	tmp_val_lst=[]
	for value in table.findAll('li', attrs = {'class':'_21lJbe'}):
		if len(value.text) > 120:
			tmp_val_lst.append(tmp_vaar)
		value_specs.append(str(value.text))
		tmp_vaar+=1
	
	for rating in table.findAll('div', attrs = {'class':'_2d4LTz'}):
		rating_mn=rating.text

	print("\nRatings: ",rating_mn,"/ 5")

	for sta in table.findAll('div', attrs = {'class':'_1uJVNT'}):
		stars_specs.append(sta.text)

	print("\nReviews: ")

	for d in range(len(stars_specs)):
		print(str(5-d) + " Stars are given by " + str(stars_specs[d]) + " users")
	
except:
	print("Invalid URL or Some Error Occured, Re-run The Program Or Change The URL")
	exit()

heading_specs_tb = []
value_specs_tb = []

tmp_var = 0
for x in range(len(heading_specs)):
	flg = 0
	for y in tmp_val_lst:
		if tmp_var == y:
			flg = 1
	if flg == 0:
		heading_specs_tb.append(heading_specs[x])
		value_specs_tb.append(value_specs[x])

	tmp_var = tmp_var + 1

heading_specs = []
value_specs = []

heading_specs = heading_specs_tb
value_specs = value_specs_tb

heading_specs2=heading_specs2+heading_specs
value_specs2=value_specs2+value_specs

print("\nSpecifications: \n")

myTable = PrettyTable(["Specification", "Description"])
for x in range(len(heading_specs2)):
	myTable.add_row([heading_specs2[x], value_specs2[x]])
print(myTable)


csv_nm=title_mn+" Specifications.csv"


while True:

	sel=input("\nDo You Want to Make CSV of Specifications ? (y/n): ")
	
	if sel=="y" or sel=="Y":
		with open(str(csv_nm), 'w') as f:
			writer = csv.writer(f)
			writer.writerows(zip(heading_specs, value_specs))
		print("\nCSV File Created")
		print("\nThank You For Using This Tool !")
		exit(0)
	elif sel=="n" or sel=="N":
		print("\nThank You For Using This Tool !")
		exit(0)
	else:
		print("\nInvalid Option")
		continue