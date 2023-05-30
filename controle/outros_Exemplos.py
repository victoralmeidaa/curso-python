#!python3

pessoas = ['Gui', 'Rebeca']
adjs = ['Sapeca', 'Inteligente']

for p in pessoas:
    for a in adjs:
        print(f'{p} e {a}')             # imprime pessoas e adjetivos

for i in [1, 2, 3]:                     # para definir um laco vazio e preciso do pass
    pass 

for i in range(1, 11):
    if i % 2 == 1:
        continue
    print(i, end=' ')
print(' ')
for i in range(1, 11):
    if i == 5:
        break
    print(i, end=' ')
print(' ')
print('Fim')