def triple_6(a):
    a = list(map(int, a))
    checker = 0
    for i in range(len(a)-2):
        if a[i] == a[i+1] == a[i+2] == 6:
            checker = 1
            break
    
    if checker == 0:
        return 0
    else:
        return 1


#main

N = int(input())

i = 665
cnt = 0
while True:
    i += 1
    i = str(i)
    cnt += triple_6(list(i))
    if cnt == N:
        break
    i = int(i)
print(int(i))