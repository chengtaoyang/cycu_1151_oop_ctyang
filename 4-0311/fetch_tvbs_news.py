# 這是楊承道老師（ctyang@rosa.systems）為中原大學
# 「物件導向程式設計」課程所準備的教材範例。

# 基礎語法：匯入套件呼叫網頁請求，以物件方法解析 HTML 並逐筆處理結果。
# 擷取 TVBS 新聞首頁的新聞標題與連結。
# 透過 BeautifulSoup 解析網頁內容後逐項顯示。
import requests
from bs4 import BeautifulSoup

def fetch_tvbs_news():
    url = 'https://news.tvbs.com.tw/'
    response = requests.get(url)
    response.encoding = 'utf-8'
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        news_items = soup.find_all('div', class_='news_list')
        
        for item in news_items:
            title = item.find('h2').text.strip()
            link = item.find('a')['href']
            print(f'Title: {title}')
            print(f'Link: {link}')
            print('---')
    else:
        print('Failed to retrieve the news')

if __name__ == "__main__":
    fetch_tvbs_news()