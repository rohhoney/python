#10개의 수를 입력 받고 42로 나눈 나머지의 종류 개수 구하기

num_list = []
remain_list =[]
a = 0

for i in range(10):
    num_list.append(int(input()))

for j in num_list:
    remain_list.append(j % 42)

remain_list.sort()

for k in remain_list:
    if remain_list.count(k) != 1:
        for l in range(remain_list.count(k)-1):
            remain_list.remove(k)

print(remain_list)
print(len(remain_list))
