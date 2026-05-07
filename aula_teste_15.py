# 06.05.2026
"""
x, y, z = 1, 2, 3
print(x)
print(y)
print(z)
"""
"""
x = y = z = 3
print(x)
print(y)
print(z)
"""
#Desempacotamento / unpack
"""
frutas = ("maca", "banana", "uva")
x, y, z = frutas
print(x)
print(y)
print(z)
"""
#Variáveis de saída
"""
x = "python e legal"
print(x)
"""
"""
x = "python"
y = "e"
z = "legal"
print(x,y,z)
"""
"""
x = "python "
y = "e "
z = "legal "
print(x + y + z)
"""
"""
x = 1
y = 2
print(x + y)
"""
"""
x = 5  ====>usar virgula
y =("john")
print(x , y)
"""
"""
#Usando * para pegar o resto
numeros = [1, 2, 3, 4, 5]
a, *resto = numeros
print(a)
print(resto)
"""
"""
valores = [1, 2, 3, 4, 5]
x, *outros = valores
print(x)
print(outros)
"""
"""
valores = [1, 2, 3, 4, 5]
inicio, *meio, fim = valores
print(inicio)
print(fim)
print(meio)
"""
"""
#Variáveis Globais
x = "legal"
def myfunc():
    print("python e " + x)
myfunc()
"""
"""
x = "legal"
def myfunc():
   print("python e " + x)
x = "fantastico"
myfunc()
"""
x = 5
y = "john"
print(type(x))
print(type(y))


