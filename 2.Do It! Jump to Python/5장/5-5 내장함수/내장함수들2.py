#divmod 몫과 나머지 튜플리턴
print("divmod(7, 3):", divmod(7, 3))

#enumerate 순서가 있는 데이터를 입력받아 인덱스 값을 포함하는 enumerate 객체 리턴
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)
print("dict(enumerate(['body', 'foo', 'bar'])):", dict(enumerate(['body', 'foo', 'bar'])))

#eval 문자열인 표현식 계산값 리턴
print("eval('1+2'):", eval("eval('1+2')"))