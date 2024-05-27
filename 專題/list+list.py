#list1=[[2, 8, 14], [6, 12, 18], [1, 7, 13], [4, 10, 16], [3, 9, 15], [5, 11, 17]]
#list2=[[1, 7, 13], [2, 8, 14], [3, 9, 15], [4, 10, 16], [5, 11, 17], [6, 12, 18]]

#list1 = [[0, 0, 0], [0, 2, 0], [0, 0, 4], [0, 2, 4], [4, 0, 4], [4, 2, 4], [4, 2, 0],[4, 0, 0]]
#list2 = [[0, 2, 4], [0, 0, 4], [0, 2, 0], [0, 0, 0], [4, 2, 4], [4, 0, 4], [4, 2, 0],[4, 0, 0]]

list1 = [[0, 0, 0], [0, 2, 0], [0, 0, 4], [0, 2, 4], [4, 0, 4], [4, 2, 4], [4, 2, 0],[4, 0, 0]]
# 使用 sorted() 函數對 list1 進行排序
list1 = sorted(list1, key=lambda x: (x[0], -x[2], -x[1]))

# 使用 min() 函數找到 list1[x][0] 的最小值
min_valuex = min(list1, key=lambda x: x[0])[0]
min_valuey = min(list1, key=lambda x: x[1])[1]
min_valuez = min(list1, key=lambda x: x[2])[2]
print(min_valuex , min_valuey , min_valuez )
# 從 list1 的每個元素的第一個值中減去 min_value
for i in range(len(list1)):
    list1[i][0] -= min_valuex
    list1[i][1] -= min_valuey
    list1[i][2] -= min_valuez

print(list1) 