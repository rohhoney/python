import itertools

for i in itertools.permutations('abcd'):
    print(''.join(i), end=', ')

print("\b\b")