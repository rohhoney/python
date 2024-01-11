#그룹단어 개수 찾기

def find_group_word(w):
    wlist = list(w)
    ban_list = []

    for i in range(len(wlist)-1):
        if wlist[i] == wlist[i+1]:
            pass
        else:
            ban_list.append(wlist[i])
            if wlist[i+1] in ban_list:
                return 0
    return 1

N = int(input())
cnt = 0

for i in range(N):
    word = input()
    cnt += find_group_word(word)

print(cnt)

#gpt도 거의 똑같이 했다