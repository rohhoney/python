N = int(input())

List1 = [0 for _ in range(16)]
List1[0] = 2
for i in range(1, 16):
    List1[i] = List1[i - 1] + (List1[i - 1] - 1)

print(List1[N]**2)
