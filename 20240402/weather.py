import feedparser
import requests
from bs4 import BeautifulSoup

def get_city_names(rss_url):
    feed = feedparser.parse(rss_url)
    city_names = [entry.title for entry in feed.entries]
    return city_names

def get_rss_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True) if 'rss' in a['href']]
    return links

url = "https://www.cwa.gov.tw/V8/C/S/eservice/rss.html"
rss_links = get_rss_links(url)
for link in rss_links:
    
    rss_url = "https://www.cwa.gov.tw"+link
    city_names = get_city_names(rss_url)
    for name in city_names:
        print(name)
    print("====================================")