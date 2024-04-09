#https://scweb.cwa.gov.tw/zh-tw/earthquake/data/

import requests

# CSV文件的URL
url = 'https://scweb.cwa.gov.tw/zh-tw/earthquake/data/your_csv_file.csv'  # 請將此處替換為實際的CSV文件URL

# 發送HTTP請求並獲取響應
response = requests.get(url)

# 確保我們收到了一個有效的響應
response.raise_for_status()

# 創建一個新的CSV文件並將內容寫入該文件
with open('earthquake_data.csv', 'wb') as f:
    f.write(response.content)