#int(input().split()) doesn't work. Then what should we use?

a,b = map(int, input().split())
print(a, b)

#Change string to integer by using map() function
test_string = '12345'
test_list = list(test_string)
print(test_list)
test_list2 = list(map(int, test_string))    #Take Notice that using list() function
print(test_list2)

#Using 'lambda' with map() function
#it is convenient to use 'lambda' instead of function when function is not that complicate

test_list3 = [1, 2, 3, 4, 5]

def add_plus1(x):
    x += 1
    return x
#Using def
test_list3 = list(map(add_plus1,test_list3))
print(test_list3)
#Using lambda
test_list3 = list(map(lambda x: x+1, test_list3))
print(test_list3)