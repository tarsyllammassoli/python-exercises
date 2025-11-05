numeros = []

for i in range(1,101):
    print(i, end=" ")
    numeros.append(i)

soma_numeros = sum(numeros)

print(f"Somatório de todos os números de 1 a 100: ", soma_numeros)
