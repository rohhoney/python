#9개의 정수중 최댓값을 찾고 배열에서 그 수가 몇번째인지 찾기
array =[int(input()) for i in range(9)]
print(max(array))
print(array.index(max(array))+1)
