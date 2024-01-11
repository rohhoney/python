#Input two numbers N times in order to make 2d matrix and find max, min x_value and y_value]
a = '''
N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]

print(a)
# use key =
x_max = max(a, key=lambda x: x[0])[0]
x_min = min(a, key=lambda x: x[0])[0]
y_max = max(a, key=lambda x: x[1])[1]
y_min = min(a, key=lambda x: x[1])[1]

x = x_max - x_min
y = y_max - y_min

print(x * y)
'''

#another example

list1 = ['asdf', 'a', 'asdlfkj', 'dlkfjq']

max_len = max(list1, key = len)
print(max_len)