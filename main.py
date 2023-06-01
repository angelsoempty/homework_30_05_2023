import requests
from bs4 import BeautifulSoup
def get_html(url):
    response = requests.get(url)
    return response.text

url = "http://example.com"
html = get_html(url)
soup = BeautifulSoup(html, 'html.parser')
h1_element = soup.find('h1')
if h1_element:
    print("Заголовок <h1>:")
    print(f"Текст: {h1_element.text}")
    print(f"Атрибути: {h1_element.attrs}")
else:
    print("Заголовок <h1> не знайдений на сторінці.")