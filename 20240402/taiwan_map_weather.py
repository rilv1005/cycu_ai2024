import feedparser
import requests
from bs4 import BeautifulSoup
import re
import geopandas as gpd
import pandas as pd

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
city_temperature = {}
for link in rss_links:
    rss_url = "https://www.cwa.gov.tw" + link
    temp_dict = get_city_temperature(rss_url)  # 獲取每個城市的溫度
    city_temperature.update(temp_dict)  # 更新字典

        

import geopandas as gpd
import matplotlib.pyplot as plt

# 讀取 GIS 檔案
taiwan = gpd.read_file('/workspaces/cycu_ai2024/20240402/county/COUNTY_MOI_1090820.shp')


# 將字典轉換為 DataFrame
temp_df = pd.DataFrame(list(city_temperature.items()), columns=['C_Name', 'Temperature'])

# 將溫度資料與 GeoDataFrame 合併
taiwan = taiwan.merge(temp_df, left_on='COUNTYNAME', right_on='C_Name')

# 繪製地圖
fig, ax = plt.subplots(1, 1,figsize=(10,10))
taiwan.plot(column='Temperature', ax=ax, legend=True)
plt.xlim(119,122)
plt.ylim(21.5,25.5)
#加上數字
for x, y, label in zip(taiwan.geometry.centroid.x, taiwan.geometry.centroid.y, taiwan['Temperature']):
    ax.text(x, y, label, fontsize=8, ha='center')
#加上標題
plt.title('11022306 HSU-CHING NI')

plt.show()
#save to png file
plt.savefig('20240402/taiwan_map_weather.png')