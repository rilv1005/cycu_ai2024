#"C:\Users\User\Desktop\homework\國科會\仿生結構\實驗excel\20250306 試驗\20250306 試驗\F2D1\ADRL 1mm 1\ADRL 1-1.csv"
#"C:\Users\User\Desktop\homework\國科會\仿生結構\實驗excel\20250306 試驗\20250306 試驗\F2D1\ADRL 1mm 1\ADRL 1-2.csv"
#"C:\Users\User\Desktop\homework\國科會\仿生結構\實驗excel\20250306 試驗\20250306 試驗\F2D1\ADRL 1mm 1\ADRL 1-3.csv"
#"C:\Users\User\Desktop\homework\國科會\仿生結構\實驗excel\20250306 試驗\20250306 試驗\F2D1\ADRL 1mm 1\ADRL 1-4.csv"
#"C:\Users\User\Desktop\homework\國科會\仿生結構\實驗excel\20250306 試驗\20250306 試驗\F2D1\ADRL 1mm 1\ADRL 1-5.csv"
#"C:\Users\User\Desktop\homework\國科會\仿生結構\實驗excel\20250306 試驗\20250306 試驗\F2D1\ADRL 1mm 1\ADRL 1-6.csv"


#"C:\Users\User\Desktop\homework\國科會\仿生結構\實驗excel\20250306 試驗\20250306 試驗\F2D1"

import pandas as pd
import os

# 設定資料夾路徑
folder_path = r"C:\Users\User\Desktop\homework\國科會\仿生結構\實驗excel\20250425 試驗\20250425 試驗\cube 1"

# 初始化一個空的DataFrame來存放整合後的資料
combined_df = pd.DataFrame()

# 定義欄位名稱
columns = ["時間", "荷重", "位移"]

# 遍歷資料夾中的所有檔案
for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        file_path = os.path.join(folder_path, filename)
        # 讀取CSV檔案，略過前三行，並指定編碼格式
        df = pd.read_csv(file_path, skiprows=3, encoding='latin1', names=columns)
        # 將讀取的資料接續到combined_df中
        combined_df = pd.concat([combined_df, df], axis=0, ignore_index=True)

# 確保資料夾中有資料被讀取並合併
if not combined_df.empty:
    # 將整合後的資料儲存為新的Excel檔案
    output_file_path = os.path.join(folder_path, "cube 1 整合.xlsx")
    combined_df.to_excel(output_file_path, index=False)
    print("整合完成")

    # 設定資料夾路徑
folder_path = r"C:\Users\User\Desktop\homework\國科會\仿生結構\實驗excel\20250425 試驗\20250425 試驗\cube 2"

# 初始化一個空的DataFrame來存放整合後的資料
combined_df = pd.DataFrame()

# 定義欄位名稱
columns = ["時間", "荷重", "位移"]

# 遍歷資料夾中的所有檔案
for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        file_path = os.path.join(folder_path, filename)
        # 讀取CSV檔案，略過前三行，並指定編碼格式
        df = pd.read_csv(file_path, skiprows=3, encoding='latin1', names=columns)
        # 將讀取的資料接續到combined_df中
        combined_df = pd.concat([combined_df, df], axis=0, ignore_index=True)

# 確保資料夾中有資料被讀取並合併
if not combined_df.empty:
    # 將整合後的資料儲存為新的Excel檔案
    output_file_path = os.path.join(folder_path, "cube 2 整合.xlsx")
    combined_df.to_excel(output_file_path, index=False)
    print("整合完成")

    # 設定資料夾路徑
folder_path = r"C:\Users\User\Desktop\homework\國科會\仿生結構\實驗excel\20250425 試驗\20250425 試驗\cube 3"

# 初始化一個空的DataFrame來存放整合後的資料
combined_df = pd.DataFrame()

# 定義欄位名稱
columns = ["時間", "荷重", "位移"]

# 遍歷資料夾中的所有檔案
for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        file_path = os.path.join(folder_path, filename)
        # 讀取CSV檔案，略過前三行，並指定編碼格式
        df = pd.read_csv(file_path, skiprows=3, encoding='latin1', names=columns)
        # 將讀取的資料接續到combined_df中
        combined_df = pd.concat([combined_df, df], axis=0, ignore_index=True)

# 確保資料夾中有資料被讀取並合併
if not combined_df.empty:
    # 將整合後的資料儲存為新的Excel檔案
    output_file_path = os.path.join(folder_path, "cube 3 整合.xlsx")
    combined_df.to_excel(output_file_path, index=False)
    print("整合完成")






