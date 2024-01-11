#입력할 정보 수를 입력하고 두 수를 입력하고 각각 입력받은 두 수의 합을 출력하는 프로그램
times = int(input())

i = 1
resultlist =[]
while i<=times:
    a,b = map(int,input().split())
    sumab = a+b
    resultlist.append(sumab)
    i+=1

for j in resultlist:
    print(j)