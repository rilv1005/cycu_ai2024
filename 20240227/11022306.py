print("Hello world")

import feedparser
import csv
def fetch_rss_titles_and_contents(url):
    feed = feedparser.parse(url)
    entries = [(entry.title, entry.summary) for entry in feed.entries]
    return entries

url = "https://news.pts.org.tw/xml/newsfeed.xml"
entries = fetch_rss_titles_and_contents(url)
for title, content in entries:
    print(f"Title: {title}\nContent: {content}\n")
    #列出台中市的新聞
    if "台中市" in content:
        print(f"Title: {title}\nContent: {content}\n")
        with open("11022306.csv", "a", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([title, content])
            

    
    



    


