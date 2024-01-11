N, M = map(int,input().split())
ball_box = [0 for p in range(N)]

for a in range(M):
    i, j, k = map(int,input().split())
    for l in range(i-1,j):
        ball_box[l] = k

print(*ball_box)