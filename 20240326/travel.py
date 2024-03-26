import os
import requests
from bs4 import BeautifulSoup

def download_files(url, folder_path):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    for link in soup.find_all('a'):
        href = link.get('href')

        # 如果是資料夾，則遞迴地訪問
        if href.endswith('/'):
            new_folder_path = os.path.join(folder_path, href[:-1])
            if not os.path.exists(new_folder_path):
                os.makedirs(new_folder_path)
            download_files(url + href, new_folder_path)
        # 如果是檔案，則下載
        elif href.endswith('.csv'):
            file_url = url + href
            file_name = href
            print(f"Downloading {file_name}...")
            r = requests.get(file_url, stream=True)
            with open(os.path.join(folder_path, file_name), 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            print(f"Downloaded {file_name}!")

# 使用範例
#download_files("https://tisvcloud.freeway.gov.tw/history/TDCS/M04A/20240325/", "TDCS_M04A_20240325")

import pandas as pd
import glob

# 找到所有的 csv 檔案
csv_files = glob.glob('/workspaces/cycu_ai2024/20240326/TDCS_M04A_20240325')

# 讀取所有的 csv 檔案並將它們合併成一個 DataFrame
df_list = [pd.read_csv(file) for file in csv_files]
combined_df = pd.concat(df_list, ignore_index=True)

# 將合併後的 DataFrame 儲存為一個 csv 檔案
combined_df.to_csv('/workspaces/cycu_ai2024/20240326/TDCS_M04A_20240325.csv', index=False)
