#https://scweb.cwa.gov.tw/zh-tw/earthquake/data/
import requests
from bs4 import BeautifulSoup
import folium
from datetime import datetime

# 爬取網站上的數據
url = 'https://scweb.cwa.gov.tw/zh-tw/earthquake/data/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 找到所有的地震資訊
earthquakes = soup.find_all('tr')[1:]  # 第一個 tr 是表頭，所以我們從第二個 tr 開始

# 創建一個地圖
m = folium.Map(location=[23.5, 121], zoom_start=7)

# 在地圖上繪製地震資訊
for earthquake in earthquakes:
    tds = earthquake.find_all('td')
    if len(tds) < 6:
        continue  # 如果這個 tr 標籤中沒有至少6個 td 標籤，則跳過這個地震

    # 獲取地震的時間、緯度、經度和規模
    time = datetime.strptime(tds[0].text, '%Y-%m-%d %H:%M:%S')
    lat = float(tds[4].text)
    lon = float(tds[5].text)
    magnitude = float(tds[1].text)

    # 根據規模設置圓形的大小和顏色
    radius = magnitude * 2
    color = 'red' if magnitude >= 5 else 'blue'

    # 在地圖上繪製一個圓形
    folium.CircleMarker([lat, lon], radius=radius, color=color, fill=True, fill_color=color).add_to(m)

# 保存地圖
m.save('earthquake4_map.html')