
import pandas as pd
import numpy as np

# 讀取 Excel 文件
file_path = r"C:\Users\User\Desktop\homework\國科會\仿生結構\結案報告\實驗數據\HEXA 實驗數據.xlsx"
df = pd.read_excel(file_path)

# 假設 C 列是位移 (x)，B 列是力 (F)
x = df.iloc[:, 2].values  # 取第三列作為位移數據
F = df.iloc[:, 1].values  # 取第二列作為力數據

# 檢查數據是否為數值型別並處理缺失值
if not np.issubdtype(x.dtype, np.number) or not np.issubdtype(F.dtype, np.number):
    print("位移或力數據不是數值型別，請檢查資料格式。")
    exit()

# 移除缺失值
mask = ~np.isnan(x) & ~np.isnan(F)
x = x[mask]
F = F[mask]

# 過濾位移數據，限制位移 x 只取到 14
mask = x <= 15
x = x[mask]
F = F[mask]

# 使用梯形法則計算應變能 (積分)
U = np.trapz(F, x)  # NumPy 的 trapezoidal rule (梯形法則)

print(U)

# 假設 F 列是位移 (x)，E 列是力 (F)
x = df.iloc[:, 5].values  # 取第六列作為位移數據
F = df.iloc[:, 4].values  # 取第五列作為力數據

# 檢查數據是否為數值型別並處理缺失值
if not np.issubdtype(x.dtype, np.number) or not np.issubdtype(F.dtype, np.number):
    print("位移或力數據不是數值型別，請檢查資料格式。")
    exit()

# 移除缺失值
mask = ~np.isnan(x) & ~np.isnan(F)
x = x[mask]
F = F[mask]

# 過濾位移數據，限制位移 x 只取到 14
mask = x <= 15
x = x[mask]
F = F[mask]

# 使用梯形法則計算應變能 (積分)
U = np.trapz(F, x)  # NumPy 的 trapezoidal rule (梯形法則)

print(U)

# 假設 L 列是位移 (x)，K 列是力 (F)
x = df.iloc[:, 8].values  # 取第九列作為位移數據
F = df.iloc[:, 7].values  # 取第八列作為力數據

# 檢查數據是否為數值型別並處理缺失值
if not np.issubdtype(x.dtype, np.number) or not np.issubdtype(F.dtype, np.number):
    print("位移或力數據不是數值型別，請檢查資料格式。")
    exit()

# 移除缺失值
mask = ~np.isnan(x) & ~np.isnan(F)
x = x[mask]
F = F[mask]

# 過濾位移數據，限制位移 x 只取到 14
mask = x <= 15
x = x[mask]
F = F[mask]

# 使用梯形法則計算應變能 (積分)
U = np.trapz(F, x)  # NumPy 的 trapezoidal rule (梯形法則)

print(U)