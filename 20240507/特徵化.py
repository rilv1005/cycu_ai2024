#C:\Users\User\Desktop\homework\Github\cycu_ai2024\20240430\TDCS_M03A_M05A_combined.csv

import pandas as pd
from sklearn.preprocessing import StandardScaler

# 讀取 CSV 檔案
df = pd.read_csv(r'C:\Users\User\Desktop\homework\Github\cycu_ai2024\20240507\TDCS_M03A_M05A_combined_processed.csv')


## 對時間欄位做標準化，把他切分為每個五分鐘(1-288)
df['time'] = pd.to_datetime(df['time'])
df['time'] = df['time'].dt.hour * 12 + df['time'].dt.minute / 5
df['time'] = df['time'].astype(int)
#建立一個時間區間 每五分鐘為一個區間
df['time_group'] = pd.cut(df['time'], bins=range(0, 289, 1), right=False, labels=range(0, 288))


# 將 'location' 欄位分解為 'road', 'mileage' 和 'direction'
df['mileage'] = df['location'].str.slice(3, 7).astype(int)
df['direction'] = df['location'].str.slice(-1)

# 將 'road' 和 'direction' 欄位轉換為數字
df['direction'] = df['direction'].map({'N': 0, 'S': 1})


# 刪除原始的 'location' 欄位
df = df.drop(columns=['location'])

# 以 x 軸為時間，y 軸為里程，z 軸為車輛數，顏色為速度，畫出四維圖
# 速度的分色為藍色到紅色
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import ListedColormap, BoundaryNorm
import numpy as np

# 刪除或填充 NaN 值
df = df.dropna()

# 限制無窮大的值
df = df[np.isfinite(df['velocity'])]

# 創建一個 3D 圖形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 定義顏色和範圍
colors = ['white', 'purple', 'red', 'orange', 'yellow', 'green']
bounds = [-1, 0, 20, 40, 60, 80, 160]
norm = BoundaryNorm(bounds, len(colors))
cmap = ListedColormap(colors)

# 繪製散點圖，其中 x 軸為時間，y 軸為里程，z 軸為車輛數，顏色為速度
sc = ax.scatter(df['time_group'], df['mileage'], df['counts_M03A'], c=df['velocity'], cmap=cmap, norm=norm)

# 添加顏色條，並將其與圖形的距離設為 10% 的圖形寬度，並設置標籤
cbar = plt.colorbar(sc, pad=0.3)
cbar.set_label('Speed (km/h)')
cbar.set_ticks([0, 20, 40, 60, 80, 160])
cbar.set_ticklabels(['0', '20', '40', '60', '80', '160'])

# 設置軸標籤
ax.set_xlabel('Time')
ax.set_ylabel('Mileage')
ax.set_zlabel('Number of Cars')
plt.title('11022306CHINNI')
plt.show()

#儲存圖片
plt.savefig(r'C:\Users\User\Desktop\homework\Github\cycu_ai2024\20240507\11022306CHINNI.png')





