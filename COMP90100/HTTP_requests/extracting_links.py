import requests # Library for sending HTTP requests
from bs4 import BeautifulSoup # Library for parsing and navigating HTML documents

url = 'https://www.python.org'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

links = soup.find_all('a')

for link in links:
    href = link.get('href')

    if not href:
        continue
    if not href.startswith("http"):
        continue
    if "docs" in href or "learn" in href:
        print(href)