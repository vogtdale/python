import requests
from bs4 import BeautifulSoup

base_url = 'https://www.msn.com/fr-fr?AR=4'
result = requests.get(base_url)
print(result.status_code)

src = result.content
soup = BeautifulSoup(src, "lxml")

urls = []
for uls  in soup.find_all("li"):
    a = uls.find('a')
    urls.append(a.attrs['href'])
print(urls)
    



