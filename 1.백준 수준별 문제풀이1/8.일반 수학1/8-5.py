#벌집
N = int(input())
hive = []
floor = 1
floor_max = 0

while N > floor_max:
    floor_max = 1 + 6 * (floor*(floor-1))/2
    floor += 1

print(floor-1)