#변형 블랙잭

N, M = map(int, input().split())
card = list(map(int,input().split()))
min_sub = -1
max_sum = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum_triple = card[i] + card[j] + card[k]
            if sum_triple > M:
                pass
            else:
                sub = M - sum_triple
                if min_sub == -1:
                    min_sub = sub
                if sub <= min_sub:
                    min_sub = sub
                    max_sum = sum_triple


print(max_sum)