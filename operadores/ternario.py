#!python3
lockdown = False
grana = 101

#   Resultado se Verdadeiro / Esprecao Logica / Resultado se Falso
status = 'em casa' if lockdown or grana <= 100 else 'Uhuuuu' 

print(f'O Status é: {status}')