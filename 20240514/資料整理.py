#/workspaces/cycu_ai2024/20240514/TDCS_M03A_20240429_180500.csv

import pandas as pd

# 讀取 csv 文件
df = pd.read_csv('/workspaces/cycu_ai2024/20240514/TDCS_M03A_20240429_180500.csv')

# 將 'gate' 欄位的資料分割成三個新的欄位
df[['road', 'milage', '南北']] = df['gate'].str.extract('(\d{2}F)(\d{4})([NS])')

# 刪除 'gate' 和 '南北' 欄位
df = df.drop(columns=['gate', '南北'])

# 重新排序欄位
df = df.reindex(columns=['time', 'road', 'milage', 'direct', 'type', 'counts'])

# 將 DataFrame 寫入新的 csv 文件
df.to_csv('/workspaces/cycu_ai2024/20240514/TDCS_M03A_20240429_180500_new.csv', index=False)
