#gpt 코드 2

N, M = map(int,input().split())

basket = []
# 바구니에 번호부여하기
for n in range(1, N+1):
    basket.append(n)

# 둘째줄부터 M개의 줄 입력
for _ in range(1,M+1):
    i, j = map(int,input().split())
    basket[i-1:j] = reversed(basket[i-1:j]) #reversed() 사용

print(*basket)