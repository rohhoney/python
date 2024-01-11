def count_croatian_alphabets(word):
    croatian_alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    count = 0
    i = 0

    while i < len(word):
        if i + 2 < len(word) and word[i:i + 3] in croatian_alphabets:
            count += 1
            i += 3
        elif i + 1 < len(word) and word[i:i + 2] in croatian_alphabets:
            count += 1
            i += 2
        else:
            count += 1
            i += 1

    return count

# 입력 받기
word = input().strip()

# 결과 출력
print(count_croatian_alphabets(word))
