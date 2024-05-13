#C:\Users\User\Desktop\homework\Github\cycu_ai2024\20240430\TDCS_M03A_combined_new.csv
#C:\Users\User\Desktop\homework\Github\cycu_ai2024\20240430\TDCS_M05A_combined_new.csv
#M03a欄位名稱: 'time', 'location', 'direction', 'type', 'counts'
#M05a欄位名稱: 'time', 'location', 'location2', 'type', 'velocity', 'counts'
#合併後欄位名稱: 'time', 'location', 'counts_M03A', 'type_M03A', 'velocity_M05A'


import pandas as pd

# 讀取 CSV 檔案
df1 = pd.read_csv(r'C:\Users\User\Desktop\homework\Github\cycu_ai2024\20240430\TDCS_M03A_combined_new.csv')
df2 = pd.read_csv(r'C:\Users\User\Desktop\homework\Github\cycu_ai2024\20240430\TDCS_M05A_combined_new.csv')

# 將時間欄位轉換為相同的格式
df1['time'] = pd.to_datetime(df1['time'])
df2['time'] = pd.to_datetime(df2['time'])

# 根據時間和地點欄位合併兩個 DataFrame
merged_df = pd.merge(df1, df2, on=['time', 'location'], suffixes=('_M03A', '_M05A'))

# 只保留特定的欄位
merged_df = merged_df[['time', 'location', 'type_M03A', 'counts_M03A', 'velocity']]

# 將合併後的 DataFrame 儲存為新的 CSV 檔案
merged_df.to_csv(r'C:\Users\User\Desktop\homework\Github\cycu_ai2024\20240430\TDCS_M03A_M05A_combined.csv', index=False)

