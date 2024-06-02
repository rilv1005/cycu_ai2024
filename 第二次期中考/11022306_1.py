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
import pandas as pd
import glob



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

#C:\Users\User\Desktop\homework\Github\cycu_ai2024\M05A
#檔案格式 TDCS_M05A_20240101_000000.CSV

# 創建資料夾
if not os.path.exists('C:\\Users\\User\\Desktop\\homework\\Github\\cycu_ai2024\\M05A_Combined'):
    os.mkdir('C:\\Users\\User\\Desktop\\homework\\Github\\cycu_ai2024\\M05A_Combined')

# 指定欄位名稱
column_names = ['TimeInterval', 'GantryFrom', 'GantryTo', 'VehicleType', 'SpaceMeanSpeed', '交通量']

# 處理每一天的資料
for day in pd.date_range(start='2024-01-01', end='2024-04-30'):
    # 將日期轉換為特定的格式
    day_str = day.strftime('%Y%m%d')

    # 找到所有符合 'TDCS_M05A_{day_str}_*' 模式的檔案
    files = glob.glob(f'M05A\\TDCS_M05A_{day_str}_*')

    # 讀取每個檔案，並將它們存儲在一個列表中
    dataframes = [pd.read_csv(file, skipinitialspace=True, header=None, names=column_names) for file in files]

    # 將所有的 DataFrame 合併成一個
    combined_df = pd.concat(dataframes)

    # 保留 VehicleType=31 的 "SpaceMeanSpeed"
    speed_df = combined_df[combined_df['VehicleType'] == 31][['TimeInterval', 'GantryFrom', 'GantryTo', 'SpaceMeanSpeed', '交通量']]
    speed_df.rename(columns={'交通量': '交通量(小客車 31)'}, inplace=True)

    # 處理其他 VehicleType 的資料
    for vehicle_type in [32, 41, 42, 5]:
        vehicle_df = combined_df[combined_df['VehicleType'] == vehicle_type][['TimeInterval', 'GantryFrom', 'GantryTo', '交通量']]
        vehicle_df.rename(columns={'交通量': f'交通量({vehicle_type})'}, inplace=True)
        speed_df = pd.merge(speed_df, vehicle_df, on=['TimeInterval', 'GantryFrom', 'GantryTo'], how='outer')

    # 將合併後的 DataFrame 寫入新的 CSV 檔案
    speed_df.to_csv(f'C:\\Users\\User\\Desktop\\homework\\Github\\cycu_ai2024\\M05A_Combined\\M05A_{day_str}.csv', index=False)        