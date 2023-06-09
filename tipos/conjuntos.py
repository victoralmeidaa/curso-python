
print({1, 2, 3})
print(type({1, 2, 3}))
 
conj1 = {1, 2, 3, 3, 3, 3}
conj2 = set([4, 5, 6, 6, 6])

# print(conj1[1])    # conjuntos nao permite acessar elementos a partir de valores indexados 
print(conj1)         # Conjuntos nao imprime valores repetidos 
print(len(conj1))    # Conjuntos nao retorna valores repetidos 

print(conj2)         # Conjuntos nao imprime valores repetidos 
print(len(conj2))    # Conjuntos nao retorna valores repetidos