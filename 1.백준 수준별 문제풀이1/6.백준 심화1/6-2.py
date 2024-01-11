real_pieces = [1,1,2,2,2,8]
ddpeices = list(map(int, input().split()))

result = []

for _ in range(6):
    a = real_pieces[_] - ddpeices[_]
    result.append(a)

print(*result)
