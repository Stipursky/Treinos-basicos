p = int(input("Insira o 1º valor: "))
s = int(input("Insira o 2º valor: "))
t = int(input("Insira o 3º valor: "))

if t > p:
    t, p = p, t

if t > s:
    t, s = s, t

if s > p:
    s, p = p, s

print(f"\n O 1º valor é: {p}")
print(f" O 2º valor é: {s}")
print(f" O 3º valor é: {t}")


