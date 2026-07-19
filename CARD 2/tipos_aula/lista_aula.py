nums = [1, 2, 3]

print(type(nums)) # <class 'list'>
# listra permite repetidos
nums.append(3) # para adicionar 
nums.append(3) # para adicionar 
nums.append(3) # para adicionar 
print(len(nums)) # len mostra o tamanho

print(2 in nums) # True 

nums[3] = 100
print(nums) # [1, 2, 3, 100, 3, 3]
nums.insert(0, -200) # pra inserir um numero em um inc x
print(nums) # [-200, 2, 3, 100, 3, 3]

print(nums[6]) # pra printa algum valor especificcco
print(nums[-1]) #-1 ultimo da lista
print(nums[-2])# pega o penultimo

