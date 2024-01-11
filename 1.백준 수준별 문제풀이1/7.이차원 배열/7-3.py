M = []
N = []

for _ in range(5):
    M.append(list(input()))
    N.append(len(M[_]))

for i in range(15):
    for j in range(5):
        if i < N[j]:
            print(M[j][i],end="")

