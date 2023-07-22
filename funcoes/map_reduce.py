from functools import reduce


def somar_nota(delta):
    def calc(nota):
        return nota + delta
    return calc


notas = [6.4, 7.2, 5.4, 8.4]

notas_finais = map(somar_nota(1.5), notas)
# usar funcao lista para converter objetos map em lista
converter_lista = list(notas_finais)
# imprime a lista de notas
print(converter_lista)


def somar(a, b):
    return a + b


total = reduce(somar, notas, 0)
print(total)

# for i, nota in enumerate(notas):
#     notas[i] = nota + 1.5
# print(notas)

# for i in range(len(notas)):
#     notas[i] = notas[i] + 1.5
# print(notas)
