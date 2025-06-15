#國科會\ADRL 斜撐1mm 實驗數據.xlsx

import pandas as pd
import matplotlib.pyplot as plt

# 讀取 Excel 檔案
file_path = r"C:\Users\User\Desktop\homework\國科會\仿生結構\結案報告\實驗數據\六種力與位移圖.xlsx"
df = pd.read_excel(file_path)

# 每50筆數據抓取一次
df_reduced = df.iloc[::1, :]
df_reduced1 = df.iloc[::1, :]


# 繪製 XY 散布圖
plt.figure(figsize=(10, 6))

# 繪製第一條曲線
plt.plot(df_reduced.iloc[:, 2], df_reduced.iloc[:, 1], label=df.columns[0], color='#FF0000', linestyle='-', linewidth=1.75)

# 繪製第二條曲線
plt.plot(df_reduced.iloc[:, 5], df_reduced.iloc[:, 4], label=df.columns[3], color='#FFBC00', linestyle='-', linewidth=1.75)

# 繪製第三條曲線
plt.plot(df_reduced.iloc[:, 8], df_reduced.iloc[:, 7], label=df.columns[6], color='#00A651', linestyle='-', linewidth=1.75)

# 繪製第四條曲線
plt.plot(df_reduced1.iloc[:, 11], df_reduced1.iloc[:, 10], label=df.columns[9], color='#2D89CB', linestyle='-', linewidth=1.75)

# 繪製第五條曲線
plt.plot(df_reduced1.iloc[:, 14], df_reduced1.iloc[:, 13], label=df.columns[12], color='#A1A1A1', linestyle='-', linewidth=1.75)

# 繪製第六條曲線
plt.plot(df_reduced1.iloc[:, 17], df_reduced1.iloc[:, 16], label=df.columns[15], color='#FF9A03', linestyle='-', linewidth=1.75)

# 設定圖表標題和標籤
plt.xlabel('Displacement (mm)', fontsize=20, fontname='Arial', fontweight='bold')
plt.ylabel('Compressive load (kN)', fontsize=20, fontname='Arial', fontweight='bold')
plt.legend(fontsize=12, frameon=False)

# 設定 X、Y 軸
plt.xticks(fontsize=15, fontname='Arial')
plt.yticks(fontsize=15, fontname='Arial')
plt.gca().spines['bottom'].set_color('black')
plt.gca().spines['bottom'].set_linewidth(1.5)
plt.gca().spines['left'].set_color('black')
plt.gca().spines['left'].set_linewidth(1.5)
plt.gca().spines['top'].set_color('black')
plt.gca().spines['top'].set_linewidth(1.5)
plt.gca().spines['right'].set_color('black')
plt.gca().spines['right'].set_linewidth(1.5)

# 設定 X、Y 軸切齊0 且都以整數展示
plt.gca().xaxis.set_major_locator(plt.MultipleLocator(2))  # X 軸以 1 為間距標示
plt.gca().yaxis.set_major_locator(plt.MaxNLocator(integer=True))
plt.gca().set_xlim(left=0,right=18)  
plt.gca().set_ylim(bottom=0)

# 設定尺寸格線在內側
plt.gca().tick_params(axis='both', direction='in')

# 顯示圖表
plt.show()