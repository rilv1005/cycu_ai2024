#C:\Users\User\Desktop\homework\Github\cycu_ai2024\5月平日.csv

import pandas as pd

# 讀取 CSV 檔案
df = pd.read_csv('C:\\Users\\User\\Desktop\\homework\\Github\\cycu_ai2024\\5月假日.csv')

# 在 DataFrame 中添加一個名為 'Rains' 的新欄位，初始值設為 NaN
df['Rains'] = pd.NA
#將


# 將修改後的 DataFrame 保存回 CSV 檔案，不包含索引
df.to_csv('C:\\Users\\User\\Desktop\\homework\\Github\\cycu_ai2024\\5月平日.csv', index=False)

#C:\Users\User\Desktop\homework\Github\cycu_ai2024\May_filtered_rain_Meg.csv
import pandas as pd

# 讀取 CSV 檔案
df_rain = pd.read_csv('May_filtered_rain_Meg.csv')
df_traffic = pd.read_csv('5月假日.csv')

# 將 DateTime 和 TimeInterval 欄位轉換為日期格式
df_rain['Date'] = pd.to_datetime(df_rain['DateTime']).dt.date
df_traffic['Date'] = pd.to_datetime(df_traffic['TimeInterval']).dt.date

# 初始化 Rains 欄位
df_traffic['Rains'] = 0

# 遍歷交通量數據
for index, row in df_traffic.iterrows():
    # 尋找相同日期的雨量數據
    rain_data = df_rain[df_rain['Date'] == row['Date']]
    if not rain_data.empty:
        # 檢查 NOW 欄位的值，並更新 Rains 欄位
        df_traffic.at[index, 'Rains'] = 1 if any(rain_data['NOW'] != 0) else 0

#刪除Date欄位
df_traffic = df_traffic.drop(columns=['Date'])

# 保存更新後的數據到新的 CSV 檔案
df_traffic.to_csv('5月假日_含雨量更新.csv', index=False)

#C:\Users\User\Desktop\homework\Github\cycu_ai2024\5月平日.csv

import pandas as pd

# 讀取 CSV 檔案
df = pd.read_csv('C:\\Users\\User\\Desktop\\homework\\Github\\cycu_ai2024\\5月平日.csv')

# 在 DataFrame 中添加一個名為 'Rains' 的新欄位，初始值設為 NaN
df['Rains'] = pd.NA
#將


# 將修改後的 DataFrame 保存回 CSV 檔案，不包含索引
df.to_csv('C:\\Users\\User\\Desktop\\homework\\Github\\cycu_ai2024\\5月平日.csv', index=False)

#C:\Users\User\Desktop\homework\Github\cycu_ai2024\May_filtered_rain_Meg.csv
import pandas as pd

# 讀取 CSV 檔案
df_rain = pd.read_csv('May_filtered_rain_Meg.csv')
df_traffic = pd.read_csv('5月平日.csv')

# 將 DateTime 和 TimeInterval 欄位轉換為日期格式
df_rain['Date'] = pd.to_datetime(df_rain['DateTime']).dt.date
df_traffic['Date'] = pd.to_datetime(df_traffic['TimeInterval']).dt.date

# 初始化 Rains 欄位
df_traffic['Rains'] = 0

# 遍歷交通量數據
for index, row in df_traffic.iterrows():
    # 尋找相同日期的雨量數據
    rain_data = df_rain[df_rain['Date'] == row['Date']]
    if not rain_data.empty:
        # 檢查 NOW 欄位的值，並更新 Rains 欄位
        df_traffic.at[index, 'Rains'] = 1 if any(rain_data['NOW'] != 0) else 0

#刪除Date欄位
df_traffic = df_traffic.drop(columns=['Date'])

# 保存更新後的數據到新的 CSV 檔案
df_traffic.to_csv('5月平日_含雨量更新.csv', index=False)