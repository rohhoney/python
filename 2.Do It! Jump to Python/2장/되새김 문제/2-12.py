from copy import copy

a = b = [1, 2, 3]
a[1] = 4
print(b)

b = copy(a)
a[1] = 2
print(a)
print(b)