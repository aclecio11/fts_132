import pytest

from main import somar_dois_numeros, subtrair_dois_numeros, multiplicar_dois_numeros, dividir_dois_numeros, \
    elevar_um_numero_ao_outro, calcular_area_de_um_triangulo, calcular_area_de_um_retangulo, \
    calcular_area_de_um_quadrado


def testar_somar_dois_numeros():
    # 1ª Etapa - Configura / Prepara
    #Dados / Valores
    #Entradas / Input
    a = 8
    b = 9
    #Saída / Output
    resultado_esperado = 17

    # 2ª Etapa: Executa
    resultado_atual = somar_dois_numeros(a, b)

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
    resultado_atual = subtrair_dois_numeros(a, b)

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
    resultado_atual = multiplicar_dois_numeros(a, b)

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
    resultado_atual = dividir_dois_numeros(a, b)

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
    resultado_atual = elevar_um_numero_ao_outro(a, b)

    # 3ª Etapa: Confirma / Check / Valida
    assert resultado_atual == resultado_esperado

def testar_calcular_area_de_um_triangulo():
    # 1ª Etapa - Configura / Prepara
    #Dados / Valores
    #Entradas / Input
    B = 10
    h = 5
    #Saída / Output
    resultado_esperado = 25

    # 2ª Etapa: Executa
    resultado_atual = calcular_area_de_um_triangulo(B, h)

    # 3ª Etapa: Confirma / Check / Valida
    assert resultado_atual == resultado_esperado

def testar_calcular_area_de_um_retangulo():
    # 1ª Etapa - Configura / Prepara
    #Dados / Valores
    #Entradas / Input
    B = 6
    h = 8
    #Saída / Output
    resultado_esperado = 48

    # 2ª Etapa: Executa
    resultado_atual = calcular_area_de_um_retangulo(B, h)

    # 3ª Etapa: Confirma / Check / Valida
    assert resultado_atual == resultado_esperado

def testar_calcular_area_de_um_quadrado():
    # 1ª Etapa - Configura / Prepara
    #Dados / Valores
    #Entradas / Input
    l = 9
    #Saída / Output
    resultado_esperado = 81

    # 2ª Etapa: Executa
    resultado_atual = calcular_area_de_um_quadrado(l)

    # 3ª Etapa: Confirma / Check / Valida
    assert resultado_atual == resultado_esperado