def change(num):
    if num > 9:
        return chr(num + 55)
    return num


N, Radix = map(int,input().split())
a =[]
while N // Radix > 0:
    a.append(N % Radix)
    N = N // Radix
a.append(N)
a.reverse()

for i in a:
    print(change(i),end="")
