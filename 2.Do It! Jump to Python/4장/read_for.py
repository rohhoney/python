f = open("새파일.txt", 'r')
for line in f:
    print(line.strip())
f.close()