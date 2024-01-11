N1, N2 = input().split()

n1list = list(N1)
n2list = list(N2)

n1list.reverse()
n2list.reverse()

cN1 = ''.join(n1list)
cN2 = ''.join(n2list)

cN1 = int(cN1)
cN2 = int(cN2)

if cN1>cN2:
    print(cN1)
else:
    print(cN2)
