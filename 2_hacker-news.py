import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36'
}

response = requests.get("https://space.bilibili.com/282739748/upload/video",headers=headers)
html_content = response.text
soup = BeautifulSoup(html_content,'html.parser')
titlelines = soup.find_all('div',attrs={'class':'bili-video-card__title'})
for titleline in titlelines:
    hyperlink_tag = titleline.find('a')
    title = hyperlink_tag.text
    link = hyperlink_tag['href']
    print(f"Title: {title}\nLink: {link}\n")
