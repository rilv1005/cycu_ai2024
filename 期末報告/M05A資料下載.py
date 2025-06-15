#https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/

import requests
import os
from datetime import datetime, timedelta

# 設定日期範圍
start_date = datetime(2024, 5, 10)
end_date = datetime(2024, 5, 31)

# 建立資料夾
folder_name = 'May_M05A'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# 迭代日期範圍
current_date = start_date
while current_date <= end_date:
    for hour in range(24):
        # 生成URL，時間部分改為每小時的第5分鐘
        url = f"https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/{current_date.strftime('%Y%m%d')}/{str(hour).zfill(2)}/TDCS_M05A_{current_date.strftime('%Y%m%d')}_{str(hour).zfill(2)}5500.csv"
        
        # 下載CSV檔案
        response = requests.get(url)
        if response.status_code == 200:
            # 檔案名稱也相應改為每小時的第5分鐘
            file_path = os.path.join(folder_name, f"TDCS_M05A_{current_date.strftime('%Y%m%d')}_{str(hour).zfill(2)}5500.csv")
            with open(file_path, 'wb') as file:
                file.write(response.content)
            
        else:
            print(f"Failed to download data for {current_date.strftime('%Y%m%d')} hour {str(hour).zfill(2)}")
    
    # 移至下一天
    print(f"Finished downloading data for {current_date.strftime('%Y%m%d')}")
    current_date += timedelta(days=1)