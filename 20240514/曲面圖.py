#/workspaces/cycu_ai2024/20240514/TDCS_M03A_20240429_180500_new.csv

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 讀取 csv 文件
df = pd.read_csv('/workspaces/cycu_ai2024/20240514/TDCS_M03A_20240429_180500_new.csv')

# 清理數據：刪除 'milage' 或 'counts' 欄位中包含 NaN 的行
df = df[df['milage'].notna() & df['counts'].notna()]

# 分割 DataFrame
df_N = df[df['direct'] == 'N']
df_S = df[df['direct'] == 'S']

# 刪除 'milage' 欄位的數據中的重複值並排序
df_N = df_N.drop_duplicates(subset='milage').sort_values(by='milage')
df_S = df_S.drop_duplicates(subset='milage').sort_values(by='milage')

# 提取 'milage' 和 'counts' 欄位的數據並轉換為 NumPy 陣列
x_N = np.array(df_N['milage'])
y_N = np.array(df_N['counts'])
x_S = np.array(df_S['milage'])
y_S = np.array(df_S['counts'])

# 繪製 'N' 方向的曲線和點
plt.figure()
plt.plot(x_N, y_N, label='Aggregate Curve N')  # 繪製聚合曲線
plt.scatter(x_N, y_N, color='red')  # 繪製點
plt.legend()
plt.savefig('Aggregate_Curve_N.png')  # 儲存圖表
plt.show()

# 繪製 'S' 方向的曲線和點
plt.figure()
plt.plot(x_S, y_S, label='Aggregate Curve S')  # 繪製聚合曲線
plt.scatter(x_S, y_S, color='red')  # 繪製點
plt.legend()
plt.savefig('Aggregate_Curve_S.png')  # 儲存圖表
plt.show()