#change two variable's value each other

a = 5
b = 7
print(a, b)

a, b = b, a #it works in python
print(a, b)

#in list

list1 =[1,2,3,4,5,6]

list1[0], list1[3] = list1[3], list1[0]

print(list1)