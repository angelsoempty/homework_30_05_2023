import requests
from bs4 import BeautifulSoup
def get_html(url):
    response = requests.get(url)
    return response.text
url = "http://example.com"
html = get_html(url)
soup = BeautifulSoup(html, 'html.parser')
table_elements = soup.find_all('table')
for table in table_elements:
    print(table)
    print()
