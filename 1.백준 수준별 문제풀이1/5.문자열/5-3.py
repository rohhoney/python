#문자열을 입력으로 주면 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오.

T = int(input())
s_list = []
for _ in range(T):
    s_list.append(input())

for _ in s_list:
    print(_[0],end="")
    print(_[-1])