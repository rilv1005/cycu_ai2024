#C:\Users\User\Desktop\homework\Github\cycu_ai2024\20240430\TDCS_M05A_combined.csv
#'time', 'location', 'location2', 'type', 'velocity', 'counts'

import pandas as pd

#M05a
# 指定欄位名稱
column_names = ['time', 'location', 'location2', 'type', 'velocity', 'counts']

# 讀取 CSV 檔案，並新增欄位名稱
df = pd.read_csv('C:\\Users\\User\\Desktop\\homework\\Github\\cycu_ai2024\\20240430\\TDCS_M05A_combined.csv', names=column_names)

# 儲存 DataFrame 為新的 CSV 檔案
df.to_csv('C:\\Users\\User\\Desktop\\homework\\Github\\cycu_ai2024\\20240430\\TDCS_M05A_combined_new.csv', index=False)

#M03A
# 指定欄位名稱
column_names = ['time', 'location', 'direction', 'type', 'counts']

# 讀取 CSV 檔案，並新增欄位名稱
df = pd.read_csv('C:\\Users\\User\\Desktop\\homework\\Github\\cycu_ai2024\\20240430\\TDCS_M03A_combined-3.csv', names=column_names)

# 儲存 DataFrame 為新的 CSV 檔案
df.to_csv('C:\\Users\\User\\Desktop\\homework\\Github\\cycu_ai2024\\20240430\\TDCS_M03A_combined_new.csv', index=False)