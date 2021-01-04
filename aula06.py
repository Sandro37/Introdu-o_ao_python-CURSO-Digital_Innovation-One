#organizando conjuntos e subconjuntos de elementos em python

#não permite duplicidade
conjunto = {1,2,3,4,4}

print(type(conjunto))

conjunto.add(5)

#remover elemento
conjunto.discard(2)

print('Conjunto: {}'.format(conjunto))

print('_________________________________')

conjunto1 = {1,2,3,4,5}
conjunto2 = {5,6,7,8}

conjuntoUniao = conjunto1.union(conjunto2)

print('Conjunto união: {}'.format(conjuntoUniao))

conjuntoInterseccao = conjunto1.intersection(conjunto2)
print('Conjunto intersecção: {}'.format(conjuntoInterseccao))

conjuntoDiferenca1 = conjunto1.difference(conjunto2)
conjuntoDiferenca2 = conjunto2.difference(conjunto1)
print('Conjunto diferença 1 para 2: {}'.format(conjuntoDiferenca1))
print('Conjunto direfenla 2 para 1: {}'.format(conjuntoDiferenca2))

conjunto_diff_simetrica = conjunto1.symmetric_difference(conjunto2)
print('Diferença simetrica: {}'.format(conjunto_diff_simetrica))

conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5}

conjunto_subset = conjunto_a.issubset(conjunto_b)
print('A é subConjunto de B: {}'.format(conjunto_subset))

conjunto_superSet = conjunto_b.issuperset(conjunto_a)
print('B é Super Conjunto de A: {}'.format(conjunto_superSet))

#Tirando duplicidade lista

lista = ['cachorro','cachorro', 'gato', 'gato', 'elefante']
print(lista)

conjunto_animais = set(lista)
print(conjunto_animais)

lista_animais = list(conjunto_animais)
print(lista_animais)


conjun = {10,20,30,40,50}
conjun.discard(40)
print("CONJUN = {}".format(conjun))

