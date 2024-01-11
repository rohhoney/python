
str1 = "asdf1234resfqwegsadgqwe"
list1 = list(str1)

#in loop

for i in str1:
    print(i,end='')
print('')
for i in list1:
    print(i,end='')
print('')

#if

if '1234' in str1:
    print("1")
else:
    print('0')

if list('1234') in list1:
    print("1")
else:
    print('0')

