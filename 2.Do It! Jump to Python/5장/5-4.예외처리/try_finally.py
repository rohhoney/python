try:
    f = open('foo.txt', 'w')
    f.write("hi")

finally:
    f.close()
