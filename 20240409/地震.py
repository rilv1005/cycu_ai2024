#C:\Users\User\Desktop\0904\cycu_ai2024\20240409\地震活動彙整.csvimport pandas as pd
import pandas as pd
import folium

# 讀取 csv 文件
df = pd.read_csv(r'C:\Users\User\Desktop\0904\cycu_ai2024\20240409\地震活動彙整.csv', encoding='big5')

# 提取經度和緯度
locations = df[['緯度', '經度']]

# 創建一個地圖
m = folium.Map(location=[23.5, 121], zoom_start=7)

# 在地圖上繪製數據點
for index, row in df.iterrows():
    # 創建一個 Popup
    popup = folium.Popup(f"緯度: {row['緯度']}, 經度: {row['經度']}", max_width=300)
    
    # 將 Popup 添加到 Marker 中
    folium.Marker([row['緯度'], row['經度']], popup=popup).add_to(m)

# 保存地圖
m.save('earthquake_map.html')