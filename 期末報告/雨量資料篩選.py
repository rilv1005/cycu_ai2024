#C:\Users\User\Desktop\homework\Github\cycu_ai2024\May_rain
import pandas as pd
import os

# 設定資料夾路徑
folder_path = r'C:\Users\User\Desktop\homework\Github\cycu_ai2024\May_rain'

# 獲取資料夾內所有 CSV 檔案的路徑
csv_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.csv')]

# 初始化一個空的 DataFrame 來儲存篩選後的資料
filtered_df = pd.DataFrame()

# 遍歷所有 CSV 檔案
for file in csv_files:
    # 讀取 CSV 檔案
    df = pd.read_csv(file)
    
    # 篩選特定 StationId 的資料
    df_filtered = df[df['StationId'].isin(['A0C410', 'A2C560', 'C0C700'])]
    
    # 將篩選後的資料加入到 filtered_df
    filtered_df = pd.concat([filtered_df, df_filtered], ignore_index=True)
    print("File", file, "has been 完成")

#刪除StationName,CountyName,TownName,StationLatitude,StationLongitude,StationAltitude
filtered_df = filtered_df.drop(['StationName', 'CountyName', 'TownName', 'StationLatitude', 'StationLongitude', 'StationAltitude'], axis=1)
#刪除Past1hr,Past10Min,Past3hr,Past6hr,Past12hr,Past24hr,Past2days,Past3days
filtered_df = filtered_df.drop(['Past1hr', 'Past10Min', 'Past3hr', 'Past6hr', 'Past12hr', 'Past24hr', 'Past2days', 'Past3days'], axis=1)

# 儲存篩選後的資料到新的 CSV 檔案
filtered_df.to_csv('May_filtered.csv', index=False)


# 讀取 CSV 檔案
df = pd.read_csv('May_filtered.csv')

# 假設日期時間格式為 '年-月-日 時:分:秒'
df['DateTime'] = pd.to_datetime(df['DateTime'], format='%Y-%m-%d %H:%M:%S', errors='coerce')

# 將 DateTime 欄位轉換為僅日期格式
df['DateTime'] = df['DateTime'].dt.date

# 對相同日期的 NOW 值進行加總
df_sum = df.groupby('DateTime')['NOW'].sum().reset_index()

# 存檔
df_sum.to_csv('May_filtered_rain.csv', index=False)