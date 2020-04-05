import copy

lst1 = [1,2,3,4,4,5,6,7,7]
lst2 = [5,5,6,7,7,8,9]

#remove duplicates
uLst1 = []

for item in lst1:
    if item not in uLst1:
        uLst1.append(item)


uLstTemp = copy.deepcopy(uLst1)


for item in lst2:
    if item not in uLstTemp:
        uLst1.append(item)
print("Union is:", uLst1)





#intersection

iList = []
for i in uLstTemp:                  
    if i in lst2:                   
        iList.append(i)

print("Intersection is:",iList)
















                     
