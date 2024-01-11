###format code###
a = 1234
b = 1.234
c = 'testing'

print("ingeter:%d\nfloat:%8.3f\nfloat2:%f\nfloat3:%-8.3f\nstring:%s" % (a,b,b,b,c))

###formating function###

#use number and string
print("i ate {0} apples".format(5))
print("i ate {0} apples".format('five'))
#use variable
number = 3
print("i ate {0} apples".format(number))

#use many {}
print("I ate {0} apples. so I was sick for {1} days.".format(10,3))

#use {name} instead of {number}({0},{1}, ...)
print("I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3))

#sort
print("{0:>10}".format("hi")) #right
print("{0:<10}".format("hi")) #left
print("{0:^10}".format("hi")) #middle

#fill spaces
print("{0:!<10}".format("hi"))

###f-string formating###

name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
print(f'나의 이름은 {name+"선생님"}입니다. 나이는 {age + 3}입니다.')

#use with dictionary
d = {'name':'홍길동', 'age':30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')