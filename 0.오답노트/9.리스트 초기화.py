#Ways to initialize list

list1 = []
list2 = [0 for i in range(10)]
list3 = [i*2 for i in range(10)]
list4 = list(map(int, list3))
print(list1, list2, list3, list4)
