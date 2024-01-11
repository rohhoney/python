###string function###

#count
a = "hobby"
print(a.count('b'))

#find, index
print(a.find('b')) #find return first 'b' position in hobby
print(a.index('b')) #it is same find
print(a.find('c')) #find return -1 when there is no 'c' in string.However, 'index' makes error

#join
print(",".join('abcd'))
print(','.join(['a','b','c','d'])) #join() can use with string, list, tuple

##########
print(''.join(['a', 'b', 'c', 'd'])) #it is the way that makes string from list
##########

#upper, lower
print("ab".upper())
print("AB".lower())

#r,l strip
print("      a".lstrip())
print("a     ".rstrip())

#replace

string = "oh my god"
print(string.replace("god","mom"))
print(string)
##########
#split() <= delete space and makes string into list
list1 = string.split()
print(list1)
##########



