if __name__ == '__main__':
      contador_letras = lambda lista: [len(x) for x in lista]

      lista_animais = ['cachorro','gato','leão', 'elefante']
      print(contador_letras(lista_animais))

      soma = lambda a, b: a + b
      subtracao = lambda a, b: a - b
      multiplicacao = lambda a, b: a * b
      divisao = lambda a, b: a / b

      print(soma(5,3))
      print(subtracao(10,5))
      print(multiplicacao(5,5))
      print(divisao(5,5))

      calculadora = {
          'soma': lambda a, b: a + b,
          'subtracao': lambda a, b: a - b,
          'multiplicacao': lambda a, b: a * b,
          'divisao': lambda a, b: a / b
      }

      print(type(calculadora))
      multiplicacao = calculadora['multiplicacao']
      subtracao = calculadora['subtracao']
      div = calculadora['divisao']

      print('soma = {}'.format(soma(5,5)))
      print('multiplicaçao = {}'.format(multiplicacao(5,5)))
      print('subtração = {}'.format(subtracao(10,5)))
      print('Divisão = {}'.format(div(10,2)))