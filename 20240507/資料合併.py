#/workspaces/cycu_ai2024/20240430/TDCS_M03A_combined-1.csv
#/workspaces/cycu_ai2024/20240430/TDCS_M05A_combined.csv

import pandas as pd

# 讀取 csv 檔案
df1 = pd.read_csv('/workspaces/cycu_ai2024/20240430/TDCS_M03A_combined-1.csv')
df2 = pd.read_csv('/workspaces/cycu_ai2024/20240430/TDCS_M05A_combined.csv')

# 合併兩個 DataFrame
merged_df = pd.concat([df1, df2])

# 移除重複的行
merged_df = merged_df.drop_duplicates()

# 儲存合併後的資料
merged_df.to_csv('merged.csv', index=False)