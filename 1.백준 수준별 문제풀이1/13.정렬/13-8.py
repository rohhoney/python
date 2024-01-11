#11650번
# 2차원 좌표를 N번 입력받고 x값 증가순서대로 정렬 하고 만약 같으면 y값 증가량 으로 정렬한다.
import sys

N = int(input())
points = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

points.sort(key=(lambda x: (x[0], x[1]) + (len(points),))) #sort 함수는 튜플을 키로 하면 튜플 순서를 우선순위로 정렬

for i in range(N):
    print(' '.join(list(map(str, (points[i])))))