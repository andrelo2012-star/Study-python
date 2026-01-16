n1 = float(input("nota 1: 5"))
n2 = float(input("nota 2: 3"))
n3 = float(input("nota 3: 8"))

media = (n1 + n2 + n3) / 3

if media >= 7:
    print("Aprovado")
    elif media >= 5:
    print("Recuperação")
    else media >= 3:
    print("Reprovado")