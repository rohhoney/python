

W = input()

numlist = []
for char in W:
    if char in 'ABC':
        numlist.append(3)
    elif char in 'DEF':
        numlist.append(4)
    elif char in 'GHI':
        numlist.append(5)
    elif char in 'JKL':
        numlist.append(6)
    elif char in 'MNO':
        numlist.append(7)
    elif char in 'PQRS':
        numlist.append(8)
    elif char in 'TUV':
        numlist.append(9)
    elif char in 'WXYZ':
        numlist.append(10)

print(sum(numlist))