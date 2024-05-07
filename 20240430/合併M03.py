import glob
import pandas as pd

# 定義欄位名稱
column_names = ['time', 'gate', 'direct', 'type', 'counts']

# 找到所有的 CSV 檔案
csv_files = glob.glob('/workspaces/cycu_ai2024/20240430/TDCS_M03A_*.csv')

# 讀取所有的 CSV 檔案，並指定欄位名稱和只讀取前五個欄位
dfs = [pd.read_csv(csv_file, names=column_names, usecols=range(5)) for csv_file in csv_files]

# 合併所有的 DataFrame
combined_df = pd.concat(dfs, ignore_index=True)

# 將合併後的 DataFrame 儲存為新的 CSV 檔案
combined_df.to_csv('/workspaces/cycu_ai2024/20240430/TDCS_M03A_combined.csv', index=False)