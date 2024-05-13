#list1=[1,2,3]
#list2=[1,2,3]
#list3=[1,2,3]

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [1, 2, 3]

# 使用 zip 函數將三個列表的對應元素組合在一起
zipped = zip(list1, list2, list3)

# 使用 list 函數將結果轉換為列表
list4 = [list(item) for item in zipped]

print(list4)  # 輸出：[[1, 1, 1], [2, 2, 2], [3, 3, 3]]