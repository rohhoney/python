N, M = map(int,input().split())
basket = [a for a in range(1,N+1)]

for k in range(M):
    i, j = map(int, input().split())
    reverse_list = basket[i-1:j]
    reverse_list.reverse()
    a = 0
    for l in range(i-1, j):
        basket[l] = reverse_list[a]
        a+=1

print(*basket)