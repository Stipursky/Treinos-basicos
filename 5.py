p = int(input("Informe o 1º valor: "))
s = int(input("Informe o 2º valor: "))
t = int(input("Informe o 3º valor: "))

if p > s:
    p, s = s, p
if p > t:
    p, t = t, p
if s > t:
    s, t = t, s

print(f"\n 1º valor: {p}.")
print(f" 2º valor: {s}.")
print(f" 3º valor: {t}.")
