#BEE 1019
#tempo = int(input())
#hh = tempo // 3600
#mm = tempo // 60
#ss = tempo % 60
#print(f'{hh}:{mm}:{ss}')

#BEE 1020
#tempo=int(input())

#ano = tempo // 365
#resto = tempo % 365
#mes = resto // 30
#dias = resto % 30
#print(ano, ("ano(s)"))
#print(mes , ("mes(e)s"))
#print(dias , ("dia(s)"))

#EXERCÍCIO 1 Leia um valor em segundos e converta para horas, minutos e segundos

#tempo = int(input())
#horas = tempo // 3600
#resto = tempo % 3600
#minutos = resto // 60
#segundos = resto % 60
#print (f"{horas} : {minutos} : {segundos} ")

#EXERCÍCIO 2 Leia um valor inteiro e informe quantas notas de
#100, 50, 20, 10, 5, 2, 1
#576
#numero = int(input())
#notas_100 = numero // 100
#resto = numero % 100
#notas_50 = resto // 50
#resto = resto % 50
#notas_20 = resto // 20
#resto = resto % 20
#notas_10 = resto // 10
#resto = resto % 10
#notas_5 = resto // 5
#resto = resto % 5
#notas_2 = resto // 2
#resto = resto % 2
#notas_1 = resto // 1
#resto = resto % 1
#print (f"{notas_100} de notas 100")
#print (f"{notas_50} de notas 50")
#print (f"{notas_20} de notas 20")
#print (f"{notas_10} de notas 10")
#print (f"{notas_5} de notas 5")
#print (f"{notas_2} de notas 2")
#print (f"{notas_1} de notas 1")

tempo=int(input())
dias = tempo * 365
resto = tempo % 24
print(dias , ("dias"))
print(resto)

