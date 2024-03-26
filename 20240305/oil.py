import requests
from bs4 import BeautifulSoup
import pandas as pd

# 定義一個函數來抓取網頁上的表格資料
def get_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tables = soup.find_all('table')
    df = pd.read_html(str(tables[1]))[0]
    return df

# 兩個網址
url1 = "https://vipmbr.cpc.com.tw/mbwebs/ShowHistoryPrice_oil.aspx"
url2 = "https://vipmbr.cpc.com.tw/mbwebs/ShowHistoryPrice_oil2019.aspx"

# 抓取兩個網址的資料
df1 = get_data(url1)
df2 = get_data(url2)

# 將兩個 dataframe 合併
df = pd.concat([df1, df2])

# 重設索引
df.reset_index(drop=True, inplace=True)

# 儲存到 CSV 檔案
df.to_csv('/workspaces/cycu_ai2024/20240305', encoding='utf_8_sig')


# 只保留前6個欄位的資料
df = df.iloc[:, :6]
# 去除值是NaN的資料
df = df.dropna()





#繪製折線圖
#使用繁體中文字型
#x軸是日期 y軸是油價 
#分別是 92無鉛汽油,95無鉛汽油,98無鉛汽油,超級柴油
#除了日期以外的欄位 其他每個欄位都是一條折線
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(10, 6))
plt.plot(df[df.columns[0]], df[df.columns[1]], label='92無鉛汽油')
plt.plot(df[df.columns[0]], df[df.columns[2]], label='95無鉛汽油')
plt.plot(df[df.columns[0]], df[df.columns[3]], label='98無鉛汽油')
plt.plot(df[df.columns[0]], df[df.columns[4]], label='超級柴油')
plt.legend()
plt.show()








