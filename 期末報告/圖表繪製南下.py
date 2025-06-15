#C:\Users\User\Desktop\homework\Github\cycu_ai2024\5月平日_含雨量更新.csv
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates

# 讀取資料
df = pd.read_csv('期末報告\\5月假日_含雨量更新_彙整.csv')

# 篩選GantryFrom為01F0584N和01F0633N的資料
filtered_df = df[df['GantryFrom'].isin(['01F0578S', '01F0633S'])]

# 設定matplotlib支援中文和負號
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False


# 繪製圖表
plt.figure(figsize=(10, 6))

# GantryFrom為01F0584N Rains為0
df_01F0584N_0 = filtered_df[(filtered_df['GantryFrom'] == '01F0633S') & (filtered_df['Rains'] == 0)]
plt.plot(df_01F0584N_0['Time'], df_01F0584N_0['交通量']/4, color='orange', label='中壢平鎮南下沒雨')

# GantryFrom為01F0584N Rains為1
df_01F0584N_1 = filtered_df[(filtered_df['GantryFrom'] == '01F0633S') & (filtered_df['Rains'] == 1)]
plt.plot(df_01F0584N_1['Time'], df_01F0584N_1['交通量']/4, color='blue', label='中壢平鎮南下下雨')

# GantryFrom為01F0633N Rains為0
df_01F0633N_0 = filtered_df[(filtered_df['GantryFrom'] == '01F0578S') & (filtered_df['Rains'] == 0)]
plt.plot(df_01F0633N_0['Time'], df_01F0633N_0['交通量']/4, color='red', label='內壢中壢南下沒雨')

# GantryFrom為01F0633N Rains為1
df_01F0633N_1 = filtered_df[(filtered_df['GantryFrom'] == '01F0578S') & (filtered_df['Rains'] == 1)]
plt.plot(df_01F0633N_1['Time'], df_01F0633N_1['交通量']/4, color='green', label='內壢中壢南下下雨')

# 設定圖表標題和軸標籤
plt.title('五月假日南下')
plt.xlabel('時間')
plt.ylabel('交通量')
plt.xticks(range(0, 288, 12))
plt.xticks(rotation=45)
plt.legend(title='方向')
plt.legend(loc='upper right')
plt.tight_layout()
#plt.show()
# Save the plot as a file
plt.savefig('5月假日南下.png')

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates

# 讀取資料
df = pd.read_csv('期末報告\\5月平日_含雨量更新_彙整.csv')

# 篩選GantryFrom為01F0584N和01F0633N的資料
filtered_df = df[df['GantryFrom'].isin(['01F0578S', '01F0633S'])]

# 設定matplotlib支援中文和負號
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False


# 繪製圖表
plt.figure(figsize=(10, 6))

# GantryFrom為01F0584N Rains為0
df_01F0584N_0 = filtered_df[(filtered_df['GantryFrom'] == '01F0633S') & (filtered_df['Rains'] == 0)]
plt.plot(df_01F0584N_0['Time'], df_01F0584N_0['交通量']/8, color='orange', label='中壢平鎮南下沒雨')

# GantryFrom為01F0584N Rains為1
df_01F0584N_1 = filtered_df[(filtered_df['GantryFrom'] == '01F0633S') & (filtered_df['Rains'] == 1)]
plt.plot(df_01F0584N_1['Time'], df_01F0584N_1['交通量']/15, color='blue', label='中壢平鎮南下下雨')

# GantryFrom為01F0633N Rains為0
df_01F0633N_0 = filtered_df[(filtered_df['GantryFrom'] == '01F0578S') & (filtered_df['Rains'] == 0)]
plt.plot(df_01F0633N_0['Time'], df_01F0633N_0['交通量']/8, color='red', label='內壢中壢南下沒雨')

# GantryFrom為01F0633N Rains為1
df_01F0633N_1 = filtered_df[(filtered_df['GantryFrom'] == '01F0578S') & (filtered_df['Rains'] == 1)]
plt.plot(df_01F0633N_1['Time'], df_01F0633N_1['交通量']/15, color='green', label='內壢中壢南下下雨')

# 設定圖表標題和軸標籤
plt.title('五月平日南下')
plt.xlabel('時間')
plt.ylabel('交通量')
plt.xticks(range(0, 288, 12))
plt.xticks(rotation=45)
plt.legend(title='方向')
plt.legend(loc='upper right')
plt.tight_layout()
#plt.show()
# Save the plot as a file
plt.savefig('5月平日南下.png')
