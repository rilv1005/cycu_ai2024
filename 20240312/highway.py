
import pandas as pd
import matplotlib.pyplot as plt

# 讀取 CSV 文件
df = pd.read_csv('/workspaces/cycu_ai2024/20240312/112年1-10月交通事故簡訊通報資料.csv')

#找尋國道名稱為國道1號的資料
df1 = df[df['國道名稱'] == '國道3號']
#而且找尋方向為南或者南下的資料
df4 = df1[df1['方向'] == '南']
#而且找尋方向為南或者南下的資料
df3 = df1[df1['方向'] == '南向']
#合併 df2 和 df3
df2 = pd.concat([df4, df3], axis=0)





#把 欄位 '年' '月' '日' '時' '分' 組成一個欄位 '日期' , 並且轉換成日期格式
df2['事件開始'] = df2['年'].astype(str) + '-' + df2['月'].astype(str) + '-' + df2['日'].astype(str) + ' ' + df2['時'].astype(str) + ':' + df2['分'].astype(str)
df2['事件開始'] = pd.to_datetime(df2['事件開始'])
#把 欄位 '年' '月' '日' '事件排除'  合併成一個欄位 '事件排除' , 並且轉換成日期格式
df2['事件排除'] = df2['年'].astype(str) + '-' + df2['月'].astype(str) + '-' + df2['日'].astype(str) + ' ' + df2['事件排除'].astype(str)
df2['事件排除'] = pd.to_datetime(df2['事件排除'])
#drop 欄位 '年' '月' '日' '時' '分'
df2 = df2.drop(columns=['年', '月', '日', '時', '分'])

#將 '事件開始' '事件排除' 兩個欄位轉換成 unix time stamp 並使用整數表示
df2['事件開始1'] = df2['事件開始'].apply(lambda x: int(x.timestamp()))
df2['事件排除1'] = df2['事件排除'].apply(lambda x: int(x.timestamp()))

#df 是您的 DataFrame，並且 '事件開始' 和 '事件排除' 是 datetime 欄位
print(df2[['事件開始', '事件排除', '國道名稱','里程','事件開始1','事件排除1']])
#使用繁體中文
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

#以 '里程' 為 y軸 , '事件開始1' 為 x軸 起點 , '事件排除1' 為 x軸 終點 繪製線段
#圖表標題名稱為 11022306國道1號南向
plt.title('11022306國道3號南向')
for index, row in df2.iterrows():
    plt.plot([row['事件開始1'], row['事件排除1']], [row['里程'], row['里程']])
plt.xlabel('事件時間')
plt.ylabel('里程')
plt.show()




