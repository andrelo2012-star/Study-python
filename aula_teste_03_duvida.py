# for i in range(1,11): # não inclui o número final
#   print(i)

#l = [1,3,5,7,9]
#for i in l:
#    if i < 5 :
#        print(i)

#m = [1,3,5,7,9]
#for i in m:
#    if i <= 1 :
#        print(i)

#for i in range (1000000,0,-100):
#            print(i)

soma = 0
for i in range(1,10):
    soma+=i
print (soma)

#for i in range(1,11): # não inclui o número final
#    print(i)

#for i in range(2,22,2):
#    print(i)

#for i in range(3,33,3):
#       print(i)
for i in range(5,55,5):
            print(i)

numero = int(input("numero_tabuada"))
for i in range(1,101):
    print(numero,"x", i, "=", numero*i)

#for i in range(1,50):
#    contador = i
#    print(contador)

contador = 0     # quantos numeros são multiplos de 5
for i in range (1,51):
        if i % 5 == 0:
          contador += 1
          print(contador)
