#https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/20240416/
import os
import requests
from bs4 import BeautifulSoup

def download_csv_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for link in soup.find_all('a'):
        file_url = link.get('href')
        if file_url.endswith('/'):  # 如果是資料夾，則遞迴訪問
            download_csv_from_url(url + file_url)
        elif file_url.endswith('.csv'):  # 如果是 csv 檔案，則下載
            file_url = url + file_url
            file_response = requests.get(file_url)
            file_name = os.path.basename(file_url)
            with open(file_name, 'wb') as f:
                f.write(file_response.content)

url = 'https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/20240416/'
download_csv_from_url(url)

