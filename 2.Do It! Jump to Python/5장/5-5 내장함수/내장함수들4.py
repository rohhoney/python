#hex() 16진수 문자열 리턴
print('hex(234):', hex(234))

#id() 객체 주솟값 리턴
print("id()함수사용")
a = 3
print(id(3))
print(id(a))
b = a
print(id(b))
print("다른 객체 id()함수")
print(id(4))

# int()
print('int("11",2):', int('11', 2))

#isinstance 객체가 특정 class의 인스턴스인지 확인
class Person: pass

a = Person()

print('isinstance(a, Person):', isinstance(a, Person))

print("oct(34):", oct(34))


#round(number[,ndigits])
print('round(3.6):', round(3.6))
print('int(3.6):', int(3.6))
print("round(3.13412341,2):", round(3.13412341,2) )

#tuple => 튜플로 변환
print("tuple([1,2,3]):", tuple([1,2,3]))

#type
print('type("abe"):', type("abe") )

#zip 동일한 개수로 이루어진 데이터들을 묶어서 리턴하는 함수이다.

print("list(zip([1, 2, 3], [4, 5, 6])):", list(zip([1, 2, 3], [4, 5, 6])))
print("list(zip('abc','def')): ", list(zip("abc","def")))

