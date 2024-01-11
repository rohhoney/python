def find_nth_end_of_the_world(n):
    end_of_the_world = 666
    count = 0

    while True:
        if '666' in str(end_of_the_world):  #이런 간단한 방법이
            count += 1
            if count == n:
                return end_of_the_world
        end_of_the_world += 1

# 입력 받기
n = int(input())

# N번째 영화의 제목에 들어간 수 출력
result = find_nth_end_of_the_world(n)
print(result)
