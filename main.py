import pytest
    #FUNÇÕES( cozinheiro):
def somar_dois_numeros(a,b):
    return a + b

def subtrair_dois_numeros(a, b):
    return a - b

def multiplicar_dois_numeros(a, b):
    return a * b

def dividir_dois_numeros(a, b):
    return a / b

def elevar_um_numero_ao_outro(a, b):
        return a ** b


    #CHAMADAS(garçom):
if __name__ == '__main__':

       resultado = somar_dois_numeros(89,8)
       print(f'A soma é {resultado}')

       resultado = subtrair_dois_numeros(59, 17)
       print(f'A subtração é {resultado}')

       resultado = multiplicar_dois_numeros(145, 15)
       print(f'A multiplicação é {resultado}')

       resultado = dividir_dois_numeros(365, 5)
       print(f'A divisão é {resultado}')

       resultado = elevar_um_numero_ao_outro(3, 4)
       print(f'A exponenciação é {resultado}')

    #Teste( degustador):
def testar_somar_dois_numeros():
    # 1ª Etapa - Configura / Prepara
    #Dados / Valores
    #Entradas / Input
    a = 8
    b = 9
    #Saída / Output
    resultado_esperado = 17

    # 2ª Etapa: Executa
    resultado_atual = somar_dois_numeros(a,b)

    # 3ª Etapa: Confirma / Check / Valida
    assert resultado_atual == resultado_esperado

def testar_subtrair_dois_numeros():
    # 1ª Etapa - Configura / Prepara
    #Dados / Valores
    #Entradas / Input
    a = 100
    b = 47
    #Saída / Output
    resultado_esperado = 53

    # 2ª Etapa: Executa
    resultado_atual = subtrair_dois_numeros(a,b)

    # 3ª Etapa: Confirma / Check / Valida
    assert resultado_atual == resultado_esperado

def testar_multiplicar_dois_numeros():
    # 1ª Etapa - Configura / Prepara
    #Dados / Valores
    #Entradas / Input
    a = 10
    b = 47
    #Saída / Output
    resultado_esperado = 470

    # 2ª Etapa: Executa
    resultado_atual = multiplicar_dois_numeros(a,b)

    # 3ª Etapa: Confirma / Check / Valida
    assert resultado_atual == resultado_esperado

def testar_dividir_dois_numeros():
    # 1ª Etapa - Configura / Prepara
    #Dados / Valores
    #Entradas / Input
    a = 100
    b = 10
    #Saída / Output
    resultado_esperado = 10

    # 2ª Etapa: Executa
    resultado_atual = dividir_dois_numeros(a,b)

    # 3ª Etapa: Confirma / Check / Valida
    assert resultado_atual == resultado_esperado

def testar_elevar_um_numero_ao_outro():
    # 1ª Etapa - Configura / Prepara
    #Dados / Valores
    #Entradas / Input
    a = 2
    b = 3
    #Saída / Output
    resultado_esperado = 8

    # 2ª Etapa: Executa
    resultado_atual = elevar_um_numero_ao_outro(a,b)

    # 3ª Etapa: Confirma / Check / Valida
    assert resultado_atual == resultado_esperado

