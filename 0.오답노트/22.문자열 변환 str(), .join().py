a = [1, 2, 3, 4, 5]
print(a)
print(str(a))   #list became str include []

# print(''.join(a))
print(list(str(a)))

b = [str(n) for n in a]
print(''.join(b))

print(' '.join("amazing"))