#C:\Users\User\Desktop\homework\Github\cycu_ai2024\20240507\TDCS_M03A_M05A_combined_processed.csv
import pandas as pd

# 讀取 CSV 檔案
df = pd.read_csv(r'C:\Users\User\Desktop\homework\Github\cycu_ai2024\20240507\TDCS_M03A_M05A_combined_processed.csv')

# 將 'time' 欄位轉換為 datetime 對象
df['time'] = pd.to_datetime(df['time'])

# 提取出小時和分鐘部分，並將其轉換為字串格式
df['time'] = df['time'].dt.strftime('%H:%M')

#刪除第六欄位
df = df.drop(df.columns[5], axis=1)

#儲存為csv檔
df.to_csv(r'C:\Users\User\Desktop\homework\Github\cycu_ai2024\20240507\TDCS_M03A_M05A_combined_processed.csv', index=False)