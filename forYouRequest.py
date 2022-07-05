from urllib import response
import requests

# https://www.tiktok.com/foryou?is_copy_url=1&is_from_webapp=v1

response = requests.get('https://www.tiktok.com/foryou?is_copy_url=1&is_from_webapp=v1')

if response.status_code == 200:
    print("Status code 200")
else:
    print("oops\n" + response.status_code)
    exit

jsonResponse = response.json() # fixme
for key, value in jsonResponse.items():
    print(key, ":", value)