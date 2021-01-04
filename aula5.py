#como organizar os dados em uma lista ou tupla
# e realizar operações com elas


lista = [12,20,1,3,5,7]
lista_animal = ['cachorro', 'gato', 'elefante']

# print(lista_animal[1])

soma = 0
for x in lista:
    soma += x

print(soma)

print(sum(lista))
print(max(lista))
print(min(lista))

print(max(lista_animal))
print(min(lista_animal))

# nova_lista = lista_animal * 3
#
# print(nova_lista)


if 'gato' in lista_animal:
    print('Existe um gato na lista')
else:
    print('Não existe um gato na lista')

if 'lobo' in lista_animal:
    print('Existe um lobo na lista')
else:
    print('Não existe um lobo na lista. Será incluido')
    lista_animal.append('lobo')
    print(lista_animal)

lista_animal.pop()
print(lista_animal)

lista_animal.remove('elefante')
print(lista_animal)

#ordenando lista


lista_animal.sort()
lista.sort()

print(lista_animal)
print(lista)

# reverse
lista_animal.reverse()
lista.reverse()

print(lista_animal)
print(lista)

# tuplas (imutável)

tupla = (1,10,12,14,20,185)
print(len(tupla))

tupla_animal = tuple(lista_animal)

print(tupla_animal)

lista_numerica = list(tupla)

print(lista_numerica)

