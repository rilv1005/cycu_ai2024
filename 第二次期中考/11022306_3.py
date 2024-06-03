#繪圖 HTML 檔，表現 2024 年 4 月 29 日的交通量與車速隨時間與高速公路里程的變化
#第二次期中考\M05A_feature\M05A_20240429_feature.csv

import pandas as pd
import folium
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
import numpy as np
from folium.plugins import TimestampedGeoJson
import os
from datetime import datetime, timedelta
import matplotlib.cm as cm
import geopandas as gpd


# 讀取 CSV 文件
df = pd.read_csv('M05A_feature\M05A_20240429_feature.csv')

# 將指定的欄位值相加
df['交通量'] = df[['交通量(小客車 31)','交通量(32)','交通量(41)','交通量(42)','交通量(5)']].sum(axis=1)
# 如果你想要刪除原來的欄位，可以使用以下的程式碼：
df = df.drop(columns=['交通量(小客車 31)','交通量(32)','交通量(41)','交通量(42)','交通量(5)'])

# 從每個 DataFrame 中選擇你需要的欄位
selected_columns_df = df[['TimeInterval','Time', 'GantryFrom','GantryTo','SpeedClass','交通量']] 

# 寫入新的 CSV 文件
selected_columns_df.to_csv('20240429.csv', index=False)


#製作地圖 門架在時間與速度和交通量的關係
#20240429.csv
#第二次期中考\國道計費門架座標及里程牌價表1130327.csv
import folium
from folium.plugins import TimestampedGeoJson
from branca.element import Template, MacroElement

# 讀取數據
gantry_data = pd.read_csv('第二次期中考\國道計費門架座標及里程牌價表1130327.csv')
traffic_data = pd.read_csv('20240429.csv')
# 創建地圖
m = folium.Map(location=[23.5, 121], zoom_start=8)

# 合併數據
merged_data = pd.merge(traffic_data, gantry_data, how='left', left_on='GantryFrom', right_on='設定收費區代碼')

# 將數據按照時間排序
merged_data.sort_values('Time', inplace=True)

# 創建TimestampedGeoJson數據
data = {
    'type': 'FeatureCollection',
    'features': []
}
gantry_coordinates = pd.read_csv('第二次期中考\國道計費門架座標及里程牌價表1130327.csv')
# 創建一個字典，其中包含每個門架代碼的經緯度
gantry_data = {}
for index, row in gantry_coordinates.iterrows():
    gantry_code = row['設定收費區代碼']
    lat = row['緯度']
    lon = row['經度']
    gantry_data[gantry_code] = (lat, lon)

colors = {0: 'white', 1: 'purple', 2: 'red', 3: 'orange', 4: 'yellow', 5: 'green'}


# 獲取經緯度數據
lons = merged_data['經度'].tolist()
lats = merged_data['緯度'].tolist()

# 創建一個包含所有點的經緯度坐標的列表
coordinates = list(zip(lons, lats))

from datetime import datetime, timedelta

# 將 NewTime 列轉換為 ISO 8601 格式的日期時間字符串
start_time = datetime(2024, 4, 29)
merged_data['Time'] = [start_time + timedelta(minutes=5*i) for i in merged_data['Time']]
merged_data['Time'] = merged_data['Time'].dt.strftime('%Y-%m-%dT%H:%M:%S')

times = merged_data['Time'].tolist()
speed_classes = merged_data['SpeedClass'].astype(int).tolist()
weights = (merged_data['交通量'] / 1000).tolist()


for i in range(len(merged_data)):
    feature = {
        'type': 'Feature',
        'geometry': {
            'type': 'Point',  
            'coordinates': [merged_data.iloc[i]['經度'], merged_data.iloc[i]['緯度']]
        },
        'properties': {
            'times': [times[i], times[i]],
            'speed': speed_classes[i],
            'style': {'color': colors[speed_classes[i]], 'weight': float(weights[i])},
            'icon': 'circle',
            'iconstyle': {
                'fillColor': colors[speed_classes[i]],
                'fillOpacity': 0.8,
                'stroke': 'true',
                'radius': float(weights[i])
            }
        }
    }
    data['features'].append(feature)

TimestampedGeoJson(
    data,
    period='PT5M',
    add_last_point=True,
    auto_play=False,
    loop=False,
    loop_button=True,
    date_options='YYYY/MM/DD HH:mm:ss',
    time_slider_drag_update=True
).add_to(m)

template = """
{% macro html(this, kwargs) %}
<div style="
    position: fixed; 
    top: 5px;
    left: 5px;
    width: 120px;
    height: 150px;
    z-index:9999;
    font-size:14px;
    background-color: #F0EFEF;
    opacity: 0.7;
    border-radius: 2px;
    ">
    <p><strong>速度顏色分類表</strong></p>
    <p><div style="display:inline-block;width:10px;height:10px;background-color:#000000"></div> 0</p>
    <p><div style="display:inline-block;width:10px;height:10px;background-color:#800080"></div> 1~20</p>
    <p><div style="display:inline-block;width:10px;height:10px;background-color:#ff0000"></div> 21~40</p>
    <p><div style="display:inline-block;width:10px;height:10px;background-color:#ffa500"></div> 41~60</p>
    <p><div style="display:inline-block;width:10px;height:10px;background-color:#ffff00"></div> 61~80</p>
    <p><div style="display:inline-block;width:10px;height:10px;background-color:#008000"></div> 80以上</p>
</div>
{% endmacro %}
"""

macro = MacroElement()
macro._template = Template(template)

m.get_root().add_child(macro)

m.save('map.html')
