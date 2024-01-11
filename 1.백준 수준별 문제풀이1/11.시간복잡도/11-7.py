a, b = map(int, input().split())    # y = an + b
c = int(input())    # y = cn
n0 = int(input())    # n >= n0

if a > c:
    print(0)
elif a * n0 + b > c * n0:
    print(0)
else:
    print(1)


