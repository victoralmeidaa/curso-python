from functools import reduce

alunos = [
    {'name': 'Ana', 'nota': 7.2},
    {'name': 'Breno', 'nota': 8.1},
    {'name': 'Claudia', 'nota': 8.7},
    {'name': 'Pedro', 'nota': 6.4},
    {'name': 'Rafael', 'nota': 6.7}
]

obter_nota = lambda aluno: aluno['nota']
somar = lambda a, b: a + b

alunos_aprovados = [aluno for aluno in alunos if aluno['nota'] >= 7]
notas_alunos_aprovados = [aluno['nota'] for aluno in alunos_aprovados]
total = reduce(somar, notas_alunos_aprovados, 0)

print(total / len(alunos_aprovados))
