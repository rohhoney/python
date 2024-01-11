#진법변환
def change(x):
    if x in list('0123456789'):
        return int(x)
    elif x in list("ABCDEFGHIJKLNMOPQRSTUVWXYZ"):
        return ord(x) - ord('A') + 10



S, N = input().split()

N = int(N)
Slist = list(S)
Rlist = []
Slist.reverse()
result = 0

for i in range(len(Slist)):
        result = result + change(Slist[i]) * (N ** i)

print(result)