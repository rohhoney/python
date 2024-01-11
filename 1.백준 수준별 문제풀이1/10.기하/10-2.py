x, y, w, h = map(int,input().split())

dlist = []
dlist.append(x)
dlist.append(y)
dlist.append(w-x)
dlist.append(h-y)

print(min(dlist))