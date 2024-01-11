#11650번
# 2차원 좌표를 N번 입력받고 x값 증가순서대로 정렬 하고 만약 같으면 y값 증가량 으로 정렬한다.
import sys
def wight(l):
    total = l[0]*1000000 + l[1]
    return total

N = int(input())
points = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

points.sort(key=wight)

for i in range(N):
    print(' '.join(list(map(str, (points[i])))))