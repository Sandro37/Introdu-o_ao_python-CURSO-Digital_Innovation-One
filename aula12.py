#instalando e utilizando pacotes em python e realizar
# requisições com requests
import requests



def retorna_dados_cep(cep):
    resposta = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    print(resposta.status_code)
    print(resposta.json())
    print(type(resposta.json()))
    dados_cep = resposta.json()

    print(dados_cep['logradouro'])
    print(dados_cep['bairro'])
    return dados_cep


def retorna_dados_pokemon(pokemon):
    resposta = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = resposta.json()
    return dados_pokemon


def retorna_response(url):
    resposta = requests.get(url)
    return resposta.text

if __name__ == '__main__':
    # retorno = retorna_dados_cep('13188200')
    # print(retorno['cep'])

    dados_pokemon = retorna_dados_pokemon('pikachu')
    print(dados_pokemon['species']['url'])
    print(dados_pokemon['sprites']['front_shiny'])

    #resposta_url = retorna_response('https://www.dextra.com.br/')
    #print(resposta_url)