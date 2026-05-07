#BEE 1014 dia 08.03.2025
#km
#x = int(input()) #km
#y = float(input()) #combustivel_gasto
#consumo = (x / y)
#print(f"{consumo:.3f} km/l")

#BEE 1015
#x1, y1 = map(float, input().split())
#x2, y2 = map(float, input().split())
#Distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
#print (f"{Distancia:.4f}")

#BEE 1016 Fisica
#distancia = int(input())
#tempo = distancia * 2
#print(f"{int(input()) * 2} minutos")

#BEE 1017
#tempo = float(input())
#velocidade_media = float(input())
#consumo_carro = 12 #km-L
#Litros_viagem = (tempo * velocidade_media) / consumo_carro
#print (f"{Litros_viagem:.3f}")

#BEE 1018
#n = int(input())
#print(n)
#n100 = n // 100
#n = n % 100

#n50 = n // 50
#n = n % 50

#n20 = n // 20
#n = n % 20

#n10 = n // 10
#n = n % 10

#n5 = n // 5
#n = n % 5

#n2 = n // 2
#n = n % 2

#n1 = n

#print(f"{n100} nota(s) de R$ 100,00")
#print(f"{n50} nota(s) de R$ 50,00")
#print(f"{n20} nota(s) de R$ 20,00")
#print(f"{n10} nota(s) de R$ 10,00")
#print(f"{n5} nota(s) de R$ 5,00")
#print(f"{n2} nota(s) de R$ 2,00")
#print(f"{n1} nota(s) de R$ 1,00")

valor = int(input())
print(valor)

n100=valor // 100
resto = valor % 100

n50=resto // 50
resto = resto % 50

n20=resto // 20
resto = resto % 20

n10=resto // 10
resto = resto % 10

n5=resto // 5
resto = resto % 5

n2=resto // 2
resto = resto % 2

n1=resto // 1
resto = resto % 1

print(f"{n100} nota(s) de R$ 100,00")
print(f"{n50} nota(s) de R$ 50,00")
print(f"{n20} nota(s) de R$ 20,00")
print(f"{n10} nota(s) de R$ 10,00")
print(f"{n5} nota(s) de R$ 5,00")
print(f"{n2} nota(s) de R$ 2,00")
print(f"{n1} nota(s) de R$ 1,00")