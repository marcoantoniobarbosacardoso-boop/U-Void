Número = int (input("Digite um número: "))

while Número <= 0:
    Número = int (input("Digite um número: "))

Fatorial = 1

for i in range (1, Número + 1):
    Fatorial *= i

print (Fatorial)