#GPT의
def calculate_black_area(papers):
    board = [[0] * 100 for _ in range(100)]

    for x, y in papers:
        for i in range(10):
            for j in range(10):
                board[x + i][y + j] = 1

    black_area = sum(sum(row) for row in board) #어차피 나머지 영역이 다 0 이니깐 1개수 세는게 아니라 다 더했음
    return black_area

# 입력 받기
N = int(input().strip())
papers = []
for _ in range(N):
    x, y = map(int, input().split())
    papers.append((x, y))

# 결과 출력
result = calculate_black_area(papers)
print(result)