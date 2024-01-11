def count_repaint(board, start_i, start_j):
    repaint_count = 0
    for i in range(start_i, start_i + 8):
        for j in range(start_j, start_j + 8):
            if (i + j) % 2 == 0:  # 검은색(시작점이 흰색)과 흰색(시작점이 검은색) 체스판 패턴 비교 #체스판 패턴일땐 이 방법을 쓰면 좋다!
                if board[i][j] == 'W':
                    repaint_count += 1
            else:
                if board[i][j] == 'B':
                    repaint_count += 1
    return min(repaint_count, 64 - repaint_count)  # 시작점이 흰색인 경우와 검은색인 경우 중 최소값 반환


N, M = map(int, input().split())
board = [input() for _ in range(N)]

min_repaint = float('inf')

for i in range(N - 7):
    for j in range(M - 7):
        min_repaint = min(min_repaint, count_repaint(board, i, j))

print(min_repaint)
