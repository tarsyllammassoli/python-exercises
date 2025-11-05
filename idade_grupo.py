idade_mulheres = []
idade_homens = []
idade_grupo = []

for i in range(10):
    gênero = input(f"Digite seu gênero (M) Mulher ou (H) Homem: ")
    idade = int(input(f"Digite sua idade: "))
    if gênero == "M":
        idade_mulheres.append(idade)
        idade_grupo.append(idade)
    if gênero == "H":
        idade_homens.append(idade)
        idade_grupo.append(idade)

soma_mulheres = sum(idade_mulheres)
soma_homens = sum(idade_homens)
soma_grupo = sum(idade_grupo)

quantidade_mulheres = len(idade_mulheres)
quantidade_homens = len(idade_homens)
quantidade_grupo = len(idade_grupo)

media_mulher = soma_mulheres / quantidade_mulheres
media_homem = soma_homens / quantidade_homens
media_grupo = soma_grupo / quantidade_grupo

print("\n")
print(f"Idade das Mulheres:", idade_mulheres)
print(f"Média da idade das Mulheres: ", media_mulher)
print(f"Idade dos Homens: ", idade_homens)
print(f"Média da idade dos Homens: ", media_homem)
print(f"Idade do grupo: ", idade_grupo)
print(f"Média da idade do grupo: ", media_grupo)
