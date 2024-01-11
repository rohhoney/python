#gpt의 답
def find_most_frequent_alphabet(word):
    word = word.upper()  # 입력 단어를 모두 대문자로 변환
    alphabet_count = {}  # 알파벳 빈도를 저장할 딕셔너리

    # 각 알파벳의 빈도를 세기
    for char in word:
        if char.isalpha():  # 알파벳인 경우만 처리
            alphabet_count[char] = alphabet_count.get(char, 0) + 1

    # 빈도가 가장 높은 알파벳 찾기
    max_count = max(alphabet_count.values())
    most_frequent_alphabets = [char for char, count in alphabet_count.items() if count == max_count]

    if len(most_frequent_alphabets) == 1:
        return most_frequent_alphabets[0]  # 가장 빈도가 높은 알파벳이 1개인 경우
    else:
        return '?'  # 가장 빈도가 높은 알파벳이 여러 개인 경우

# 입력 받기
word = input().strip()

# 결과 출력
print(find_most_frequent_alphabet(word))
