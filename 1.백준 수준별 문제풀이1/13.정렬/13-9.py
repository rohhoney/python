#1181번
#단어 정렬, 길이순->사전순

N = int(input())

w_list = [input() for _ in range(N)]
w_list = list(set(w_list))
w_list.sort(key=lambda x: (len(x), x))

for j in w_list:
    print(j)