#영수증 문제
total_price = int(input())
type_nums = int(input())
total = 0

i = 1
list1 = []
while i <= type_nums: #using 'for' is more convenient
    product_price, product_num = map(int,input().split())
    products_price = product_price * product_num
    list1.append(products_price)
    i += 1

for a in list1:
    total += a
if total == total_price:
    print("Yes")
else:
    print("No")

