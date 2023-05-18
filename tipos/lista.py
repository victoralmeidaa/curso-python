nums = [1,2,3]
print(type(nums))

nums.append(3)
nums.append(4)
nums.append(5)
print(len(nums))

nums[3] = 100 # indice 3 recebe valor 100
nums.insert(0, -200) # indice 0 recebe valor -200

print(nums[6]) # imprime na tela o valor do indice 6
print(nums[-1]) # imprime na tela o valor do ultimo indice
print(nums[-2]) # imprime na tela o valor do penultimo indice


print(nums)
