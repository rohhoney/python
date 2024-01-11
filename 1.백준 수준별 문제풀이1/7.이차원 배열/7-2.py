a = []
M = []
I = []

for _ in range(9):
    a.append(list(map(int,input().split())))

for i in range(9):
    MAX = max(a[i])
    IDX = a[i].index(MAX)

    M.append(MAX)
    I.append(IDX)

FM = max(M)
L = M.index(FM)
N = I[L]

print(FM)
print(L+1, N+1)

