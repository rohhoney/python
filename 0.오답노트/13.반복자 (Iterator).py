my_list = [1, 2, 3]

# 리스트 객체를 반복자로 변환
my_iterator = iter(my_list)

# 반복자를 사용하여 리스트의 요소에 접근
print(my_iterator)
print(next(my_iterator))  # 1
print(next(my_iterator))  # 2
print(next(my_iterator))  # 3
#print(next(my_iterator))  # StopIteration 예외 발생


my_list = [1, 2, 3]

# 리스트 객체를 반복자로 변환
my_iterator = iter(my_list)

# for 루프로 반복자 사용
for item in my_iterator:
    print(item,end="")  # 1, 2, 3
