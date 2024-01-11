#GPT's answer

def calculate_change(C):
    # 거스름돈을 쿼터, 다임, 니켈, 페니의 개수로 변환합니다.
    quarters = C // 25
    C %= 25

    dimes = C // 10
    C %= 10

    nickels = C // 5
    C %= 5

    pennies = C

    return quarters, dimes, nickels, pennies

try:
    T = int(input())  # 테스트 케이스의 개수를 입력받습니다.

    for _ in range(T):
        C = int(input())  # 거스름돈 C를 입력받습니다.

        # 필요한 쿼터, 다임, 니켈, 페니의 개수를 계산합니다.
        quarters, dimes, nickels, pennies = calculate_change(C)

        # 결과를 출력합니다.
        print(quarters, dimes, nickels, pennies)

except ValueError:
    print("입력이 올바르지 않습니다.")