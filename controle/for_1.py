#!python3
for i in range(10):
    print(i, end=' ')               # imprime de 0 a 9
print('')

for i in range(1, 11):
    print(i,  end=' ')              # imprime de 1 a 10 / end imprime na mesma linha
print('')

for i in range(1, 100, 7):          # imprime de 1 a 100 paso 7
    print(i, end=' ')
print('')

for i in range(20, 0, -3):          # imprime de 20 a 0 paso -3
    print(i, end=' ')
print('')

nums = [2, 4, 6, 8]

for n in nums:
    print(n, end=' ')               # imprime todos os elementos de nums / end=' ' imprime tudo na mesma linha
print('')

texto = 'Python'

for letra in texto:
    print(letra, end=' ')
print('')

for n in {1, 2, 3, 4, 4, 4}:        # imprime de 1 a 4 / SET nao imprime valores repetidos
    print(n, end=' ')
print('')

produto = {
    'nome': 'Caneta',
    'Preco': 8.8,
    'Desconto': 0.5
}

for atributo in produto:
    print(atributo, '==>', produto[atributo])
print('')

for valor in produto.values():        # imprime os valores
    print( valor, end=' ')
print('')

for atributo in produto.keys():       # imprime as chaves
    print(atributo, end=' ')
print('')