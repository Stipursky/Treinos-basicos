nome = input("Insira o nome do aluno: ")
n1 = float(input("Insira a 1ª nota: "))
n2 = float(input("Insira a 2ª nota: "))
n3 = float(input("Insira a 3ª nota: "))

media = (n1 + n2 + n3) / 3

if media >= 7:
    print(f"O aluno(a): {nome} foi aprovado(a) com média: {media:.2f}.")

else:
    print(f"O aluno(a): {nome} foi reprovado(a) com média: {media:.2f}.")
