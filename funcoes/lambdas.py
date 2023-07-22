from functools import reduce

alunos = [
    {'name': 'Ana', 'nota': 7.2},
    {'name': 'Breno', 'nota': 8.1},
    {'name': 'Claudia', 'nota': 8.7},
    {'name': 'Pedro', 'nota': 6.4},
    {'name': 'Rafael', 'nota': 6.7}
]


aluno_aprovado = lambda aluno: aluno['nota'] >= 7

aluno_honra = lambda aluno: aluno['nota'] >= 8

obter_nota = lambda aluno: aluno['nota']


alunos_aprovados = filter(aluno_aprovado, alunos)
alunos_honra = filter(aluno_honra, alunos)
notas_alunos_aprovados = map(obter_nota, alunos_aprovados)

# total = reduce(somar, notas_alunos_aprovados, 0)
# print(len(list(alunos_aprovados)))
# print(total / len(list(alunos_aprovados)))

# print(alunos)
# print(list(obter_nota(alunos)))
print(list(alunos_honra))
print(list(alunos_aprovados))
