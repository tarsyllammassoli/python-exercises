notas = []
soma_das_notas = 0
alunos_aprovados = 0

for i in range(4):
    nota = float(input(f"Digite a {i + 1}º nota: "))
    notas.append(nota)
for algo in notas:
    soma_das_notas = soma_das_notas + algo
media_turma = soma_das_notas / 4
for aluno in notas:
    if aluno >= media_turma:
        alunos_aprovados += 1

print(f"A média da turma foi: {media_turma:.2f}")
print(f"Total de alunos aprovados foram: {alunos_aprovados}")