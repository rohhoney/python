#When you have to input many times. Using sys modul and sys.stdin.readlines() module is faster than input()

import sys

T = int(input()) #Test times

for i in range(T):
    a,b = map(int, sys.stdin.readline().split())
    print(a,b)

