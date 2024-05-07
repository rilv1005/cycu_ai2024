#/workspaces/cycu_ai2024/20240430/TDCS_M03A_combined-1.csv
#/workspaces/cycu_ai2024/20240430/TDCS_M05A_combined.csv

import pandas as pd

# 讀取 csv 檔案
df1 = pd.read_csv('/workspaces/cycu_ai2024/20240430/TDCS_M03A_combined-1.csv')
df2 = pd.read_csv('/workspaces/cycu_ai2024/20240430/TDCS_M05A_combined.csv')

# 從 df2 中選取第五欄位的資料
df2_selected = df2.iloc[:, 4]

# 將 df2 的第五欄位加到 df1
df1['New_Column'] = df2_selected

# 儲存合併後的資料
df1.to_csv('merged.csv', index=False)