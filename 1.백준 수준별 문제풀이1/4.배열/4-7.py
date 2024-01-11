students =[]
for i in range(30):
    students.append(i+1)
for j in range(28):
    students.remove(int(input()))
print(students[0])
print(students[1])
