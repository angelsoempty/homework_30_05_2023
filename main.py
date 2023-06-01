import requests
from bs4 import BeautifulSoup
def get_html(url):
    response = requests.get(url)
    return response.text
url = "http://example.com"
html = get_html(url)
soup = BeautifulSoup(html, 'html.parser')
h2_elements = soup.find_all('h2')
for h2 in h2_elements:
    print(h2.get_text())
