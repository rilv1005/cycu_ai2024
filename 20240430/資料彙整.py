import pandas as pd
import glob

csv_files = glob.glob('/path/to/TDCS_M03A/*.csv')
dfs = []
for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    df = df[df.iloc[:, 1].str.startswith('01')]  # 假設第二欄位是在索引 1 的位置
    dfs.append(df)
combined_df = pd.concat(dfs, ignore_index=True)

combined_df.to_csv('/workspaces/cycu_ai2024/20240430/TDCS_M03A', index=False)