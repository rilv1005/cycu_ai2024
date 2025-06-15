
a = 0
numbers = [["B1F-C1"], ["1F-C1"], ["B1F-C3"], ["B1F-C1"], ["2F-C1"], ["2F-C2"], ["B2F-C2"], ["2F-C1"]]
for i in range(len(numbers)):
    if "B1F" in numbers[i][0]:
        if "C1" in numbers[i][0]:
            a += 1  
        if "C3" in numbers[i][0]:
            a += 1

print(a)  # 輸出: 1


# 使用列表推導式篩選出以 B1F 開頭的資料
filtered_numbers = [item for item in numbers if item[0].startswith("B1F")]

print(filtered_numbers)  # 輸出: [['B1F-C1'], ['B1F-C3'], ['B1F-C1']]

list3 = [[1,2,3],[4,5,6,7],[1,2]]
list4 = [item for sublist in list3 for item in sublist]
print(list4)  # 輸出: [1, 2, 3, 4, 5, 6, 7, 1, 2]