import requests
from bs4 import BeautifulSoup

url = 1
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

basliklar = soup.find_all("h1")
for baslik in basliklar:
  print(baslik.text)