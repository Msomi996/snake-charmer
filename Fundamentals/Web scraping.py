import requests
from bs4 import BeautifulSoup
url = 'https://signupmerchant.capitecbank.co.za/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')
print(soup)
# we can also specify exactly what we are scraping for in a website.