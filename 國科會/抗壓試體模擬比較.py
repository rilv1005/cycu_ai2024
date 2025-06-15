#"C:\Users\User\Desktop\homework\國科會\仿生結構\結案報告\模擬數據"
#"C:\Users\User\Desktop\homework\國科會\仿生結構\結案報告\模擬數據\ADRL1D2.txt"

import pandas as pd

# 讀取txt檔案
txt_file_path = r"C:\Users\User\Desktop\homework\國科會\仿生結構\結案報告\模擬數據\DDRL1D2.txt"
data = pd.read_csv(txt_file_path, delimiter=",")  # 假設txt檔案是以逗號分隔的

# 將資料寫入excel檔案
excel_file_path = r"C:\Users\User\Desktop\homework\國科會\仿生結構\結案報告\模擬數據\DDRL1D2.xlsx"
data.to_excel(excel_file_path, index=False)

print(f"已將 {txt_file_path} 轉換成 {excel_file_path}")