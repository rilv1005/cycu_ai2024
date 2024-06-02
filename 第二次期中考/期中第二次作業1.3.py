#C:\Users\User\Desktop\homework\Github\cycu_ai2024\M05A
#檔案格式 TDCS_M05A_20240101_000000.CSV

import pandas as pd
import glob
import os

# 創建資料夾
if not os.path.exists('C:\\Users\\User\\Desktop\\homework\\Github\\cycu_ai2024\\M05A_Combined'):
    os.mkdir('C:\\Users\\User\\Desktop\\homework\\Github\\cycu_ai2024\\M05A_Combined')

# 指定欄位名稱
column_names = ['TimeInterval', 'GantryFrom', 'GantryTo', 'VehicleType', 'SpaceMeanSpeed', '交通量']

# 處理每一天的資料
for day in pd.date_range(start='2024-01-01', end='2024-04-30'):
    # 將日期轉換為特定的格式
    day_str = day.strftime('%Y%m%d')

    # 找到所有符合 'TDCS_M05A_{day_str}_*' 模式的檔案
    files = glob.glob(f'M05A\\TDCS_M05A_{day_str}_*')

    # 讀取每個檔案，並將它們存儲在一個列表中
    dataframes = [pd.read_csv(file, skipinitialspace=True, header=None, names=column_names) for file in files]

    # 將所有的 DataFrame 合併成一個
    combined_df = pd.concat(dataframes)

    # 保留 VehicleType=31 的 "SpaceMeanSpeed"
    speed_df = combined_df[combined_df['VehicleType'] == 31][['TimeInterval', 'GantryFrom', 'GantryTo', 'SpaceMeanSpeed', '交通量']]
    speed_df.rename(columns={'交通量': '交通量(小客車 31)'}, inplace=True)

    # 處理其他 VehicleType 的資料
    for vehicle_type in [32, 41, 42, 5]:
        vehicle_df = combined_df[combined_df['VehicleType'] == vehicle_type][['TimeInterval', 'GantryFrom', 'GantryTo', '交通量']]
        vehicle_df.rename(columns={'交通量': f'交通量({vehicle_type})'}, inplace=True)
        speed_df = pd.merge(speed_df, vehicle_df, on=['TimeInterval', 'GantryFrom', 'GantryTo'], how='outer')

    # 將合併後的 DataFrame 寫入新的 CSV 檔案
    speed_df.to_csv(f'C:\\Users\\User\\Desktop\\homework\\Github\\cycu_ai2024\\M05A_Combined\\M05A_{day_str}.csv', index=False)

