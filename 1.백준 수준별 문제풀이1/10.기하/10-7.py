a, b, c = 1, 1, 1
while True:
    a, b, c = map(int,input().split())
    if (a == 0 and b == 0 and c == 0):
        break
    elif a + b <= c or a + c <= b or b + c <= a:
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or a == c or b == c:
        print("Isosceles")
    else:
        print("Scalene")

