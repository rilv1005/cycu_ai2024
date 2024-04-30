#https://tisvcloud.freeway.gov.tw/history/TDCS/M03A/20240429/
#https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/20240429/

import requests
from bs4 import BeautifulSoup
import os

def get_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    csv_links = [url + node.get('href') for node in soup.find_all('a') if node.get('href').endswith('.csv')]
    dir_links = [url + node.get('href') for node in soup.find_all('a') if node.get('href').endswith('/') and node.get('href') != '/']
    return csv_links, dir_links

def download_csv(url, folder):
    response = requests.get(url)
    filename = os.path.join(folder, url.split('/')[-1])
    with open(filename, 'wb') as f:
        f.write(response.content)

def download_all_csv(url, folder):
    csv_links, dir_links = get_links(url)
    for link in csv_links:
        download_csv(link, folder)
    for link in dir_links:
        download_all_csv(link, folder)

urls = [
    'https://tisvcloud.freeway.gov.tw/history/TDCS/M03A/20240429/',
    'https://tisvcloud.freeway.gov.tw/history/TDCS/M05A/20240429/'
]

for url in urls:
    download_all_csv(url, '/workspaces/cycu_ai2024/20240430')