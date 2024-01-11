###3Ways to reverse list

#1 use reverse() function
a = ['a', 'c', 'b']
a.reverse() #listname.function() is action, it doesn't return any value.
print(a)
a.reverse()
#2 use reversed() function
b = list(reversed(a))
print(b)

#3 use [::-1]
a = a[::-1]
print(a)
a.reverse()

a[0:2] = a[0:2][::-1]   #way to reverse part of the list
print(a)