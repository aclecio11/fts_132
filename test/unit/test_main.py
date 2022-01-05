import pytest

from main import somar_dois_numeros, subtrair_dois_numeros, multiplicar_dois_numeros, dividir_dois_numeros, \
    elevar_um_numero_ao_outro, calcular_area_de_um_triangulo, calcular_area_de_um_retangulo, \
    calcular_area_de_um_quadrado, calcular_area_de_um_circulo, calcular_volume_de_um_paralelograma


# anotação para usar como massa de teste
@pytest.mark.parametrize('a, b, resultado_esperado', [
        # valores:
        (-10, 5, -5),   # teste n°1 teste positivo
        (2, 5, 7),      # teste n°2
        (-10, 10, 0),   # teste n°3
        (40, 5, 45),    # teste n°4
        ('a', 'b', 'Falha de cálculo - dado digitado não é um número'),  # teste nº5 teste negativo
        (' ', '&', 'Falha de cálculo - dado digitado não é um número'),  # teste nº6
                                        ])

def testar_somar_dois_numeros(a, b, resultado_esperado):
    # 1ª Etapa - Configura / Prepara
    #Dados / Valores
    #Entradas / Input
    #a = 8
    #b = 9
    #Saída / Output
    #resultado_esperado = 17

    # 2ª Etapa: Executa
    resultado_atual = somar_dois_numeros(a, b)

    # 3ª Etapa: Confirma / Check / Valida
    assert resultado_atual == resultado_esperado

# anotação para usar como massa de teste
@pytest.mark.parametrize('a, b, resultado_esperado', [
        # valores:
        (10, 5, 5),  # teste n°1
        (2, 5, -3),  # teste n°2
        (10, 10, 0),  # teste n°3
        (40, 5, 35),  # teste n°4
        ('a', 'b', 'Falha de cálculo - dado digitado não é um número'),  # teste nº5
        (' ', '&', 'Falha de cálculo - dado digitado não é um número'),  # teste nº6
                                        ])

def testar_subtrair_dois_numeros(a, b, resultado_esperado):
    # 1ª Etapa - Configura / Prepara
    #Dados / Valores
    #Entradas / Input
    #a = 100
    #b = 47
    #Saída / Output
    #resultado_esperado = 53

    # 2ª Etapa: Executa
    resultado_atual = subtrair_dois_numeros(a, b)

    # 3ª Etapa: Confirma / Check / Valida
    assert resultado_atual == resultado_esperado

#anotação para usar como massa de teste
@pytest.mark.parametrize('a, b, resultado_esperado' ,[
    #valores:
            (10, 5, 50),  #teste n°1
            (2, 5, 10), #teste n°2
            (10, 4, 40), #teste n°3
            (40, 5, 200),  #teste n°4
            ('a', 'b', 'Falha de cálculo - dado digitado não é um número'), #teste nº5
            (' ','&','Falha de cálculo - dado digitado não é um número'), #teste nº6
                                ])

def testar_multiplicar_dois_numeros(a, b, resultado_esperado):
    # 1ª Etapa - Configura / Prepara
    #Dados / Valores
    #Entradas / Input
    #a = 10
    #b = 47
    #Saída / Output
    #resultado_esperado = 470

    # 2ª Etapa: Executa
    resultado_atual = multiplicar_dois_numeros(a, b)

    # 3ª Etapa: Confirma / Check / Valida
    assert resultado_atual == resultado_esperado

#anotação para usar como massa de teste
@pytest.mark.parametrize('a, b, resultado_esperado' ,[
    #valores:
            (100, 5, 20),  #teste n°1
            (2, 5, 0.4), #teste n°2
            (10, 4, 2.5), #teste n°3
            (40, 5, 8),  #teste n°4
            ('a', 'b', 'Falha de cálculo - dado digitado não é um número'), #teste nº5
            (' ','&','Falha de cálculo - dado digitado não é um número'), #teste nº6
                                ])

def testar_dividir_dois_numeros(a, b, resultado_esperado):
    # 1ª Etapa - Configura / Prepara
    #Dados / Valores
    #Entradas / Input
    #a = 100
    #b = 10
    #Saída / Output
    #resultado_esperado = 10

    # 2ª Etapa: Executa
    resultado_atual = dividir_dois_numeros(a, b)

    # 3ª Etapa: Confirma / Check / Valida
    assert resultado_atual == resultado_esperado

#anotação para usar como massa de teste
@pytest.mark.parametrize('a, b, resultado_esperado' ,[
    #valores:
            (1, 3, 1),  #teste n°1
            (2, 5, 32), #teste n°2
            (3, 4, 81), #teste n°3
            (4, 3, 64),  #teste n°4
            ('a', 'b', 'Falha de cálculo - dado digitado não é um número'), #teste nº5
            (' ','&','Falha de cálculo - dado digitado não é um número'), #teste nº6
                                ])

