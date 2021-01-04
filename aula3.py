#Como criar um código em Python que funcione
# de acordo com a relação das variáveis

a = int(input('Primeiro Valor:' ))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

if a > b and a > c:
    print('O maior número é {}'.format(a))
elif b > a and b > c:
    print('O maior número é {}'.format(b))
else:
    print('O maior número é {}'.format(c))

print('Final do Programa...')



a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))

if (a % 2 == 0) or (not b % 2 > 0):
    print('Foi digitado um número par!')
else:
    print('Nenhum número par digitado!')


a = int(input('1 Bimestre: '))
if a > 10:
    a = int(input("Você digitou Errado. 1 Bimestre:"))
b = int(input('2 Bimestre: '))
if b > 10:
    b = int(input("Você digitou Errado. 2 Bimestre:"))
c = int(input('3 Bimestre: '))
if c > 10:
    c = int(input("Você digitou Errado. 3 Bimestre:"))
d = int(input('4 Bimestre: '))
if d > 10:
    d = int(input("Você digitou Errado. 4 Bimestre:"))

media = (a + b + c + d) / 4
print('Media = {}'.format(media))

if a <= 10 and b <= 10 and c <= 10 and d <= 10:

    print('Media = {}'.format(media))
else:
    print('foi informado alguma nota errada!')

