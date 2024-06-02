#https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/
#第一種 壓縮檔案
#https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/M05A_20240101.tar.gz
#第二種 網頁資料夾
#https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/20240416/
#https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/20240416/TDCS_M05A_20240416_000000.CSV

import requests
from bs4 import BeautifulSoup
from datetime import timedelta, date
import os
import tarfile
from urllib.parse import urljoin
import re

# 確保資料夾存在
if not os.path.exists('M05A'):
    os.makedirs('M05A')

def download_and_extract_file(url, local_filename, folder):
    # 下載檔案
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(os.path.join(folder, local_filename), 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)
    
    # 如果是.tar.gz檔案，則解壓縮
    if local_filename.endswith('.tar.gz'):
        with tarfile.open(os.path.join(folder, local_filename), 'r:gz') as tar:
            members = tar.getmembers()
            # 移除檔案路徑中的資料夾名稱
            for member in members:
                member.name = os.path.basename(member.name)
            tar.extractall(path='M05A', members=members)  # 解壓縮到'M05A'資料夾

def download_csv_file(url, local_filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)
    return local_filename

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

def download_file(url, local_filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)

start_date = date(2024, 1, 1)
end_date = date(2024, 5, 1)

destination_folder = 'M05A'

for single_date in daterange(start_date, end_date):
    date_str = single_date.strftime("%Y%m%d")
    url1 = f"https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/M05A_{date_str}.tar.gz"
    url2 = f"https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/{date_str}/"
    response1 = requests.get(url1)
    if response1.status_code == 200:
        # 下載並解壓縮.tar.gz檔案
        download_and_extract_file(url1, f"M05A_{date_str}.tar.gz", 'M05A_tar')
    else:
        response2 = requests.get(url2)
        if response2.status_code == 200:
            soup = BeautifulSoup(response2.text, 'html.parser')
            for link in soup.find_all('a'):
                if link.get('href').endswith('/'):
                    sub_url = urljoin(url2, link.get('href'))  # 使用urljoin來組合URL
                    sub_response = requests.get(sub_url)
                    if sub_response.status_code == 200:
                        sub_soup = BeautifulSoup(sub_response.text, 'html.parser')
                        for sub_link in sub_soup.find_all('a'):
                            if sub_link.get('href').endswith('.csv'):
                                file_url = urljoin(sub_url, sub_link.get('href'))  # 使用urljoin來組合URL
                                download_csv_file(file_url, os.path.join(destination_folder, os.path.basename(sub_link.get('href'))))  # 使用os.path.basename來獲取檔案名稱

        