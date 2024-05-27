
list_total=[]
list_P=[[1,2,3,4],[7,8,9,6],[4,5,6,5],[7,8,9,6],[10,11,12,13],[1,2,3,4]]

for i in range (0,len(list_P),1):
	list_total=list_total+list_P[i]
list_total=list(set(list_total))
print(list_total)

list_P2 = [[1,2,3,4],[7,8,9,6],[4,5,6,5],[7,8,9,6],[10,11,12,13],[1,2,3,4]]
list_total2 = []

for i in list_P2:
    if i not in list_total2:
        list_total2.append(i)

print(list_total2)