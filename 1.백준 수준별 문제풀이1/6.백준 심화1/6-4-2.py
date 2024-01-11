s = input()
slist = list(s)

for i in range(len(slist)):
    if slist[i] != slist[-i-1]:
        break
    else:
        pass

if i == len(slist) - 1:
    print("1")
else:
    print("0")