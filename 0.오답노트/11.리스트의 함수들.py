#####Functions of List#####

    ###Adding###

#insert
a = [1, 2, 3, 4]

a.insert(0,8)   #insert value 8 in position 0

print("insert:", a)

#append
a = [1, 2, 3, 4]

a.append(5)

print("append:",a)

#extend
a = [1, 2, 3, 4]

a.extend([1,2,3])   #parameter of function extend() must be list

print("extend:", a)

###subtraction###

#del
a = [1, 2, 3, 4]

del a[0]
print("del:", a)

#pop
a = [1, 2, 3, 4]

print("return of pop():", a.pop())

print("pop:", a)

#remove
a = [1, 2, 3, 4, 1, 2, 3, 4]
a.remove(1)     #remove() removes first parameter's value
print("remove:", a)


###utility function###

#count
a = [1, 2, 3, 4, 4, 4]

print("count:", a.count(4))

#len
a = [1, 2, 3, 4]
print("len:", len(a))

#reverse
a = [1, 2, 3, 4]
a.reverse()
print("reverse:", a)




