def Sum_nums(num):
    a = list(str(num))
    a = list(map(int, a))
    return sum(a)

N = int(input())
creator_list = []
divide_sum = 0
for i in range(1, 1000001):
    divide_sum = i + Sum_nums(i)
    if divide_sum == N:
        creator_list.append(i)
if creator_list == []:
    print(0)
else:
    print(min(creator_list))
