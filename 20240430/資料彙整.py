#/workspaces/cycu_ai2024/20240430/TDCS_M03A
import pandas as pd
import glob

# 找到所有的 CSV 檔案
csv_files = glob.glob('/workspaces/cycu_ai2024/20240430/TDCS_M05A/*.csv')

# 讀取並過濾所有的 CSV 檔案
dfs = []
for csv_file in csv_files:
    df = pd.read_csv(csv_file, header=None)
    # 過濾出第二欄位（索引為 1）是以 '01' 開頭的資料
    filtered_df = df[df[1].str.startswith('01')]
    # 過濾出第四欄位（索引為 3）是 '31' 的資料
    filtered_df = filtered_df[filtered_df[3] == 31]
    dfs.append(filtered_df)

# 合併所有的 DataFrame
combined_df = pd.concat(dfs, ignore_index=True)

# 將合併後的 DataFrame 儲存為新的 CSV 檔案
combined_df.to_csv('/workspaces/cycu_ai2024/20240430/TDCS_M05A_combined.csv', index=False, header=False)

# 找到所有的 CSV 檔案
csv_files = glob.glob('/workspaces/cycu_ai2024/20240430/TDCS_M03A/*.csv')

# 讀取並過濾所有的 CSV 檔案
dfs = []
for csv_file in csv_files:
    df = pd.read_csv(csv_file, header=None)
    # 過濾出第二欄位（索引為 1）是以 '01' 開頭的資料
    filtered_df = df[df[1].str.startswith('01')]
    dfs.append(filtered_df)

# 合併所有的 DataFrame
combined_df = pd.concat(dfs, ignore_index=True)

# 將合併後的 DataFrame 儲存為新的 CSV 檔案
combined_df.to_csv('/workspaces/cycu_ai2024/20240430/TDCS_M03A_combined.csv', index=False, header=False)
