W_Matrix = [[0 for _ in range(100)] for i in range(100)]

T = int(input())

for _ in range(T):
    i, j = map(int,input().split())
    for k in range(10):
        for l in range(10):
            W_Matrix[i+k][j+l] = 1

area = 0

for _ in range(100):
    area = area + W_Matrix[_].count(1)
print(area)