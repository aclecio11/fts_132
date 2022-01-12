# Bibliotecas:

import pytest  # Framework de Teste  unitario - Engine
import requests  # Framework de Teste de API - Requests / Responses

# Endereço da API:
base_url = 'https://petstore.swagger.io/v2/pet'
headers = {'Content-Type': 'application/json'}  # Nos .asmx seria 'text/xml'


def teste_criar_pet():
    # 1 Configura: dados de entrada vem do json
    status_code_esperado = 200
    pet_id_esperado = 10111
    categoria_esperada = {'id': 1, 'name': 'cachorro'}
    pet_nome_esperado = 'chocolate'
    url_esperada = [
        'https://static.vix.com/pt/sites/default/files/f/foto-concurso-cachorro-nao-usar-11-0718-1400x1080.jpg']
    tag_esperada = [{'id': 2, 'name': 'vacinado'}]
    status_esperado = 'available'

    # 2 Executa:
    resposta = requests.post(  # Faz a requisição ,passando:
        url=base_url,  # o end point da API
        data=open('C:/Users/aclecio11/PycharmProjects/fts_132/test/db/pet1.json', 'rb'),  # O body JSON
        headers=headers  # O header com o Content type
    )
    # 3 Formata:
    corpo_da_resposta = resposta.json()
    print(resposta)  # Resposta bruta
    print(resposta.status_code)  # Status code
    print(corpo_da_resposta)  # Resposta formatada

    # 4 Valida:
    # asserts primários:
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['id'] == pet_id_esperado
    assert corpo_da_resposta['category'] == categoria_esperada
    assert corpo_da_resposta['name'] == pet_nome_esperado
    assert corpo_da_resposta['photoUrls'] == url_esperada
    assert corpo_da_resposta['tags'] == tag_esperada
    assert corpo_da_resposta['status'] == status_esperado


#######################################################################

def testar_consultar_pet():
    # 1 configura:
    status_code_esperado = 200
    pet_id_esperado = 10111
    categoria_esperada = {'id': 1, 'name': 'cachorro'}
    pet_nome_esperado = 'chocolate'
    url_esperada = [
        'https://static.vix.com/pt/sites/default/files/f/foto-concurso-cachorro-nao-usar-11-0718-1400x1080.jpg']
    tag_esperada = [{'id': 2, 'name': 'vacinado'}]
    status_esperado = 'available'

    # 2 Executa:
    resposta = requests.get(  # Faz a requisição ,passando:
        url=f'{base_url}/{pet_id_esperado}',  # o end point da API
        headers=headers  # O header com o Content type
    )

    # 3 Formatação:

    corpo_da_resposta = resposta.json()
    print(resposta)  # Resposta bruta
    print(resposta.status_code)  # Status code
    print(corpo_da_resposta)  # Resposta formatada

    # 4 Valida:
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['id'] == pet_id_esperado
    assert corpo_da_resposta['category'] == categoria_esperada
    assert corpo_da_resposta['name'] == pet_nome_esperado
    assert corpo_da_resposta['photoUrls'] == url_esperada
    assert corpo_da_resposta['tags'] == tag_esperada
    assert corpo_da_resposta['status'] == status_esperado


##################################################################################

def teste_alterar_pet():
    # 1 Configura: dados de entrada vem do json
    status_code_esperado = 200
    pet_id_esperado = 10111
    categoria_esperada = {'id': 1, 'name': 'cachorro'}
    pet_nome_esperado = 'chocolate'
    url_esperada = [
        'https://static.vix.com/pt/sites/default/files/f/foto-concurso-cachorro-nao-usar-11-0718-1400x1080.jpg']
    tag_esperada = [{'id': 3, 'name': 'reprodutor'}]
    status_esperado = 'available'

    # 2 Executa:
    resposta = requests.put(  # Faz a requisição ,passando:
        url=base_url,  # o end point da API
        data=open('C:/Users/aclecio11/PycharmProjects/fts_132/test/db/pet2.json', 'rb'),  # O body JSON
        headers=headers  # O header com o Content type
    )
    # 3 Formata:
    corpo_da_resposta = resposta.json()
    print(resposta)  # Resposta bruta
    print(resposta.status_code)  # Status code
    print(corpo_da_resposta)  # Resposta formatada

    # 4 Valida:
    # asserts primários:
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['id'] == pet_id_esperado
    assert corpo_da_resposta['category'] == categoria_esperada
    assert corpo_da_resposta['name'] == pet_nome_esperado
    assert corpo_da_resposta['photoUrls'] == url_esperada
    assert corpo_da_resposta['tags'] == tag_esperada
    assert corpo_da_resposta['status'] == status_esperado

#######################################################################

def testar_excluir_pet():
    # Configura:
    pet_id_esperado = 10111
    status_code_esperado = 200
    code_esperado = 200
    type_esperado = 'unknown'
    mensagem_esperada = '10111'

    # Executa:
    resposta = requests.delete(  # Faz a requisição ,passando:
        url=f'{base_url}/{pet_id_esperado}',  # o end point da API
        headers=headers  # O header com o Content type
    )
    # Formatação:

    corpo_da_resposta = resposta.json()
    print(resposta)  # Resposta bruta
    print(resposta.status_code)  # Status code
    print(corpo_da_resposta)  # Resposta formatada

    # Valida:
    assert resposta.status_code == status_code_esperado

    assert corpo_da_resposta['code'] == code_esperado
    assert corpo_da_resposta['type'] == type_esperado
    assert corpo_da_resposta['message'] == mensagem_esperada

##################################################################################