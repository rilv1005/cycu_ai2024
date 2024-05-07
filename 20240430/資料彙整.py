#/workspaces/cycu_ai2024/20240430/TDCS_M03A
import pandas as pd
import glob

# 找到所有的 CSV 檔案
#csv_files = glob.glob('/workspaces/cycu_ai2024/20240430/TDCS_M03A_*.csv')
#對這個csv /workspaces/cycu_ai2024/20240430/TDCS_M03A_combined.csv 做篩選
csv_files = glob.glob('/workspaces/cycu_ai2024/20240430/TDCS_M03A_combined.csv')

# 讀取並過濾所有的 CSV 檔案
dfs = []
for csv_file in csv_files:
    df = pd.read_csv(csv_file, header=None)
    # 過濾出 gate 欄位（索引為 1）以 '01' 開頭的資料
    filtered_df = df[df[1].str.startswith('01')]

    dfs.append(filtered_df)

# 合併所有的 DataFrame
combined_df = pd.concat(dfs, ignore_index=True)

# 將合併後的 DataFrame 儲存為新的 CSV 檔案
combined_df.to_csv('/workspaces/cycu_ai2024/20240430/TDCS_M03A_combined-2.csv', index=False, header=False)

#將type欄位的資料轉換為字串
combined_df[3] = combined_df[3].astype(str)
#過濾出 type 欄位（索引為 3）是31的資料
filtered_df = combined_df[combined_df[3] == '31']
#將過濾後的資料儲存為新的 CSV 檔案
filtered_df.to_csv('/workspaces/cycu_ai2024/20240430/TDCS_M03A_combined-3.csv', index=False, header=False)




