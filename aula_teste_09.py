#BEE 1009 02 Março
#vendedor = input()
#salario = float(input())
#vendas = float(input())
#comissao = (vendas * 0.15 + salario)
#print (f"TOTAL = R$ {comissao:.2f}")
from functools import total_ordering

#exercicio split ()

#Ler dois números e somar
#a, b = input().split()
#a = int(a)
#b = int(b)
#soma = a + b
#print(soma)

#a, b = input().split()
#a = int(a)
#b = int(b)
#soma = a + b
#print(soma)

#Nome e idade (mostrar idade + 1)
#nome, idade = input().split()
#idade = int(idade)
#print(nome, idade +1)

#Dois inteiros e um float (produto)
#a, b, c = input().split()
#a = int(a)
#b = int(b)
#c = float(c)
#print (a * b *c)

#Duas linhas – soma total
#a, b, c = input().split()
#d, e, f = input().split()
#total = int(a) + int(b) + int(c) + int(d) + int(e) + int(f)
#print (total)

#Maior entre dois números
#a, b = input().split()
#a = int(a)
#b = int(b)
#if a > b:
#    print(a)
#else:
#    print(b)

#Soma de duas linhas ou mais
#a, b, c = input().split()
#a = int(a)
#b = int(b)
#c = int(c)
#soma = int(a) + int(b) + int(c)
#subtracao = int(a) - int(b) - int(c)
#multiplicacao = int(a) * int(b) * int(c)
#divisao = int(a) / int(b) / int(c)
#print(soma)
#print(subtracao)
#print(multiplicacao)
#print(divisao)

#Contar numeros pares
valores = input().split()
cont = 0
for valor in valores:
    if int(valor) % 2 == 0:
        cont += 1
print(cont)
