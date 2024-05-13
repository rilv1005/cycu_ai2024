#/workspaces/cycu_ai2024/20240430/TDCS_M03A_combined-3.csv
#/workspaces/cycu_ai2024/20240430/TDCS_M05A_combined.csv
# 讀取 'TDCS_M03A_combined-3.csv' 檔案
import pandas as pd

# 讀取第一個 CSV 檔案，並指定欄位名稱
df1 = pd.read_csv('/workspaces/cycu_ai2024/20240430/TDCS_M03A_combined-3.csv', 
                  header=None, names=['time', 'location', 'direction', 'type', 'counts'])

# 讀取第二個 CSV 檔案，並指定欄位名稱
df2 = pd.read_csv('/workspaces/cycu_ai2024/20240430/TDCS_M05A_combined.csv', 
                  header=None, names=['time', 'location', 'location2', 'type', 'velocity', 'counts'])

# 根據時間和地點欄位合併兩個 DataFrame
merged_df = pd.merge(df1, df2[['time', 'location', 'velocity']], on=['time', 'location'], how='left')

# 將合併後的 DataFrame 儲存為新的 CSV 檔案
merged_df.to_csv('/workspaces/cycu_ai2024/20240507/TDCS_M03A_M05A_combined.csv', index=False)