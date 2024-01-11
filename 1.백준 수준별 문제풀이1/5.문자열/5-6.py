#알파벳 찾기
word = input()

positions = [-1] * 26  # 알파벳의 처음 등장 위치를 저장할 리스트 초기화

for i in range(len(word)):
    idx = ord(word[i]) - ord('a')  # 알파벳의 인덱스 계산
    if positions[idx] == -1:  # 해당 알파벳이 처음 등장하는 경우에만 위치 저장
        positions[idx] = i

for position in positions:
    print(position, end=' ')

