#https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/20240416/
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_csv_from_url(url, directory):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for link in soup.find_all('a'):
        file_url = link.get('href')
        file_url = urljoin(url, file_url)  # 將相對 URL 轉換為絕對 URL
        if file_url.endswith('/'):  # 如果是資料夾，則遞迴訪問
            download_csv_from_url(file_url, directory)
        elif file_url.endswith('.csv'):  # 如果是 csv 檔案，則下載
            file_response = requests.get(file_url)
            file_name = os.path.join(directory, os.path.basename(file_url))
            with open(file_name, 'wb') as f:
                f.write(file_response.content)
            print(f'Downloaded: {file_name}')  # 打印已下載的檔案名稱

url = 'https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/20240417/'
directory = '/workspaces/cycu_ai2024/20240423/TDCS_M05A_20240417'  # 將此路徑替換為你想要下載到的目錄
os.makedirs(directory, exist_ok=True)  # 創建目錄，如果已存在則不會報錯
download_csv_from_url(url, directory)

