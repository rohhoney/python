#gpt의 답
def dial_time(char):
    dial_numbers = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    for i, dial in enumerate(dial_numbers):
        if char in dial:
            return i + 3

def minimum_time(word):
    total_time = 0
    for char in word:
        total_time += dial_time(char)
    return total_time

# 입력 예시
word = input().upper()

# 출력 예시
print(minimum_time(word))