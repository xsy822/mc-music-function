with open('faded1.txt', 'r') as fp:
    a = fp.read()
    a = a.split(' ')
    b = a[8:]
    for index, i in enumerate(b):
        if i != '\n' and i[0] != 'd':
            b[index] = str(int(i)+6)
    a = a[:8]
with open('faded1.txt', 'w') as fp:
    c = a + b
    print(c)
    c = ' '.join(c)
    fp.write(c)
