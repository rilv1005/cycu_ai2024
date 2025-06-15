import numpy as np
a = 0
for i in range(0,24,1):
    a+=1
    b = 7.5+i*15
    b = b*np.pi/180
    x = 100*np.sin(b)
    y = 100*np.cos(b)
    print("第",a,"點",round(b*180/np.pi,1),"度",round(x,2),round(y,2)) 


# 定義圓的半徑
radius = 19.08

# 初始化計數器
a = 0

# 計算每隔 15 度的 x 和 y 座標
for i in range(0, 360, 30):
    a += 1
    angle_deg = i
    angle_rad = np.deg2rad(angle_deg)
    x = radius * np.sin(angle_rad)
    y = radius * np.cos(angle_rad)
    print("第", a, "點", round(angle_deg, 1), "度", round(x, 2), round(y, 2))