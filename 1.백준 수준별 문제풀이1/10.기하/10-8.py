line_list = list(map(int,input().split()))

line_list.sort()

if line_list[0] + line_list[1] <= line_list[2]:
    print(2 * (line_list[0] + line_list[1]) - 1)
else:
    print(sum(line_list))