import pandas as pd

# 讀取 CSV 檔案
df = pd.read_csv('/workspaces/cycu_ai2024/20240430/TDCS_M03A_combined.csv', sep='\t', header=None)

# 使用 groupby 並將第五欄位（索引為 4）的值轉換為列表
df_grouped = df.groupby([0, 1, 2])[4].apply(list).reset_index()

# 將列表轉換為單獨的欄位
df_grouped[[f'col_{i}' for i in range(1, len(df_grouped[4].str[0])+1)]] = pd.DataFrame(df_grouped[4].to_list(), index= df_grouped.index)

# 刪除原本的第五欄位（索引為 4）
df_grouped = df_grouped.drop(columns=[4])

# 將 DataFrame 儲存為新的 CSV 檔案
df_grouped.to_csv('/workspaces/cycu_ai2024/20240430/TDCS_M03A_combined_New.csv', index=False, header=False, sep='\t')