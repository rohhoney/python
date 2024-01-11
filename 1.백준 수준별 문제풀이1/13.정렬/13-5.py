#수 정렬하기3, 메모리 제한 8MB
# 10989번
#인터넷으로 검색한 답... 난 못풀었다.
import sys

n = int(sys.stdin.readline())
num_list = [0] * 10001

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)

