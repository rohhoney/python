N = int(input())

K = N//5

for k in range(K+1):
    i = 0
    five = 0
    while True:
        if N == 5 * (K-k) + 3 * i:
            break
        elif N < 5 * (K-k) + 3 * i:
            break
        else:
            i += 1
    if N == 5 * (K-k) + 3 * i:
        five = K-k
        break

if five * 5 + i * 3 == N:
    print(five + i)
else:
    print(-1)
