#정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램
N,X = map(int,input().split())

n_list = list(map(int,input().split()))

for i in n_list:
    if i < X:
        print(i, end=" ")
