import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36'
}

for start_num in range(0,250,25):
    url = f'https://movie.douban.com/top250?start={start_num}&filter='
    response = requests.get(url,headers=headers)
    html = response.text
    soup = BeautifulSoup(html,'html.parser')
    all_titles = soup.find_all('span',attrs={'class':'title'})
    for title in all_titles:
        title_string = title.string
        if '/' not in title_string:
            print(title.string)