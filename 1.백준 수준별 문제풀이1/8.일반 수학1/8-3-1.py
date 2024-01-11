#거스름돈 문제

quarter = 25
dime = 10
nickel = 5
penny = 1

T = int(input())    #test case

whole = []

for _ in range(T):
    coin = []
    charge = int(input())

    num_q = charge // quarter
    charge %= quarter
    coin.append(num_q)

    num_d = charge // dime
    charge %= dime
    coin.append(num_d)

    num_n = charge // nickel
    charge %= nickel
    coin.append(num_n)

    coin.append(charge)

    whole.append(coin)
for i in range(T):
    print(*whole[i])
