#"C:\Users\User\Desktop\homework\海岸工程\final\P1_surfaceElevation.xlsx"
import pandas as pd

# 讀取 Excel 檔案
file_path = "C:/Users/User/Desktop/homework/海岸工程/final/P1_surfaceElevation.xlsx"
df = pd.read_excel(file_path)

# 假設 'eta (m)' 是欄位名稱
eta_values = df['eta (m)'].tolist()

# 分組
groups = []
current_group = []
for value in eta_values:
    if current_group and ((current_group[-1] < 0 and value >= 0) or (current_group[-1] >= 0 and value < 0)):
        groups.append(current_group)
        current_group = []
    current_group.append(value)
if current_group:
    groups.append(current_group)

# 合併一組負值與一組正值
merged_groups = []
i = 0
while i < len(groups) - 1:
    merged_groups.append(groups[i] + groups[i + 1])
    i += 2
if i == len(groups) - 1:
    merged_groups.append(groups[i])

# 找出每組的最大值與最小值
group_min_max = [(min(group), max(group)) for group in merged_groups]

# 列出結果
for i, (min_val, max_val) in enumerate(group_min_max):
    print(f"Group {i+1}: Min = {min_val}, Max = {max_val}")
