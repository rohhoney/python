#using // to find quotient.

a = 5//3
b = 5/3
c = 5%3
print(a,b,c)

#using 'and', 'or' instead of '&&', '||'

for i in range(5):
    if i == 1 or i== 3:
        print("1")

#using 'i' again is ok. Because i in loop is local variable.
for i in range(5):
    if i == 2 or i == 3:
        print("2")
