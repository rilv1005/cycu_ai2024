import pandas as pd

# 讀取 CSV 文件
df = pd.read_csv('C:\Users\User\Desktop\0312\cycu_ai2024\20240312\112年1-10月交通事故簡訊通報資料.csv')

# 篩選出與國道一號相關且行駛方向為南下的數據
highway1_south = df[(df['國道名稱'] == '國道一號') & (df['方向'] == '南下')]

# 統計國道一號南下的里程數
mileage = highway1_south['里程'].sum()

print(mileage)