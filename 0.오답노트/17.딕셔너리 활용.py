#learn about dictionary

#Dictionary Definition
di = {}

#keylist
dic_keys = ['a', 'b', 'c']

#valuelist
dic_val = [1, 2, 3]

#append dic keys and value
j = 0
for i in dic_keys:
    di[i] = dic_val[j]
    j += 1

print(di)
#.item() method
print(di.items())   #Iterator
dic_items_list = []
dic_items_list = list(di.items())
print(dic_items_list)


#.get() method
print(di.get('a', 0))
print(di.get('d', 0)) #get(key, default)

#Programing counting keys by dictionary

alpa_list = list("asdgqwefasdflkjqweghlasdihgqwfkjasdlfkhqwpeogihasldkhjgqiwehglksdjf")
dic = {}
for char in alpa_list:
    if char.isalpha():
        dic[char] = dic.get(char, 0) + 1
print(dic)

#find max value

max_keys = [char for char, val in dic.items() if max(dic.values()) == val]
print(max_keys)