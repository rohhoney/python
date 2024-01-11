import sys
import time
N = int(input())
list1 = list(set(map(int, sys.stdin.readline().split())))
def find_value_or_default(value):
    try:
        index = list1.index(value)
        return 1
    except ValueError:
        return 0

M = int(input())
list2 = list(map(int, sys.stdin.readline().split()))

list3 = list(map(find_value_or_default, list2))
print(*list3)