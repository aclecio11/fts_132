import pytest
    #FUNÇÕES( cozinheiro):
def somar_dois_numeros(a,b):
    return a + b

def subtrair_dois_numeros(a, b):
    return a - b

def multiplicar_dois_numeros(a, b):
    return a * b

def dividir_dois_numeros(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'Não é possivel dividir por zero'

def elevar_um_numero_ao_outro(a, b):
        return a ** b

def calcular_area_de_um_triangulo(B, h):
    return (B * h)/2

def calcular_area_de_um_retangulo(B, h):
    return B * h

def calcular_area_de_um_quadrado(l):
    return l ** 2

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



