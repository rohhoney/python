#주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

def check_prime(n):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    if len(divisors) == 2:
        return 1
    return 0

N = int(input())
cnt = 0

a = list(map(int,input().split()))

for i in range(N):
    cnt += check_prime(a[i])

print(cnt)