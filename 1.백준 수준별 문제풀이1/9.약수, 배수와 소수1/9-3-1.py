#완전수 여부
while True:
    N = int(input())
    if N == -1:
        break

    Nlist = []
    for i in range(1, N):
        if N % i == 0:
            Nlist.append(i)

    if N == sum(Nlist):
        print("%d = " % N, end="")
        for i in range(len(Nlist)-1):
            print(Nlist[i], end="")
            print(" + ", end="")
        print(Nlist[-1])

    else:
        print("%d is NOT perfect." % N)

