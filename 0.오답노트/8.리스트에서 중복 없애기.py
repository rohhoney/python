#erase duplicated value in list => change list into set

list1=[1,2,3,4,1,2,3,4,1,2,3,4]
print("list:", list1)
set1 = set(list1)
print("set:", set1)

list2 = list(set1)

print("new list:", list2)