import pandas as pd
import folium
from folium.plugins import TimestampedGeoJson
import json

# 讀取 csv 文件
df = pd.read_csv(r'C:\Users\User\Desktop\homework\Github\cycu_ai2024\20240409\地震活動彙整.csv', encoding='big5')

# 將數據轉換為 GeoJSON 格式
data = []
for index, row in df.iterrows():
    data.append({
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [row['經度'], row['緯度']],
        },
        'properties': {
            'time': row['地震時間'],
            'icon': 'marker',
            'popup': f"編號: {row['編號']}<br>地震時間: {row['地震時間']}<br>規模: {row['規模']}<br>緯度: {row['緯度']}<br>經度: {row['經度']}<br>位置: {row['位置']}",
        }
    })

# 創建一個地圖
m = folium.Map(location=[23.5, 121], zoom_start=7)

# 添加 TimestampedGeoJson
TimestampedGeoJson(
    {'type': 'FeatureCollection', 'features': data},
    period='PT1H',
    add_last_point=True,
).add_to(m)

# 保存地圖
m.save('earthquake_map2.html')