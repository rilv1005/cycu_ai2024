
import numpy as np
import math

fc = 1.5 # 穩定入滲率
f0 = 5.0 # 初期入滲率
k = 0.188 # 穩定入滲率與初期入滲率的比值
h = 1 # 時間區間
t = 0 # 時間
hr = int(input("請輸入需計算總小時的總入滲量: "))
timelist = list() #小時數
infil_volume_list = list()

def cal_infiltration_rate(t):
    infil_volume = fc + (f0 - fc) * math.exp(-k * t)
    return infil_volume 

# 計算每小時的入滲量
for i in range(hr+1):
    timelist.append(t)
    infil_volume_list.append(cal_infiltration_rate(t))
    t += h

infil_total_volume_list =np.array([timelist, infil_volume_list])
print("時間： ",infil_total_volume_list[0],"入滲量： ", infil_total_volume_list[1])

# 使用複合辛普森法則計算總入滲量
for i in range(1,hr,1):
    
    if i%2 == 0:
        infil_volume_list[i] = 2*infil_volume_list[i]
        print(i, infil_volume_list[i])
    elif i%2 == 1:
        infil_volume_list[i] = 4*infil_volume_list[i]
        print(i, infil_volume_list[i])

infil_total_volume = h/3 * sum(infil_volume_list)
print("總入滲量為: ", infil_total_volume, "立方公尺")