import sys #Test case

while True:
    try: #try: except: => 무한루프일 떄, 프로그램 종료 조건이 따로 없을때 사용하면 좋다.
        a,b = map(int, sys.stdin.readline().split())
        print(a+b)
    except:
        break
