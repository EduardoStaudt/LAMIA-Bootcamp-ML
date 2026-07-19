nomes = ("Ana", "Bia", "Gui", "Leo", "Ana") # tbm aceita repetições
# a tupla é estática só pode ser 

print('Bia' in nomes) # True
print('bia' in nomes) # False

print(nomes[0])
print(nomes[1:3]) # de -> até(sem incluir o até) 
print(nomes[1:-1]) # até o ultimo sem incluir ele
print(nomes[2:]) # tudo a partir dele inclusive o final
print(nomes[:-2]) # pega o que viria antes

# para se ter uma tupla é necessa´rio declarar com ('xxx',) tendo a , emsmo só com um elem

print(len(nomes))
print(type(nomes)) # <class 'tuple'>
print(nomes)