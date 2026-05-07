#Data 05.03.2025
#BEE 1010 - versao feita por mim
#codigo1, qtde1, valorUnit1 = input().split()
#codigo2, qtde2, valorUnit2 = input().split()
#codigo1 = int(codigo1)
#qtde1 = int(qtde1)
#valorUnit1 = float(valorUnit1)
#codigo2 = int(codigo2)
#qtde2 = int(qtde2)
#valorUnit2 = float(valorUnit2)
#valor_a_pagar = float(qtde1 * valorUnit1) + float(qtde2 * valorUnit2)
#print (f"valor a pagar: {valor_a_pagar:.2f} ")

#versao mais curta
#codigo1, qtde1, valorUnit1 = input().split()
#codigo2, qtde2, valorUnit2 = input().split()
#Valor_a_pagar = int(qtde1) * float(valorUnit1) + int(qtde2) * float(valorUnit2)
#print(f"Valor a pagar: {Valor_a_pagar:.2f} ")

#BEE 1011
#R = float(input())
#pi = 3.14159
#volume = float(4/3.0) * pi * R ** 3
#print(f"volume = {volume:.3f}")

#BEE 1012
#a, b, c = map(float, input().split())
#pi = 3.14159
#Triangulo = (a * c) / 2
#Circulo = pi * c ** 2
#Trapezio = ((a + b) * c) / 2
#Quadrado = b ** 2
#Retangulo = a * b
#print(f"Triangulo: {Triangulo:.3f}")
#print(f"Circulo: {Circulo:.3f}")
#print(f"Trapezio: {Trapezio:.3f}")
#print(f"Quadrado: {Quadrado:.3f}")
#print(f"Retangulo: {Retangulo:.3f}")

#BEE 1013
a, b, c = map(int, input().split())
Maior_AB = (a + b + abs(a - b)) // 2
maior = (Maior_AB + c + abs(Maior_AB - c)) // 2
print(f"{maior} eh o maior")

a, b, c = map(int, input().split())
maior_ab = (a + b + abs(a - b)) // 2
maior = (maior_ab + c + abs(maior_ab - c)) // 2
print(f"{maior} eh o maior")




