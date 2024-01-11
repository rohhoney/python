#메모리 잘 쓰는 법

#안좋은 예
import time

start_time = time.time()
a = list(range(100000))
a2 = list()

for i in a:
    a2.append(i*2)  #매번 메모리 재할당 되면서 효율이 나빠진다. for 문 안에서는 append()는 안쓰는게 좋다

end_time = time.time()
fin = end_time - start_time
print(fin)

#더 좋은 예

start_time = time.time()
temp = [x*2 for x in range(100000)] #리스트 컴프리헨션을 써서 메모리 재할당하는 일을 없애 메모리 활용도가 좋아졌다.
end_time = time.time()
fin = end_time - start_time
print(fin)

#베스트
start_time = time.time()
a = list(range(100000))
a2 = map(lambda n: n*2, a)  #map같은 파이썬 내부함수를 써서 더 좋아졌다. 효율적으로 모든 요소에 함수를 적용할 수 있게 된 것이다.
end_time = time.time()

fin = end_time - start_time
print(fin)
