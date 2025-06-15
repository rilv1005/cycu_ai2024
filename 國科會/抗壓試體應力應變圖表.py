#國科會\ADRL 斜撐1mm 實驗數據.xlsx

import pandas as pd
import matplotlib.pyplot as plt

# 讀取 Excel 檔案
file_path = r"C:\Users\User\Desktop\homework\國科會\仿生結構\實驗excel\25.04.28 compress intertwine.xlsx"
df = pd.read_excel(file_path)

# 每50筆數據抓取一次
df_reduced = df.iloc[::1, :]
df_reduced_sim = df.iloc[::30, :]

# 篩選 X 軸值小於等於 15 的數據
#df_reduced = df_reduced[df_reduced.iloc[:, 1] <= 15]

# 對 y 軸的值除以 630，對 x 軸的值除以 82
# 對 y 軸的值除以 549.6，對 x 軸的值除以 84
# 對 y 軸的值除以 900，對 x 軸的值除以 30
df_reduced.iloc[:, 1] = df_reduced.iloc[:, 1] 
df_reduced.iloc[:, 2] = df_reduced.iloc[:, 2] 
df_reduced.iloc[:, 4] = df_reduced.iloc[:, 4] 
df_reduced.iloc[:, 5] = df_reduced.iloc[:, 5] 
df_reduced.iloc[:, 7] = df_reduced.iloc[:, 7] 
df_reduced.iloc[:, 8] = df_reduced.iloc[:, 8] 
df_reduced_sim.iloc[:, 10] = df_reduced_sim.iloc[:, 10] / 900
df_reduced_sim.iloc[:, 11] = df_reduced_sim.iloc[:, 11] / 30
df_reduced_sim.iloc[:, 13] = df_reduced_sim.iloc[:, 13] / 900
df_reduced_sim.iloc[:, 14] = df_reduced_sim.iloc[:, 14] / 30
df_reduced_sim.iloc[:, 16] = df_reduced_sim.iloc[:, 16] / 900
df_reduced_sim.iloc[:, 17] = df_reduced_sim.iloc[:, 17] / 30

# 繪製 XY 散布圖
plt.figure(figsize=(10, 6))

# 繪製第一條曲線
plt.plot(df_reduced.iloc[:, 2], df_reduced.iloc[:, 1], label=df.columns[0], color='#0070C0', linestyle=':', linewidth=1.75)

# 繪製第二條曲線
plt.plot(df_reduced.iloc[:, 5], df_reduced.iloc[:, 4], label=df.columns[3], color='#0070C0', linestyle='--', linewidth=1.75)

# 繪製第三條曲線
plt.plot(df_reduced.iloc[:, 8], df_reduced.iloc[:, 7], label=df.columns[6], color='#0070C0', linestyle='-.', linewidth=1.75)

# 繪製第四條曲線
plt.plot(df_reduced_sim.iloc[:, 11], df_reduced_sim.iloc[:, 10], label=df.columns[9], color='#78206E', linestyle='-', linewidth=1.75)

# 繪製第五條曲線
plt.plot(df_reduced_sim.iloc[:, 14], df_reduced_sim.iloc[:, 13], label=df.columns[12], color='#78206E', linestyle=':', linewidth=1.75)

# 繪製第六條曲線
plt.plot(df_reduced_sim.iloc[:, 17], df_reduced_sim.iloc[:, 16], label=df.columns[15], color='#78206E', linestyle='-.', linewidth=2.25)

# 設定圖表標題和標籤
plt.xlabel('Strain', fontsize=14, fontname='Arial', fontweight='bold')
plt.ylabel('Stress (N/mm²)', fontsize=14, fontname='Arial', fontweight='bold')
plt.legend(fontsize=12, frameon=False)

# 設定 X、Y 軸
plt.xticks(fontsize=12, fontname='Arial')
plt.yticks(fontsize=12, fontname='Arial')
plt.gca().spines['bottom'].set_color('black')
plt.gca().spines['bottom'].set_linewidth(1.5)
plt.gca().spines['left'].set_color('black')
plt.gca().spines['left'].set_linewidth(1.5)
plt.gca().spines['top'].set_color('black')
plt.gca().spines['top'].set_linewidth(1.5)
plt.gca().spines['right'].set_color('black')
plt.gca().spines['right'].set_linewidth(1.5)

# 設定 X、Y 軸切齊0 且都以整數展示
plt.gca().xaxis.set_major_locator(plt.MultipleLocator(0.025))  # X 軸以 0.025 為間距標示
plt.gca().yaxis.set_major_locator(plt.MaxNLocator(integer=True))
plt.gca().set_xlim(left=0, right=0.2)  
plt.gca().set_ylim(bottom=0)

# 設定尺寸格線在內側
plt.gca().tick_params(axis='both', direction='in')

# 顯示圖表
plt.show()