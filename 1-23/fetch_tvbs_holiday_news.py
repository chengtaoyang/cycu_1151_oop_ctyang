# 這是楊承道老師（ctyang@rosa.systems）為中原大學
# 「物件導向程式設計」課程所準備的教材範例。

# 基礎語法：以函式呼叫取得網頁、用例外處理錯誤，並以迴圈和條件篩選標題。
# 從 TVBS 新聞首頁擷取標題含「連假」的新聞。
# 顯示符合條件新聞的標題與完整網址。
from urllib.parse import urljoin
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup


def fetch_tvbs_news():
    url = 'https://news.tvbs.com.tw/'
    request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    try:
        with urlopen(request, timeout=10) as response:
            if response.status != 200:
                print(f'Failed to retrieve the news (HTTP {response.status})')
                return
            html = response.read()
    except Exception as error:
        print(f'Failed to retrieve the news: {error}')
        return

    soup = BeautifulSoup(html, 'html.parser')
    news_items = soup.find_all('h2')
    found_news = 0

    for item in news_items:
        link_tag = item.find_parent('a', href=True)
        title = item.get_text(strip=True)
        if link_tag is None or not title:
            continue
        if '連假' not in title:
            continue

        found_news += 1
        link = urljoin(url, link_tag['href'])
        print(f'Title: {title}')
        print(f'Link: {link}')
        print('---')

    if found_news == 0:
        print('No typhoon-related news items found')

if __name__ == '__main__':
    fetch_tvbs_news()