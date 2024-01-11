def get_divisors(n):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors

def is_perfect_number(n):
    divisors = get_divisors(n)
    if sum(divisors) == n:
        return divisors
    else:
        return None

while True:
    n = int(input())
    if n == -1:
        break

    divisors = is_perfect_number(n)
    if divisors:
        print(f"{n} = {' + '.join(map(str, divisors))}")
    else:
        print(f"{n} is NOT perfect.")
