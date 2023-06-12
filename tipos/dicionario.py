aluno = {
    'nome': 'Pedro Henrique',
    'nota': 9.5,
    'ativo': True
}

print(type(aluno))      # imprime tipo dicionario
print(aluno['nome'])    # imprime chave nome
print(aluno['nota'])    # imprime chave nota
print(aluno['ativo'])   # imprime chave ativo
print(len(aluno))       # imprime quantidades de chaves

prof = dict(nome='Fernando', diciplina='Matematica', ativo=True)

print(type(prof))
print(prof)

prof['ativo'] = False

print(prof)
