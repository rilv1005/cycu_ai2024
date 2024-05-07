#/workspaces/cycu_ai2024/20240430/TDCS_M03A_combined-1.csv
#/workspaces/cycu_ai2024/20240430/TDCS_M05A_combined.csv

import pandas as pd

# 讀取 csv 檔案
df1 = pd.read_csv('/workspaces/cycu_ai2024/20240430/TDCS_M03A_combined-1.csv')
df2 = pd.read_csv('/workspaces/cycu_ai2024/20240430/TDCS_M05A_combined.csv')

# 從 df2 中選取第五欄位的資料
df2_selected = df2.iloc[:, 4]

# 確保 df1 和 df2 的行數相同
if len(df1) == len(df2):
    # 將 df2 的第五欄位的資料添加到 df1 的第五欄位
    df1.iloc[:, 4] = df2_selected
else:
    print("Error: The number of rows in the two dataframes are not equal.")

# 儲存合併後的資料
df1.to_csv('merged.csv', index=False)