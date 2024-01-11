N, M = map(int,input().split())
ball_box = [p+1 for p in range(N)]

for a in range(M):
    i, j = map(int,input().split())
    storage = ball_box[i-1]
    ball_box[i-1] = ball_box[j-1]
    ball_box[j-1] = storage

print(*ball_box)