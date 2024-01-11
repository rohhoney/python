import sys
T = int(input()) #Test case
for i in range(T):
        a,b = map(int, sys.stdin.readline().split())
        print("Case #%d: '%d"%(i+1,a+b))