#9개의 정수중 최댓값을 찾고 배열에서 그 수가 몇번째인지 찾기
array =[]
for i in range(9):
    array.append(int(input()))

max = array[0]
counter = 0
max_cnt = counter
for j in range(1,9):
    if max < array[j]:
        max = array[j]
        counter += 1
        max_cnt = counter
    else:
        counter += 1
print(max)
print(max_cnt+1)