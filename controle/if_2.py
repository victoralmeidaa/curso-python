#!python3
a = 'valor'     # Existe(True)
a = 0           # Nao Existe(False)
a = 0.00001     # Existe(True)
a = ''          # Nao Existe(False)
a = ' '         # Existe(True)
a = []          # Nao Existe(False)
a = {}          # Nao Existe(False)

if a:
    print('Existe!')
else:
    print('nao existe ou zero ou vazio...')
