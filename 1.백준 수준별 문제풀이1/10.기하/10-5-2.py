N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]

print(a)
x_max = max(a, key=lambda x: x[0])[0]
x_min = min(a, key=lambda x: x[0])[0]
y_max = max(a, key=lambda x: x[1])[1]
y_min = min(a, key=lambda x: x[1])[1]

x = x_max - x_min
y = y_max - y_min

print(x * y)
