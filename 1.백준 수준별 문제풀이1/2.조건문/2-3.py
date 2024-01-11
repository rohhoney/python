#윤년 계산기
#4배수면이면서 100의 배수가 아니면 윤년, 또는 400의 배수면 윤년임

year = input()
year = int(year)

if year%100 == 0 and year%400 != 0:
    print("0")
elif year%4 == 0:
    print("1")
else:
    print("0")