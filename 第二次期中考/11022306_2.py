#第二次期中考\M05A_Combined\M05A_20240101.csv

import numpy as np
import pandas as pd
import os
import glob

# 獲取所有的 CSV 檔案
csv_files = glob.glob('第二次期中考\M05A_Combined\*.csv')

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

    # 刪除原本的"TimeInterval"欄位
    df = df.drop(columns=['TimeInterval'])

    # 將'Date'和'Time'欄位移動到DataFrame的最前面
    df = df[['Date', 'Time'] + [col for col in df.columns if col not in ['Date', 'Time']]]

    # 將"Time"欄位的時間轉換為時間對象
    df['Time'] = pd.to_datetime(df['Time'])

    # 將時間轉換為分鐘數，然後除以5並取整數部分，得到時間段
    df['Time'] = df['Time'].dt.hour * 60 + df['Time'].dt.minute
    df['Time'] = df['Time'] // 5

    #日期和節日的處理
    # 將 'Date' 欄位的資料類型轉換為 datetime
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    # 將 'Date' 欄位的資料轉換為星期幾，並將結果存儲在新的 'WeekDay' 欄位中
    df['WeekDay'] = (df['Date'].dt.dayofweek + 1) % 7

    # 獲取 'Date' 欄位的位置
    idx = df.columns.get_loc('Date')

    # 建立新的欄位順序
    new_order = df.columns[:idx+1].tolist() + ['WeekDay'] + df.columns[idx+1:-1].tolist()

    # 使用新的欄位順序重新排列 DataFrame
    df = df[new_order]
    #第二次期中考\政府行政機關辦公日曆表.csv
    # 讀取 CSV 檔案
    holidays = pd.read_csv('第二次期中考\政府行政機關辦公日曆表.csv', encoding='big5')

    # 將 'Date' 欄位的資料類型轉換為 datetime
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    holidays['date'] = pd.to_datetime(holidays['date'], errors='coerce')

    # 創建一個新的 DataFrame，其中包含 'date' 和 'isHoliday' 兩個欄位
    holiday_dates = holidays[holidays['isHoliday'] == '是']['date']

    # 創建一個新的 'HoliDay' 欄位，如果 'Date' 欄位中的日期的下一天是假日，則 'HoliDay' 為 -1，否則為 0
    df['HoliDay'] = df['Date'].apply(lambda x: -1 if (x + pd.Timedelta(days=1)) in holiday_dates.values else 0)

    # 如果 'Date' 欄位中的日期是假日，則 'HoliDay' 為 1
    df.loc[df['Date'].isin(holiday_dates), 'HoliDay'] = 1

    # 獲取 'WeekDay' 欄位的位置
    idx = df.columns.get_loc('WeekDay')

    # 建立新的欄位順序
    new_order = df.columns[:idx+1].tolist() + ['HoliDay'] + df.columns[idx+1:-1].tolist()

    # 使用新的欄位順序重新排列 DataFrame
    df = df[new_order]


    #GantryFrom和GantryTo的處理

    # 將 'GantryFrom' 欄位的資料分割成三個新的欄位
    df['WayIDFrom'] = df['GantryFrom'].str.slice(0, 3)
    df['WayMilageFrom'] = pd.to_numeric(df['GantryFrom'].str.slice(3, 7), errors='coerce')
    df['WayDirectionFrom'] = df['GantryFrom'].str.slice(7, 8)

    #GantryFrom和GantryTo的處理
    # 獲取 'GantryFrom' 欄位的位置
    idx = df.columns.get_loc('GantryFrom')

    # 將新的欄位移動到 'GantryFrom' 欄位之後
    df = df[df.columns[:idx+1].tolist() + ['WayIDFrom', 'WayMilageFrom', 'WayDirectionFrom'] + df.columns[idx+1:-3].tolist()]

    # 刪除原本的 'GantryFrom' 欄位
    df = df.drop(columns=['GantryFrom'])

    # 將 'GantryTo' 欄位的資料分割成三個新的欄位
    df['WayIDTo'] = df['GantryTo'].str.slice(0, 3)
    df['WayMilageTo'] = pd.to_numeric(df['GantryTo'].str.slice(3, 7), errors='coerce')
    df['WayDirectionTo'] = df['GantryTo'].str.slice(7, 8)

    # 獲取 'GantryTo' 欄位的位置
    idx = df.columns.get_loc('GantryTo')

    # 將新的欄位移動到 'GantryTo' 欄位之後
    df = df[df.columns[:idx+1].tolist() + ['WayIDTo', 'WayMilageTo', 'WayDirectionTo'] + df.columns[idx+1:-3].tolist()]

    # 刪除原本的 'GantryTo' 欄位
    df = df.drop(columns=['GantryTo'])

    #速度分級處理
    # 定義分級的邊界
    bins = [-np.inf, 0, 20, 40, 60, 80, np.inf]

    # 使用 pd.cut 進行分級
    df['SpeedClass'] = pd.cut(df['SpaceMeanSpeed'], bins=bins, labels=[0, 1, 2, 3, 4, 5])

    # 將 'SpeedClass' 欄位的資料類型轉換為整數
    df['SpeedClass'] = df['SpeedClass'].astype(int)

    # 獲取 'SpaceMeanSpeed' 欄位的位置
    idx = df.columns.get_loc('SpaceMeanSpeed')

    # 建立新的欄位順序
    new_order = df.columns[:idx+1].tolist() + ['SpeedClass'] + df.columns[idx+1:-1].tolist()

    # 使用新的欄位順序重新排列 DataFrame
    df = df[new_order]

    # 獲取檔案名稱和副檔名
    file_name, file_extension = os.path.splitext(os.path.basename(csv_file))
    
    # 建立新的檔案名稱
    new_file_name = f"{file_name}_feature{file_extension}"
    
    # 儲存處理後的 DataFrame 到新的 CSV 檔案
    df.to_csv(f'M05A_feature/{new_file_name}', index=False)
    print(f"已處理 {new_file_name}")


