#분수
N = int(input())
hive = []
floor = 0
floor_max = 0

while N > floor_max:
    floor += 1
    floor_max = (floor*(floor+1))/2


differ = floor_max - N

if floor % 2 == 0:
    print("%d/%d" % (floor-differ, 1+differ))
else:
    print("%d/%d" % (1+differ, floor-differ))