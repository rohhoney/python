#4의 배수를 입력했을 떄 몫만큼 int 앞에 long 이 붙는 프로그램
a = int(input())
b = a//4
i=0
while i < b:
    print("long",end=" ")
    i += 1
print("int")