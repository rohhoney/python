function1 = '''
def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result
'''

#간단버전
function2 = '''
def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

'''

#lambda use

print(list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6])))