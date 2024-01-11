#꽤 많은 요소 정렬, 수는 중복되지 않음
import sys

T = int(input())
num_list = [int(sys.stdin.readline()) for i in range(T)]

num_list.sort()

for i in num_list:
    print(i)

