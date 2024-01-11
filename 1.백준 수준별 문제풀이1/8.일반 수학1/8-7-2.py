#GPT
def calculate_days(A, B, V):
    # 정상에 도달하기 위해 필요한 총 거리
    total_distance = V - A
    # 하루에 올라가는 거리로 정상에 도달하기까지 필요한 일수 계산
    days = total_distance // (A - B)

    # 만약 나머지가 있다면 하루 더 걸린다는 의미이므로 1일을 추가
    if total_distance % (A - B) != 0:
        days += 1

    # 정상에 도달하는 날은 하루를 추가해줍니다.
    days += 1

    return days

# 입력 받기
A, B, V = map(int, input().split())

# 결과 출력
print(calculate_days(A, B, V))

