#주사위 상금 게임
#d1,d2,d3=input().split()
#d1 = int(d1)
#d2 = int(d2)
#d3 = int(d3)
d1,d2,d3 = map(int,input().split())
dlist = [d1,d2,d3]

if d1 == d2 == d3:
    price = 10000 + d1*1000
elif d1!=d2 and d1!=d3 and d2!=d3:
    maxd = max(dlist)
    price = maxd*100
else:
    if d1==d2:
        price = 1000 + d1*100
    elif d1==d3:
        price = 1000 + d1 * 100
    else:
        price = 1000 + d2 * 100

print(price)