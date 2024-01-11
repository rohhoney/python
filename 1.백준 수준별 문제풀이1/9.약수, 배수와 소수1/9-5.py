
def check_prime(n):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    if len(divisors) == 2:
        return 1
    return 0



M = int(input())
N = int(input())
Prime = []
for i in range(M, N+1):
    if check_prime(i) == 1:
        Prime.append(i)

if Prime == []:
    print(-1)
else:
    print(sum(Prime))
    print(min(Prime))