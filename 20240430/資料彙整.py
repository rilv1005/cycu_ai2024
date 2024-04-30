import pandas as pd
import glob

# 找到所有的 CSV 檔案
csv_files = glob.glob('/workspaces/cycu_ai2024/20240430/TDCS_M03A/*.csv')

# 讀取並過濾所有的 CSV 檔案
dfs = []
for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    # 過濾出第二欄位是以 '01' 開頭的資料
    filtered_df = df[df.iloc[:, 1].str.startswith('01')]
    dfs.append(filtered_df)

# 合併所有的 DataFrame
combined_df = pd.concat(dfs, ignore_index=True)

# 儲存合併後的 DataFrame 為新的 CSV 檔案
combined_df.to_csv('/workspaces/cycu_ai2024/20240430/TDCS_M03A/TDCS_M03A.csv', index=False)

