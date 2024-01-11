#1427번 문자열 입력 받아서 정렬

S = input()
S_list = list(S)
S_list.sort()
S_list.reverse()
print(''.join(S_list))
