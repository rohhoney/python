# 자연수 5개 평균값과 중앙값 구하기
num_list = [int(input()) for _ in range(5)]
num_list.sort()

print(int(sum(num_list)/5))
print(num_list[2])