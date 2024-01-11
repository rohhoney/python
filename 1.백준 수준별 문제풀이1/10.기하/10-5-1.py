N = int(input())

a = []

for _ in range(N):
    a.append(list(map(int,input().split())))

xlist = []
ylist = []

for i in range(N):
    xlist.append(a[i][0])

for i in range(N):
    ylist.append(a[i][1])

x = max(xlist) - min(xlist)
y = max(ylist) - min(ylist)

print(x*y)
