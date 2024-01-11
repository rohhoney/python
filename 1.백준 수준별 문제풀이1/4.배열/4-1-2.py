# 리스트 요소수 N 입력 받고, 리스트 요소를 입력 받은 후(띄어 쓰기로 구분), 요소 v의 개수 찾기


N = int(input())
list1 = list(map(int,input().split()))

v = int(input())

print(list1.count(v))