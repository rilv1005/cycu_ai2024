print("Hello world")

import feedparser

def fetch_rss_titles_and_contents(url):
    feed = feedparser.parse(url)
    entries = [(entry.title, entry.summary) for entry in feed.entries]
    return entries

url = "https://news.pts.org.tw/xml/newsfeed.xml"
entries = fetch_rss_titles_and_contents(url)
for title, content in entries:
    print(f"Title: {title}\nContent: {content}\n")
    #檢查檔案的標題是否包含 台灣 如果有的話儲存成 excel 可讀取的格式
    #放在 使用者的桌面上
    #檔案名稱為 11022306.csv
    if "台灣" in title:
        with open("C:/Users/11022306/Desktop/11022306.csv", "a", encoding="utf-8") as f:
            f.write(f"{title},{content}\n")
    
    



    


