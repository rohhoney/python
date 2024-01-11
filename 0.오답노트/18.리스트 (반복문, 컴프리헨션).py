#[표현식 for 항목 in 반복가능한_객체 if 조건]

list1 = [1,2,3,4,5,6,7,8,9,10]

list_odd = [num for num in list1 if num % 2 != 0]
list_even = [num for num in list1 if num % 2 == 0]

print(list1, list_odd, list_even)

#in loop
str1 = 'abcdefg'
list1 = list(str1)
dic = {}

for i in list1:
    print(i, end='')
print("")

for i in str1:
    print(i, end='')
print("")

