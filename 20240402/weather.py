import feedparser
import requests
from bs4 import BeautifulSoup
import re

def get_city_temperature(rss_url):
    feed = feedparser.parse(rss_url)
    city_temperature = {}
    for entry in feed.entries:
        match = re.search(r'^(.{2,3}[縣市]).+溫度: (\d+ ~ \d+)', entry.title)
        if match:
            city = match.group(1)
            temperature = match.group(2)
            city_temperature[city] = temperature
    return city_temperature

def get_rss_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True) if 'rss' in a['href']]
    return links

url = "https://www.cwa.gov.tw/V8/C/S/eservice/rss.html"
rss_links = get_rss_links(url)
for link in rss_links:
    rss_url = "https://www.cwa.gov.tw"+link
    city_temperature = get_city_temperature(rss_url)
    for city, temperature in city_temperature.items():
        print(f"縣市名稱: {city}, 溫度: {temperature}")