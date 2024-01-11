#Chess_board list
W_chess_board = [list('WBWBWBWB'),
                 list('BWBWBWBW'),
                 list('WBWBWBWB'),
                 list('BWBWBWBW'),
                 list('WBWBWBWB'),
                 list('BWBWBWBW'),
                 list('WBWBWBWB'),
                 list('BWBWBWBW'),]

B_chess_board = [list('BWBWBWBW'),
                 list('WBWBWBWB'),
                 list('BWBWBWBW'),
                 list('WBWBWBWB'),
                 list('BWBWBWBW'),
                 list('WBWBWBWB'),
                 list('BWBWBWBW'),
                 list('WBWBWBWB'),]

#function def
def Min_Modifi(a):
    W_count = 0
    B_count = 0

    for i in range(8):
        for j in range(8):
            if a[i][j] != W_chess_board[i][j]:
                W_count += 1
        for j in range(8):
            if a[i][j] != B_chess_board[i][j]:
                B_count += 1
    if W_count > B_count:
        return B_count
    else:
        return W_count

#Main

M, N = map(int, input().split())
chess_list = [list(input()) for _ in range(M)]

min_change = -1

for i in range(M-7):
    for j in range(N-7):
        now_list = []
        for k in range(i, i+8):
            m = [chess_list[k][l] for l in range(j, j+8)]
            now_list.append(m)
        now_min = Min_Modifi(now_list)
        if min_change == -1:
            min_change = now_min
        else:
            if now_min <= min_change:
                min_change = now_min

print(min_change)
