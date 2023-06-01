import requests
from bs4 import BeautifulSoup
def get_html(url):
    response = requests.get(url)
    return response.text
url = "http://example.com"
html = get_html(url)
soup = BeautifulSoup(html, 'html.parser')
example_elements = soup.find_all(class_="example-class")
for element in example_elements:
    print(element)
    print()
