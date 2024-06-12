#list1=[1,2,3]
#list2=[1,2,3]
#list3=[1,2,3]

import numpy as np

#list1 = [1,2,3,4]
#list2 = [4,5,6,5]
#list3 = [7,8,9,6]
list4=[[1,2,3,4],[4,5,6,5],[7,8,9,6]]
#list5=[[1,4,7],[2,5,8],[3,6,9],[4,5,6]]

list4 = [[1,2,3,4],[4,5,6,5],[7,8,9,6]]

# 使用 zip 函數將 list4 的行和列互換
list5 = [list(item) for item in zip(*list4)]
import numpy as np

# 原始的 list5
list5 = [[1, 4, 7], [2, 5, 8], [3, 6, 9], [4, 5, 6]]

# 使用 numpy 的 array 函數將 list5 轉換為矩陣
#matrix = np.array(list5)

#print(matrix)
print(list5)  # 輸出：[[1, 4, 7], [2, 5, 8], [3, 6, 9], [4, 5, 6]]

matrix = list5

print(matrix)


#list6=[[1,1]]
#list7=[1,1]


