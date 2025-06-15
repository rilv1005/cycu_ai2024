

import numpy as np
import pandas as pd
import os
import glob

# 獲取所有的 CSV 檔案
csv_files = glob.glob('M05A_Combined\*.csv')

# 檢查"M05A_feature"資料夾是否存在，如果不存在，則創建它
if not os.path.exists('M05A_feature'):
    os.makedirs('M05A_feature')

# 對每個 CSV 檔案執行相同的操作
for csv_file in csv_files:
    # 讀取 CSV 檔案
    df = pd.read_csv(csv_file)

    #時間區間的處理
    # 將"TimeInterval"欄位分割成日期和時間
    df[['Date', 'Time']] = df['TimeInterval'].str.split(' ', expand=True)
    #將TimeInterval欄位改成只有日期
    df['TimeInterval'] = df['Date']

    #日期和節日的處理
    # 將 'Date' 欄位的資料類型轉換為 datetime
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    # 將 'Date' 欄位的資料轉換為星期幾，並將結果存儲在新的 'WeekDay' 欄位中
    df['WeekDay'] = (df['Date'].dt.dayofweek + 1) % 7

    #篩選VehicleType欄位符合31資料
    df = df.loc[df['VehicleType'] == 31]

    #第二次期中考\政府行政機關辦公日曆表.csv
    # 讀取 CSV 檔案
    holidays = pd.read_csv('第二次期中考\政府行政機關辦公日曆表.csv', encoding='big5')

    # 將 'Date' 欄位的資料類型轉換為 datetime
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    holidays['date'] = pd.to_datetime(holidays['date'], errors='coerce')

    # 創建一個新的 DataFrame，其中包含 'date' 和 'isHoliday' 兩個欄位
    holiday_dates = holidays[holidays['isHoliday'] == '是']['date']

    # 創建一個新的 'HoliDay' 欄位，如果 'Date' 欄位中的日期是假日，則 'HoliDay' 為 1，否則為 0
    df['HoliDay'] = df['Date'].apply(lambda x: 1 if x in holiday_dates.values else 0)
    #刪除Date欄位
    df = df.drop(columns=['Date'])

    #GantryFrom和GantryTo的處理
    # 篩選 GantryFrom 欄位符合特定條件的資料
    df = df.loc[df['GantryFrom'].isin(['01F0584N', '01F0633N', '01F0578S', '01F0633S'])]

    #排序欄位TimeInterval,,Time,WeekDay,HoliDay,GantryFrom,GantryTo,VehicleType,SpaceMeanSpeed,交通量
    df = df[['TimeInterval', 'Time', 'WeekDay', 'HoliDay', 'GantryFrom', 'GantryTo', 'VehicleType', 'SpaceMeanSpeed', '交通量']]

    # 獲取檔案名稱和副檔名
    file_name, file_extension = os.path.splitext(os.path.basename(csv_file))
    
    # 建立新的檔案名稱
    new_file_name = f"{file_name}_feature{file_extension}"
    
    # 儲存處理後的 DataFrame 到新的 CSV 檔案
    df.to_csv(f'M05A_feature/{new_file_name}', index=False)
    print(f"已處理 {new_file_name}")


