#Gere, copie, mova, escreva e leia informações de arquivos externos

def escrever_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'w')
    arquivo.write(str(texto) + '\n')
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(str(texto) + '\n')
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read().split('\n')
    aluno_nota.pop()
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print('Aluno: {}\n'
              'lista de notas: {}\n'
              'Media: {}\n'.format(aluno, lista_notas, media(lista_notas)))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

def salvar_media_aluno(nome_arquivo, lista_media):
    arquivo = open(nome_arquivo, 'a')
    for i in lista_media:
        arquivo.write(str(i) + '\n')
    arquivo.close()


def pedir_aluno_nota():
    nota = []
    notas = ''
    nome_aluno = input('Nome do Aluno:')
    for i in range(4):
        nota.append(int(input('Nota do {} Bimestre:'.format(i+1))))

    for i in nota:
        notas+= ',' + str(i)
    aluno = str(nome_aluno) + str(notas)
    print(aluno)
    atualizar_arquivo('notas.txt', aluno)

if __name__ == '__main__':
    # aluno = 'Ricardo, 10,9,6,7'
    # atualizar_arquivo('notas.txt', aluno)

    pedir_aluno_nota()
    lista_media = media_notas('notas.txt')
    print(lista_media)
    salvar_media_aluno('media.txt', lista_media)
