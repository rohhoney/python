#수학도둑 달팽이

A, B, V = map(int,input().split())

now_position = 0
oneday_move = A -B
Day = ((V - A) // oneday_move)

if (V-A) % oneday_move == 0:
    print(Day + 1)
else:
    print(Day + 2)