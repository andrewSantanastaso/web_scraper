from bs4 import BeautifulSoup
import requests

url='https://www.cnn.com'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, 'html.parser')
titles = soup.find_all('h2')
for title in titles:
    print(title)