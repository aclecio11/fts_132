# Bibliotecas:

import pytest  # Framework de Teste  unitario - Engine
import requests  # Framework de Teste de API - Requests / Responses

# Endereço da API:
base_url = 'https://petstore.swagger.io/v2/pet'
headers = {'Content-Type': 'application/json'}  # Nos .asmx seria 'text/xml'


def teste_criar_pet():
    # 1 Configura: dados de entrada vem do json
    status_code_esperado = 200
    id_pet_esperado = 10111
    categoria_esperada = {'id': 1, 'name': 'cachorro'}
    nome_pet_esperado = 'chocolate'
    url_esperada = ['https://static.vix.com/pt/sites/default/files/f/foto-concurso-cachorro-nao-usar-11-0718-1400x1080.jpg']
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
    assert corpo_da_resposta['id'] == id_pet_esperado
    assert corpo_da_resposta['category'] == categoria_esperada
    assert corpo_da_resposta['name'] == nome_pet_esperado
    assert corpo_da_resposta['photoUrls'] == url_esperada
    assert corpo_da_resposta['tags'] == tag_esperada
    assert corpo_da_resposta['status'] == status_esperado

#######################################################################