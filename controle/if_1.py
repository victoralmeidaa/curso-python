#!python3
nota = float(input('Informe Nota: '))
comportado = True if input('Comportado (y/n): ') == 'y' else False

if nota >= 9 and comportado:
    print('Parabens!')
    print('Quadro de Honra')
elif nota >= 7:
    print('Aprovado')
elif nota >= 5.5:
    print('Recuperacao')
elif nota >= 3.5:
    print('Recuperacao + Atividade')
else:
    print('Reprovado')

print(nota)