def testar_elevar_um_numero_ao_outro(a, b, resultado_esperado):
    # 1ª Etapa - Configura / Prepara
    #Dados / Valores
    #Entradas / Input
    #a = 2
    #b = 3
    #Saída / Output
    #resultado_esperado = 8

    # 2ª Etapa: Executa
    resultado_atual = elevar_um_numero_ao_outro(a, b)

    # 3ª Etapa: Confirma / Check / Valida
    assert resultado_atual == resultado_esperado

#anotação para usar como massa de teste
@pytest.mark.parametrize('B, h, resultado_esperado' ,[
    #valores:
            (6, 8, 24),  #teste n°1
            (4, 8, 16), #teste n°2
            (3, 4, 6), #teste n°3
            (4, 5, 10),  #teste n°4
            ('a', 'b', 'Falha de cálculo - dado digitado não é um número'), #teste nº5
            (' ','&','Falha de cálculo - dado digitado não é um número'), #teste nº6
                                ])

def testar_calcular_area_de_um_triangulo(B, h, resultado_esperado):
    # 1ª Etapa - Configura / Prepara
    #Dados / Valores
    #Entradas / Input
    #B = 10
   # h = 5
    #Saída / Output
    #resultado_esperado = 25

    # 2ª Etapa: Executa
    resultado_atual = calcular_area_de_um_triangulo(B, h)

    # 3ª Etapa: Confirma / Check / Valida
    assert resultado_atual == resultado_esperado


#anotação para usar como massa de teste
@pytest.mark.parametrize('B, h, resultado_esperado' ,[
    #valores:
            (6, 8, 48),  #teste n°1
            (4, 8, 32), #teste n°2
            (3, 4, 12), #teste n°3
            (4, 5, 20),  #teste n°4
            ('a', 'b', 'Falha de cálculo - dado digitado não é um número'), #teste nº5
            (' ','&','Falha de cálculo - dado digitado não é um número'), #teste nº6
                                ])

def testar_calcular_area_de_um_retangulo(B, h, resultado_esperado):
    # 1ª Etapa - Configura / Prepara
    #Dados / Valores
    #Entradas / Input
   # B = 6
    #h = 8
    #Saída / Output
    #resultado_esperado = 48

    # 2ª Etapa: Executa
    resultado_atual = calcular_area_de_um_retangulo(B, h)

    # 3ª Etapa: Confirma / Check / Valida
    assert resultado_atual == resultado_esperado

@pytest.mark.parametrize('l, resultado_esperado' ,[
    #valores:
            (1, 1),  #teste n°1
            (2, 4), #teste n°2
            (3, 9), #teste n°3
            (4, 16),  #teste n°4
            ('a','Falha de cálculo - lado não é um número'), #teste nº5
            (' ','Falha de cálculo - lado não é um número'),  #teste nº6
                           ])

def testar_calcular_area_de_um_quadrado(l, resultado_esperado):
    # 1ª Etapa - Configura / Prepara
    #Dados / Valores
    #Entradas / Input
    #l = 9
    #Saída / Output
    #resultado_esperado = 81

    # 2ª Etapa: Executa
    resultado_atual = calcular_area_de_um_quadrado(l)

    # 3ª Etapa: Confirma / Check / Valida
    assert resultado_atual == resultado_esperado

#anotação para usar como massa de teste
@pytest.mark.parametrize('r, resultado_esperado' ,[
    #valores:
            (1, 3.14),  #teste n°1
            (2, 12.56), #teste n°2
            (3, 28.26), #teste n°3
            (4, 50.24),  #teste n°4
            ('a','Falha de cálculo - Raio não é um número'), #teste nº5
            (' ','Falha de cálculo - Raio não é um número'), #teste nº6
                                ])
def testar_calcular_area_de_um_circulo(r, resultado_esperado):
    # 1ª Etapa - Configura / Prepara
    #Dados / Valores
    #Entradas / Input
   ## r = 1
    #Saída / Output
    ##resultado_esperado = 3.14

    # 2ª Etapa: Executa
    resultado_atual = calcular_area_de_um_circulo(r)

    # 3ª Etapa: Confirma / Check / Valida
    assert resultado_atual == resultado_esperado

def testar_calcular_volume_de_um_paralelograma():
    # 1 configura:
    l = 5
    c = 10
    h = 2
    resultado_esperado = 100

    #2 executa:
    resultado_atual = calcular_volume_de_um_paralelograma(l, c, h)

    #3 valida:
    assert resultado_atual == resultado_esperado
