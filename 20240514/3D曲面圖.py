#/workspaces/cycu_ai2024/20240514/TDCS_M03A_M05A_New.csv

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy.interpolate import griddata
import numpy as np

# 讀取 csv 文件
df = pd.read_csv('/workspaces/cycu_ai2024/20240514/TDCS_M03A_M05A_New.csv')

# 只取 'direct' 為 'N' 的數據
df = df[df['direct'] == 'N']

# 將 'time' 欄位的數據從字符串轉換為 datetime 對象，並提取時間
df['time'] = pd.to_datetime(df['time']).dt.time

# 將時間轉換為分鐘數
df['time'] = df['time'].apply(lambda t: t.hour * 60 + t.minute)

# 提取 'time'、'counts' 和 'milage' 欄位的數據
x = df['time']
y = df['counts']
z = df['milage']

# 創建網格
xi = np.linspace(x.min(), x.max(), 100)
yi = np.linspace(y.min(), y.max(), 100)
xi, yi = np.meshgrid(xi, yi)
zi = griddata((x, y), z, (xi, yi), method='cubic')

# 創建 3D 圖表
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(xi, yi, zi, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# 設置軸的名稱
ax.set_xlabel('Time')
ax.set_ylabel('Counts')
ax.set_zlabel('Milage')

# 添加顏色條，並將其與圖表分開
fig.colorbar(surf, shrink=0.5, aspect=5, pad=0.1)

plt.show()
#儲存圖表
plt.savefig('3D曲面圖.png')