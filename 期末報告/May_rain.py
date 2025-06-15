import requests
from bs4 import BeautifulSoup
#'StationId','StationName','CountyName','TownName','StationLatitude','StationLongitude','StationAltitude','DateTime','Past1hr','Past10Min','Past3hr','Past6hr','Past12hr','Past24hr','NOW','Past2days','Past3days'
#建立一個空的csv檔，命名為rain05.csv

import csv
filename = "C:\\Users\\User\\Desktop\\homework\\Github\\cycu_ai2024\\May_rain\\rain05.csv"
# 定義標題行
headers = ['StationId', 'StationName', 'CountyName', 'TownName', 'StationLatitude', 'StationLongitude', 'StationAltitude', 'DateTime', 'Past1hr', 'Past10Min', 'Past3hr', 'Past6hr', 'Past12hr', 'Past24hr', 'NOW', 'Past2days', 'Past3days']
# 創建並寫入標題行到 CSV 檔案
with open(filename, "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)
    


first_chars = ['A']
second_chars = ['x', 'y', 'z', '0', '1', '2', '3', '4', '5']
n=1
#https://history.colife.org.tw/?r=/download&path=L%2Bawo%2BixoS%2FkuK3lpK7msKPosaHnvbJf6Zuo6YeP56uZLzIwMjQwNS9yYWluXzIwMjQwNTAxLnppcA%3D%3D
for first_char in first_chars:
     for second_char in second_chars:
        url = f"https://history.colife.org.tw/?r=/download&path=L%2Bawo%2BixoS%2FkuK3lpK7msKPosaHnvbJf6Zuo6YeP56uZLzIwMjQwNS9yYWluXzIwMjQwNT({first_char}{second_char})LnppcA%3D%3D"
        response = requests.get(url)
        # process the response here
        #下載url中的zip檔
        import requests
        import shutil
        import zipfile
        #定義URL和儲存路徑
        url1 = url
        save_path = "20240612"+str(n).zfill(2)+first_char+second_char+".zip"
        #下載檔案
        response = requests.get(url1, stream=True)
        with open(save_path, "wb") as file:
            shutil.copyfileobj(response.raw, file)
        #儲存路徑，解壓縮，儲存到C:\Users\Cosmos\Desktop\中原\cycu.ai11022329\20240612中
        with zipfile.ZipFile(save_path, 'r') as zip_ref:
            zip_ref.extractall("C:\\Users\\User\\Desktop\\homework\\Github\\cycu_ai2024\\May_rain")
        #刪除zip檔
        import os
        os.remove(save_path)
            

first_chars = ['E']
second_chars = ['w', 'x', 'y','1', '2', '3', '4', '5']
#https://history.colife.org.tw/?r=/download&path=L%2Bawo%2BixoS%2FkuK3lpK7msKPosaHnvbJf6Zuo6YeP56uZLzIwMjQwNS9yYWluXzIwMjQwNTEwLnppcA%3D%3D
for first_char in first_chars:
    for second_char in second_chars:
        url = f"https://history.colife.org.tw/?r=/download&path=L%2Bawo%2BixoS%2FkuK3lpK7msKPosaHnvbJf6Zuo6YeP56uZLzIwMjQwNS9yYWluXzIwMjQwNT({first_char}{second_char})LnppcA%3D%3D"
        response = requests.get(url)
        # process the response here
        import requests
        import shutil
        import zipfile
        #定義URL和儲存路徑
        url1 = url
        save_path = "20240612"+str(n).zfill(2)+first_char+second_char+".zip"
        #下載檔案
        response = requests.get(url1, stream=True)
        with open(save_path, "wb") as file:
            shutil.copyfileobj(response.raw, file)
        #儲存路徑，解壓縮，儲存到C:\Users\Cosmos\Desktop\中原\cycu.ai11022329\20240612中
        with zipfile.ZipFile(save_path, 'r') as zip_ref:
            zip_ref.extractall("C:\\Users\\User\\Desktop\\homework\\Github\\cycu_ai2024\\May_rain")
        #刪除zip檔
        import os
        os.remove(save_path)


first_chars = ['I']
second_chars = ['w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5']
#https://history.colife.org.tw/?r=/download&path=L%2Bawo%2BixoS%2FkuK3lpK7msKPosaHnvbJf6Zuo6YeP56uZLzIwMjQwNS9yYWluXzIwMjQwNTIwLnppcA%3D%3D
for first_char in first_chars:
    for second_char in second_chars:
        url = f"https://history.colife.org.tw/?r=/download&path=L%2Bawo%2BixoS%2FkuK3lpK7msKPosaHnvbJf6Zuo6YeP56uZLzIwMjQwNS9yYWluXzIwMjQwNT({first_char}{second_char})LnppcA%3D%3D"
        response = requests.get(url)
        # process the response here
        import requests
        import shutil
        import zipfile
        #定義URL和儲存路徑
        url1 = url
        save_path = "20240612"+str(n).zfill(2)+first_char+second_char+".zip"
        #下載檔案
        response = requests.get(url1, stream=True)
        with open(save_path, "wb") as file:
            shutil.copyfileobj(response.raw, file)
        #儲存路徑，解壓縮，儲存到C:\Users\Cosmos\Desktop\中原\cycu.ai11022329\20240612中
        with zipfile.ZipFile(save_path, 'r') as zip_ref:
            zip_ref.extractall("C:\\Users\\User\\Desktop\\homework\\Github\\cycu_ai2024\\May_rain")
        #刪除zip檔
        import os
        os.remove(save_path)

first_chars = ['M']
second_chars = ['w', 'x']
#https://history.colife.org.tw/?r=/download&path=L%2Bawo%2BixoS%2FkuK3lpK7msKPosaHnvbJf6Zuo6YeP56uZLzIwMjQwNS9yYWluXzIwMjQwNTMwLnppcA%3D%3D
for first_char in first_chars:
    for second_char in second_chars:
        url = f"https://history.colife.org.tw/?r=/download&path=L%2Bawo%2BixoS%2FkuK3lpK7msKPosaHnvbJf6Zuo6YeP56uZLzIwMjQwNS9yYWluXzIwMjQwNT({first_char}{second_char})LnppcA%3D%3D"
        response = requests.get(url)
        # process the response here
        import requests
        import shutil
        import zipfile
        #定義URL和儲存路徑
        url1 = url
        save_path = "20240612"+str(n).zfill(2)+first_char+second_char+".zip"
        #下載檔案
        response = requests.get(url1, stream=True)
        with open(save_path, "wb") as file:
            shutil.copyfileobj(response.raw, file)
        #儲存路徑，解壓縮，儲存到C:\Users\Cosmos\Desktop\中原\cycu.ai11022329\20240612中
        with zipfile.ZipFile(save_path, 'r') as zip_ref:
            zip_ref.extractall("C:\\Users\\User\\Desktop\\homework\\Github\\cycu_ai2024\\May_rain")
        #刪除zip檔
        import os
        os.remove(save_path)





                



