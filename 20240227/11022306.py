print("Hello world")

import feedparser

def fetch_rss_titles(url):
    feed = feedparser.parse(url)
    titles = [entry.title for entry in feed.entries]
    return titles

url = "https://news.pts.org.tw/xml/newsfeed.xml"
titles = fetch_rss_titles(url)
for title in titles:
    print(title)
    #檢查檔案的標題是否包含 台中 如果有的話儲存成 excel可讀取的格式
    #方在 使用者的桌面上
    #檔案名稱為 11022306.csv
    


