#우영우 확인 프로그램

import sys
s = input()
slist = list(s)

cnt = 0

for i in range(len(slist)):
    if slist[i] != slist[-i-1]:
        break
    else:
        cnt +=1
if cnt == len(slist):
    print("1")
else:
    print("0")




