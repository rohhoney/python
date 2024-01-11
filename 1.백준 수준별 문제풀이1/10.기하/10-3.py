a = []

for _ in range(3):
    a.append(list(map(int,input().split())))

xlist = []
ylist = []

for i in range(3):
    xlist.append(a[i][0])

for i in range(3):
    ylist.append(a[i][1])


for i in xlist:
    if xlist.count(i) == 1:
        print(i,end=" ")

for i in ylist:
    if ylist.count(i) == 1:
        print(i)