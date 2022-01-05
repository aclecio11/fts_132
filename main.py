import pytest
    #FUNÇÕES( cozinheiro):
#a = int(input('Digite um numero: '))
#b = int(input('Digite outro numero: '))
def somar_dois_numeros(a,b):
    try:
        return a ++ b
    except TypeError:
        return 'Falha de cálculo - dado digitado não é um número'

# print('Soma = ', somar_dois_numeros(a, b))

def subtrair_dois_numeros(a, b):
    try:
        return a - b
    except TypeError:
        return 'Falha de cálculo - dado digitado não é um número'

def multiplicar_dois_numeros(a, b):
    try:
        return a * b
    except TypeError:
        return 'Falha de cálculo - dado digitado não é um número'


def dividir_dois_numeros(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Não é possivel dividir por zero'

    except TypeError:
        return 'Falha de cálculo - dado digitado não é um número'

def elevar_um_numero_ao_outro(a, b):
        try:
            return a ** b
        except TypeError:
            return 'Falha de cálculo - dado digitado não é um número'

def calcular_area_de_um_triangulo(B, h):
    try:
        return B * h / 2
    except TypeError:
        return 'Falha de cálculo - dado digitado não é um número'

def calcular_area_de_um_retangulo(B, h):
    try:
        return B * h
    except TypeError:
        return 'Falha de cálculo - dado digitado não é um número'

def calcular_area_de_um_quadrado(l):
    try:
        return l ** 2
    except TypeError:
        return 'Falha de cálculo - lado não é um número'

def calcular_area_de_um_circulo(r):
    try:
        return 3.14 * r ** 2
    except TypeError:
        return 'Falha de cálculo - Raio não é um número'

    #CHAMADAS(garçom):
if __name__ == '__main__':

       resultado = somar_dois_numeros(89, 8)
       print(f'A soma é {resultado}')

       resultado = subtrair_dois_numeros(59, 17)
       print(f'A subtração é {resultado}')

       resultado = multiplicar_dois_numeros(145, 15)
       print(f'A multiplicação é {resultado}')

       resultado = dividir_dois_numeros(365, 5)
       print(f'A divisão é {resultado}')

       resultado = elevar_um_numero_ao_outro(3, 4)
       print(f'A exponenciação é {resultado}')

       resultado = calcular_area_de_um_triangulo(5, 8)
       print(f'A area do triâgulo é {resultado}')

       resultado = calcular_area_de_um_retangulo(8, 3)
       print(f'A area do retângulo é {resultado}')

       resultado = calcular_area_de_um_quadrado(9)
       print(f'A area do quadrado é {resultado}')

       resultado = calcular_area_de_um_circulo(9)
       print(f'A area do circulo é {resultado}')



