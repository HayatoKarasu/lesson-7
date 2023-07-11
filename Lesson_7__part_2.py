pro = str(input("Напишите любое предложение: "))

a = len(pro)

if a <= 1000:
    b = pro.split(' ')
    c = (''.join(b))
    d = len(c)
    e = a - d

    print(' ' * e + c)
    
else:
    print("no")
