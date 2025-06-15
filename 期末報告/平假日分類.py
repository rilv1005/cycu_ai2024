#M05A_feature
import pandas as pd
import os

# 設定資料夾路徑
folder_path = r'C:\Users\User\Desktop\homework\Github\cycu_ai2024\M05A_feature'

# 獲取資料夾內所有 CSV 檔案的路徑
csv_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.csv')]

# 初始化兩個空的 DataFrame
weekday_df = pd.DataFrame()
holiday_df = pd.DataFrame()

# 遍歷所有 CSV 檔案
for file in csv_files:
    # 讀取 CSV 檔案
    df = pd.read_csv(file)
    
    # 判斷第一筆資料的 Holiday 欄位
    if df.iloc[0]['HoliDay'] == 0:
        # 匯入平日的 DataFrame
        weekday_df = pd.concat([weekday_df, df], ignore_index=True)
    elif df.iloc[0]['HoliDay'] == 1:
        # 匯入假日的 DataFrame
        holiday_df = pd.concat([holiday_df, df], ignore_index=True)

# 儲存平日資料到 CSV 檔案
weekday_df.to_csv('5月平日.csv', index=False)

# 儲存假日資料到 CSV 檔案
holiday_df.to_csv('五月假日.csv', index=False)