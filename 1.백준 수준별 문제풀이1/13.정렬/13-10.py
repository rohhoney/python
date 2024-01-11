#10814
#나이 이름이 n번 입력되면, 나이->가입 순으로 정렬
import sys
N = int(input())
member = [sys.stdin.readline().split() for i in range(N)]

member.sort(key=lambda x: int(x[0]))

for i in member:
    print(*i)