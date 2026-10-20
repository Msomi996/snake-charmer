import requests
from bs4 import BeautifulSoup
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_South_Africa'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')
print(soup)
soup.find('table', class_='wikitable sortable jquery-tablesorter')[1]

#<table class="wikitable sortable jquery-tablesorter" id="mwGQ">

#</tbody><tfoot><tr class="mw-empty-elt" id="mwAe0"></tr></tfoot></table>