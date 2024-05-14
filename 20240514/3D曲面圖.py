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

# 將時間轉換為分鐘數，並且每5分鐘作為一個單位
df['time'] = df['time'].apply(lambda t: (t.hour * 60 + t.minute) // 5)

# 提取 'time'、'counts' 和 'milage' 欄位的數據
x = df['time']
y = df['milage']
z = df['counts']


# 假設 num 是你想要的網格密度
num = 50

# 創建網格
xi = np.linspace(x.min(), x.max(), num)
yi = np.linspace(y.min(), y.max(), num)
xi, yi = np.meshgrid(xi, yi)

# 使用 'linear' 插值方法計算網格上每個點的 z 值
zi = griddata((x, y), z, (xi, yi), method='linear')

# 創建 3D 圖表
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(xi, yi, zi, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# 設置軸的名稱
ax.set_xlabel('Time')
ax.set_ylabel('Counts')
ax.set_zlabel('Milage')

#繪製曲面圖
surf = ax.plot_surface(xi, yi, zi, cmap=cm.coolwarm)

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


# 創建四個子圖，每個子圖展示一個不同的視角
fig = plt.figure(figsize=(12, 10))

# 創建四個子圖，每個子圖展示一個不同的視角
for i, angle in enumerate([0, 90, 180, 270]):
    ax = fig.add_subplot(2, 2, i+1, projection='3d')
    ax.plot_surface(xi, yi, zi, cmap='viridis')
    ax.view_init(elev=30., azim=angle)
    
    # 座標軸標籤
    ax.set_xlabel('Time')
    ax.set_ylabel('Counts')
    ax.set_zlabel('Milage')


# 添加顏色條，並將其與圖表分開
fig.colorbar(surf, shrink=0.5, aspect=5, pad=0.1)
# 將圖表標題設置為 '11022306CHINGNI'，並將其移到最上方
fig.suptitle('11022306CHINGNI', y=0.95)

plt.show()
#儲存圖表
plt.savefig('3D曲面圖.png')