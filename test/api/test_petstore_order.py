# Bibliotecas:

import pytest  # Framework de Teste  unitario - Engine
import requests  # Framework de Teste de API - Requests / Responses

# Endereço da API:
base_url = 'https://petstore.swagger.io/v2/store/order'
headers = {'Content-Type': 'application/json'}  # Nos .asmx seria 'text/xml'


def teste_criar_order():
    # 1 Configura: dados de entrada vem do json
    status_code_esperado = 200
    order_id_esperado = 5
    pet_id_esperado = 10111
    quantity_esperado = 1
    shipDate_esperado = '2022-01-12T00:54:52.111+0000'
    status_esperado = 'placed'
    complete_esperado = True

    # 2 Executa:
    resposta = requests.post(  # Faz a requisição ,passando:
        url=base_url,  # o end point da API
        data=open('C:/Users/aclecio11/PycharmProjects/fts_132/test/db/order1.json', 'rb'),  # O body JSON
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
    assert corpo_da_resposta['id'] == order_id_esperado
    assert corpo_da_resposta['petId'] == pet_id_esperado
    assert corpo_da_resposta['quantity'] == quantity_esperado
    assert corpo_da_resposta['shipDate'] == shipDate_esperado
    assert corpo_da_resposta['status'] == status_esperado
    assert corpo_da_resposta['complete'] == complete_esperado

#######################################################################

def testar_consultar_order():
    # 1 configura:
    status_code_esperado = 200
    order_id_esperado = 5
    pet_id_esperado = 10111
    quantity_esperado = 1
    shipDate_esperado = '2022-01-12T00:54:52.111+0000'
    status_esperado = 'placed'
    complete_esperado = True

    # 2 Executa:
    resposta = requests.get(  # Faz a requisição ,passando:
        url=f'{base_url}/{order_id_esperado}',  # o end point da API
        headers=headers  # O header com o Content type
    )

    # 3 Formatação:

    corpo_da_resposta = resposta.json()
    print(resposta)  # Resposta bruta
    print(resposta.status_code)  # Status code
    print(corpo_da_resposta)  # Resposta formatada

    # 4 Valida:
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['id'] == order_id_esperado
    assert corpo_da_resposta['petId'] == pet_id_esperado
    assert corpo_da_resposta['quantity'] == quantity_esperado
    assert corpo_da_resposta['shipDate'] == shipDate_esperado
    assert corpo_da_resposta['status'] == status_esperado
    assert corpo_da_resposta['complete'] == complete_esperado


##################################################################################

def testar_excluir_order():
    # Configura:
    status_code_esperado = 200
    order_id_esperado = 5
    code_esperado = 200
    type_esperado = 'unknown'
    mensagem_esperada = '5'

    # Executa:
    resposta = requests.delete(  # Faz a requisição ,passando:
        url=f'{base_url}/{order_id_esperado}',  # o end point da API
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