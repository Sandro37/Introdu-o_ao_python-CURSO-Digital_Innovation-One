#O que são variáveis e como manipulá-las através
# de operadores aritméticos e interação com o osuário

valorA = int(input("Entre com o primeiro valor: "))
valorB = int(input("Entre com o segundo valor: "))

soma = valorA +  valorB
subtracao = valorA - valorB
multiplicacao = valorA * valorB
divisao = valorA / valorB
restoDivisao = valorA % valorB

print(soma)
print(subtracao)
print(multiplicacao)
print(divisao)
print(restoDivisao)

print("soma: " + str(soma))

print("________________________________________")
print("Soma: {}".format(soma))
print("Substração: {}".format(subtracao))
print("Multiplicação: {}".format(multiplicacao))
print("Divisão: {}".format(divisao))
print("Resto da divisão: {}".format(restoDivisao))

print("________________________________________________________________")
x = '1'
soma2 = int(x) + 1
print("Soma convertida = {}".format(soma2))

print("________________________________________________________________")
print("soma: {soma}. \nSubtração: {sub}\nMultiplicacao: {multiplicacao}\nDivisão: {div}\nResto da Divisão: {resto}".format(soma=soma, sub=subtracao,multiplicacao=multiplicacao,div=divisao,resto=restoDivisao))