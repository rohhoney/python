#알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
#첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
import sys

S = input().upper()
slist = list(S)
s_set = set(slist)
set_list = list(s_set)
count_list = []
MAX = 0
idx = 0
result = ""

for i in range(len(set_list)):
    a = slist.count(set_list[i])
    count_list.append(a)

MAX = max(count_list)

if count_list.count(MAX) != 1:
    print('?')
else:
    idx = count_list.index(MAX)
    result = set_list[idx]
    print(result)


