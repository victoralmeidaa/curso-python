nums = [1,2,3]      # Atribuir Lista 
print(type(nums))   # Imprime Tipo Lista

nums.append(3)  # adiciona o valor 3 ao final da lista

nums.append(4)
nums.append(5)
print(len(nums))

nums[3] = 100 # indice 3 recebe valor 100


nums.insert(0, -200) # insere o elemento -200 no índice 0 da lista

# nums.removo(3)

print(nums[6]) # imprime na tela o valor do indice 6
print(nums[-1]) # imprime na tela o valor do ultimo indice
print(nums[-2]) # imprime na tela o valor do penultimo indice

nums.remove(4) # remove o valor 4 da lista

print(nums)
