#영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 이 문자열에는 몇 개의 단어가 있을까? 이를 구하는 프로그램을 작성하시오.

S = input()
Slist = list(S)
a = Slist.count(" ")
if Slist[0] == " " and Slist[-1] == " ":
    print(a - 1)
elif Slist[0] == " " or Slist[-1] == " ":
    print(a)
elif Slist[0] != " " and Slist[-1] != " ":
    print(a+1)
else:
    print(a+1)
