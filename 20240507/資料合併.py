#/workspaces/cycu_ai2024/20240430/TDCS_M03A_combined-3.csv
#/workspaces/cycu_ai2024/20240430/TDCS_M05A_combined.csv
# 讀取 'TDCS_M03A_combined-3.csv' 檔案
import pandas as pd

# 讀取第一個 CSV 檔案，使用完整的檔案路徑
df1 = pd.read_csv('/workspaces/cycu_ai2024/20240430/TDCS_M03A_combined-3.csv', header=None)

# 讀取第二個 CSV 檔案，使用完整的檔案路徑
df2 = pd.read_csv('/workspaces/cycu_ai2024/20240430/TDCS_M05A_combined.csv', header=None)

# 根據第一和第二欄位合併兩個 DataFrame
merged_df = pd.merge(df1, df2[[0, 1, 4, 5]], on=[0, 1], how='left')

# 移除含有空值的欄位
merged_df = merged_df.dropna(axis=1)

# 將合併後的 DataFrame 儲存為新的 CSV 檔案
merged_df.to_csv('/workspaces/cycu_ai2024/20240430/TDCS_M03A_M05A_combined.csv', index=False, header=False)