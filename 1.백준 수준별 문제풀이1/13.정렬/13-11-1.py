#18870번
#좌표압축
import sys

N = int(input())
Plist = list(map(int, sys.stdin.readline().split()))
PnI_list = [[Plist[i], i] for i in range(len(Plist))]

PnI_list.sort(key=lambda x: x[0])

k = 0
for i in range(1, len(PnI_list)):
    if PnI_list[i-1][0] == PnI_list[i][0]:
        PnI_list[i-1][0] = k
    else:
        PnI_list[i-1][0] = k
        k += 1
PnI_list[-1][0] = k

PnI_list.sort(key=lambda x: x[1])

for i in PnI_list:
    print(i[0], end=' ')