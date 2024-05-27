#https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/

#第一種 https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/M05A_20240101.tar.gz 日期範圍 20240101到20240418


import os
import shutil
import tarfile
from datetime import timedelta, date
import requests

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

def download_file(url, local_filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)
    return local_filename

start_date = date(2024, 1, 1)
end_date = date(2024, 4, 19)

# 建立一個目錄來存放所有的壓縮檔
download_folder = "./M05A_downloads"
os.makedirs(download_folder, exist_ok=True)

# 下載所有壓縮檔
for single_date in daterange(start_date, end_date):
    date_str = single_date.strftime("%Y%m%d")
    url = f"https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/M05A_{date_str}.tar.gz"
    response = requests.get(url)
    if response.status_code == 200:
        download_file(url, os.path.join(download_folder, f"M05A_{date_str}.tar.gz"))

# 建立一個目錄來存放所有的csv文件
destination_folder = "./M05"
os.makedirs(destination_folder, exist_ok=True)

# 解壓縮所有壓縮檔並將csv文件移動到指定目錄
for file_name in os.listdir(download_folder):
    if file_name.endswith(".tar.gz"):
        tar = tarfile.open(os.path.join(download_folder, file_name))
        extract_path = os.path.join(download_folder, file_name[:-7])
        tar.extractall(path=extract_path)
        tar.close()

        for root, dirs, files in os.walk(extract_path):
            for file in files:
                if file.endswith(".csv"):
                    shutil.move(os.path.join(root, file), destination_folder)

#第二種 https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/20240429/ 日期範圍 20240419 到 20240429
#資料型態https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/20240416/00/TDCS_M05A_20240416_000000.csv

from bs4 import BeautifulSoup
from datetime import timedelta, date

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2024, 4, 20)
end_date = date(2024, 4, 30)

# 下載所有csv文件
for single_date in daterange(start_date, end_date):
    date_str = single_date.strftime("%Y%m%d")
    url = f"https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/{date_str}/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a'):
            if link.get('href').endswith('/'):
                sub_url = url + link.get('href')
                sub_response = requests.get(sub_url)
                if sub_response.status_code == 200:
                    sub_soup = BeautifulSoup(sub_response.text, 'html.parser')
                    for sub_link in sub_soup.find_all('a'):
                        if sub_link.get('href').endswith('.csv'):
                            file_url = sub_url + sub_link.get('href')
                            download_file(file_url, os.path.join(destination_folder, sub_link.get('href')))