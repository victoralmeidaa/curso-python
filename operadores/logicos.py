b1 = True
b2 = False
b3 = True

print(b1 and b2 and b3)         # Operador logico E(And)
print(b1 or b2 or b3)           # Operador logico OU(Or)
print(b1 != b2)                 # Pseudo Operador Logico OU Exclusivo(Xor)
print(not b1)                   # Operador Logico Nedacao
print(not b2)                   # Operador Logico Nedacao
print(b1 and not b2 and b3)     # Multiplos Operadores

x = 3
y = 4

print(b1 and not b2 and x < y)  # Operadores Logicos com Operadores Relacionais
