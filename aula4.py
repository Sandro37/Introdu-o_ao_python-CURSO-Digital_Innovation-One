#Como criar laços de repetições em python

num = int(input('Entre com um número: '))
div = 0
for i in range(1, num+1):
    resto = num % i
    print(i,resto)
    if resto == 0:
       div += 1

if div == 2:
    print('Numero {} é primo'.format(num))
else:
    print('Numero {} não é primo'.format(num))


a = int(input('Entre com um valor: '))

for num in range(a + 1):
    div = 0
    for i in range(1, num + 1):
        resto = num % i
        if resto == 0:
            div += 1

    if div == 2:
        print(num)




while a < 10:
    print(a)
    a += 1


a = int(input('1 Bimestre: '))
while a > 10:
    a = int(input("Você digitou Errado. 1 Bimestre:"))
b = int(input('2 Bimestre: '))
while b > 10:
    b = int(input("Você digitou Errado. 2 Bimestre:"))
c = int(input('3 Bimestre: '))
while c > 10:
    c = int(input("Você digitou Errado. 3 Bimestre:"))
d = int(input('4 Bimestre: '))
while d > 10:
    d = int(input("Você digitou Errado. 4 Bimestre:"))

media = (a + b + c + d) / 4
print('Media = {}'.format(media))