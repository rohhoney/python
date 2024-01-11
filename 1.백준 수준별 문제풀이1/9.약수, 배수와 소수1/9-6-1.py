#정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

N = int(input())
if N == 1:
    exit()


i = 2
Soin = []

while i != N:
    if N % i == 0:
        Soin.append(i)
        N = N / i
    else:
        i += 1
Soin.append(int(N))

for k in Soin:
    print(k)