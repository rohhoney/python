def prime_factors(N):
    factors = []
    # 2부터 N의 제곱근까지의 수로 반복하여 소인수분해를 진행합니다.
    for i in range(2, int(N**0.5) + 1):
        while N % i == 0:
            factors.append(i)
            N //= i

    # 만약 N이 2 이상인 경우에도 남은 값이 있다면, 그 값 자체도 소인수입니다.
    if N > 1:
        factors.append(N)

    return factors

# 입력 받기
N = int(input())

# 소인수분해 결과 출력
factors = prime_factors(N)
for factor in factors:
    print(factor)
