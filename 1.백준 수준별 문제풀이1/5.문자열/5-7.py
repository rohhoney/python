#자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.

T = int(input())

for _ in range(T):
    r, s = input().split()
    r = int(r)
    slist = list(s)
    for i in slist:
        print(i*r,end="")
    print("")
