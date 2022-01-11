# Bibliotecas:

import pytest  # Framework de Teste  unitario - Engine
import requests  # Framework de Teste de API - Requests / Responses



# Endereço da API:
base_url = 'https://petstore.swagger.io/v2/user'
headers = {'Content-Type': 'application/json'}  # Nos .asmx seria 'text/xml'


# Os testes:
def test_criar_usuario():
    # Configura:
    status_code_esperado = 200
    code_esperado = 200
    type_esperado = 'unknown'
    mensagem_esperada = '1011'

    # Executa:
    resposta = requests.post(  # Faz a requisição ,passando:
        url=base_url,  # o end point da API
        data=open('C:/Users/aclecio11/PycharmProjects/fts_132/test/db/user1.json', 'rb'),  # O body JSON
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

def testar_consultar_usuario():
    # 1 configura:
    status_code = 200
    id = 1011
    username = "aclecio"
    firstName = "aclecio"
    lastName = "pereira"
    email = "aclecio@test.com"
    password = "123456"
    phone = "83998244271"
    userStatus = 0

    # 2 Executa:
    resposta = requests.get(  # Faz a requisição ,passando:
        url=f'{base_url}/{username}',  # o end point da API
        headers=headers  # O header com o Content type
    )

    # 3 Formatação:
    match resposta.status_code:
        case 200:
            corpo_da_resposta = resposta.json()
            print(resposta)  # Resposta bruta
            print(resposta.status_code)  # Status code
            print(corpo_da_resposta)  # Resposta formatada

            # 4 Valida:
            assert resposta.status_code == status_code
            assert corpo_da_resposta['id'] == id
            assert corpo_da_resposta['username'] == username
            assert corpo_da_resposta['firstName'] == firstName
            assert corpo_da_resposta['lastName'] == lastName
            assert corpo_da_resposta['email'] == email
            assert corpo_da_resposta['password'] == password
            assert corpo_da_resposta['phone'] == phone
            assert corpo_da_resposta['userStatus'] == userStatus
        case 400:
            print('username fornecido incorretamente')
        case 404:
            print('usuario não encontrado')


##################################################################################

def testar_alterar_usuario():
    # Configura:
    username = 'aclecio'
    status_code_esperado = 200
    code_esperado = 200
    type_esperado = 'unknown'
    mensagem_esperada = '1011'

    # Executa:
    resposta = requests.put(  # Faz a requisição ,passando:
        url=f'{base_url}/{username}',  # o end point da API
        data=open('C:/Users/aclecio11/PycharmProjects/fts_132/test/db/user2.json', 'rb'),  # O body JSON
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


def testar_excluir_usuario():
    # Configura:
    username = 'aclecio'
    status_code_esperado = 200
    code_esperado = 200
    type_esperado = 'unknown'
    mensagem_esperada = 'aclecio'

    # Executa:
    resposta = requests.delete(  # Faz a requisição ,passando:
        url=f'{base_url}/{username}',  # o end point da API
        headers=headers  # O header com o Content type
    )
    # Formatação:
    match resposta.status_code: # nao usar
        case 200:      # Apagar um usuario encontrado
            corpo_da_resposta = resposta.json()
            print(resposta)  # Resposta bruta
            print(resposta.status_code)  # Status code
            print(corpo_da_resposta)  # Resposta formatada

            # Valida:
            assert resposta.status_code == status_code_esperado

            assert corpo_da_resposta['code'] == code_esperado
            assert corpo_da_resposta['type'] == type_esperado
            assert corpo_da_resposta['message'] == mensagem_esperada
        case 400: # na pratica nao usar match e case:
            print('username fornecido incorretamente')
        case 404:
            print('usuario não encontrado')
##################################################################################

def testar_login_do_usuario():
    #1 Configura:
    username = 'aclecio'
    password = '123456'
    status_code_esperado = 200
    code_esperado = 200
    type_esperado = 'unknown'
    inicio_mensagem_esperada = 'logged in user session:'

    #2 Executa:
    resposta = requests.get(
        url=f'{base_url}/login?username={username}&password={password}',
        headers=headers
    )
    #3 Formata:
    corpo_da_resposta = resposta.json()
    print(resposta)  # Resposta bruta
    print(resposta.status_code)  # Status code
    print(corpo_da_resposta)  # Resposta formatada

    #4 Valida:
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == code_esperado
    assert corpo_da_resposta['type'] == type_esperado
    #assert corpo_da_resposta['message'] == inicio_mensagem_esperada
    assert 'logged in user session:' in inicio_mensagem_esperada

    #5 Extrair uma informação da mensagem 'logged in user session:'
    mensagem_recebida = corpo_da_resposta['message']
    token_usuario = mensagem_recebida[23:37]
    print(f'O token do usuario eh: {token_usuario}')

