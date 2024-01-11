#김은서 코드
#set함수로 중복 지우기

num = [int(input()) for _ in range(10)]

num_div = [n%42 for n in num]

set_div = set(num_div)
print(len(set_div))