import pandas as pd
import folium
import math

# 讀取 csv 文件
df = pd.read_csv(r'C:\Users\User\Desktop\0904\cycu_ai2024\20240409\地震活動彙整.csv', encoding='big5')

# 創建一個地圖
m = folium.Map(location=[23.5, 121], zoom_start=7)

# 在地圖上繪製數據點
for index, row in df.iterrows():
    # 檢查 '緯度' 和 '經度' 是否為 NaN
    if math.isnan(row['緯度']) or math.isnan(row['經度']):
        continue

    # 創建一個 Popup
    popup = folium.Popup(f"編號: {row['編號']}<br>地震時間: {row['地震時間']}<br>規模: {row['規模']}<br>緯度: {row['緯度']}<br>經度: {row['經度']}<br>位置: {row['位置']}", max_width=300)
    
    # 根據規模設置圓形的大小和顏色
    radius = row['規模'] * 2
    color = 'red' if row['規模'] >= 5 else 'blue'
    
    # 將 Popup 和圓形添加到地圖上
    folium.CircleMarker([row['緯度'], row['經度']], radius=radius, color=color, fill=True, fill_color=color, popup=popup).add_to(m)

# 保存地圖
m.save('earthquake3_map.html')