# n1 = float(input("digite uma nota"))
# n2 = float(input("digite segunda nota"))
# n3 = float(input("digite terceira nota"))

n1 = 5
n2 = 7
n3 = 10

media = (n1 + n2 + n3) / 3

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else :
    print("Reprovado")