import requests
from bs4 import BeautifulSoup
import pandas as pd

# 獲取網頁內容
url = "https://vipmbr.cpc.com.tw/mbwebs/ShowHistoryPrice_oil.aspx"
response = requests.get(url)

# 解析網頁內容
soup = BeautifulSoup(response.text, 'html.parser')

# 找到所有的表格元素
tables = soup.find_all('table')

# 將 HTML 表格轉換為 dataframe
df1 = pd.read_html(str(tables[0]))[0]  # 第一個表格
df2 = pd.read_html(str(tables[1]))[0]  # 第二個表格

# 輸出結果
print(df2)

#做成csv檔案
#儲存到桌面
df2.to_csv('C:/Users/USER/Desktop/oil.csv', encoding='utf_8_sig')

#df2 只保留前5個欄位的資料
df2 = df2.iloc[:, :5]
#去除欄位值為NAN的資料
df2 = df2.dropna()
#把第一欄位的資料型態 轉成 datetime
df2.iloc[:, 0] = pd.to_datetime(df2.iloc[:, 0])
#使用 matplotlib 繪製圖表，並設定圖表標題、x 軸是日期、y 軸油價
#除了第一欄位資料，其他每一個欄位資料繪製一條線
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 設定字體為 SimHei
myfont = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
plt.rcParams['axes.unicode_minus'] = False

# 繪製圖表
plt.figure(figsize=(10, 6))
plt.title('CPC 油價走勢圖', fontproperties=myfont)
plt.xlabel('日期', fontproperties=myfont)
plt.ylabel('油價', fontproperties=myfont)
for i in range(1, len(df2.columns)):
    plt.plot(df2.iloc[:, 0], df2.iloc[:, i], label=df2.columns[i])
plt.legend(prop=myfont)
plt.show()
# 儲存圖表到桌面
plt.savefig('C:/Users/USER/Desktop/oil.png')





