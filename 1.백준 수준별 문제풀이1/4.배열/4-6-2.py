N, M = map(int, input().split())
basket = [i for i in range(1,N+1)]

for i in range(M):
    a, b = map(int, input().split())
    basket[a-1],basket[b-1] = basket[b-1],basket[a-1] #파이썬은 바꾸기 기능을 제공한다.

print(*basket)