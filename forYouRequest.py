from urllib import response
import requests
from bs4 import BeautifulSoup

# https://www.tiktok.com/foryou?is_copy_url=1&is_from_webapp=v1
def runMe():
	response = requests.get('https://www.tiktok.com/foryou?is_copy_url=1&is_from_webapp=v1')

	if response.status_code == 200:
	    print("Status code 200")
	else:
	    print("oops\n" + response.status_code)
	    exit

	print(response.text)
	soup = BeautifulSoup(response.text, 'html.parser')
	print(soup.prettify())