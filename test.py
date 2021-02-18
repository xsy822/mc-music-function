with open('star2.txt', 'r') as fp:
    a = fp.read()
    a = a.split()
    b = a[7:]
    for index, i in enumerate(b):
        if i[0] != 'd':
            b[index] = str(int(i)+17)
    a = a[:7]
with open('star2.txt', 'w') as fp:
    c = a + b
    print(c)
    c = ' '.join(c)
    fp.write(c)
