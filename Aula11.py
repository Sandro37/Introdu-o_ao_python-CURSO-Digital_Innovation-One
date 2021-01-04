#Gerenciando e criando exceções customizadas com try, except
# else e finally
if __name__ == '__main__':

    lista = [1,10]

    try:
        arquivo = open('media.txt', 'r')
        div = 14/0
        print(div)

        num = lista[1]
        
    except ZeroDivisionError:
        print('Não é possível realizar uma divisão por 0')
    except ArithmeticError:
        print('Houve um erro ao realizar uma operação aritmética')
    except IndexError:
        print('ìndice da lista passado não existe')
    except Exception as ex:
        print('Erro desconhecido. Erro: {}'.format(ex))
    else:
        print('Exercuta quando não ocorre nenhuma exceção')
    finally:
        print('Executa sempre')
        arquivo.close()
