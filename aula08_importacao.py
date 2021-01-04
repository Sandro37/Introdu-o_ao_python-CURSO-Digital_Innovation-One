#lidando com módulos, importação de classes, métodos
# e construção de funções anônimas
from aula07_televisao import Televisao
from aula07_calculadora2 import Calculadora
from aula08_contador_letras import contador_letras, teste

if __name__ == '__main__':
    tv = Televisao()
    print(tv.ligada)
    tv.power()
    print(tv.ligada)

    calculadora = Calculadora(5,10)
    print(calculadora.soma())

    lista = ['cachorro', 'gato', 'elefante', 'leão']
    total_letras = contador_letras(lista)
    print('Total de letras por palavras de lista: {}'.format(total_letras))
    print(teste())