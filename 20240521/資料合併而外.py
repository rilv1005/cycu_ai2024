

from bs4 import BeautifulSoup
from datetime import timedelta, date

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

# 建立一個目錄來存放所有的csv文件
destination_folder = "./M05"
os.makedirs(destination_folder, exist_ok=True)

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2024, 4, 27)
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