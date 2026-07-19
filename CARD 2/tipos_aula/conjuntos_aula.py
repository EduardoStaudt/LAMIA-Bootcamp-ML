#set utiliza {} e não permite dup
print({1, 2, 3}) # {1, 2, 3}
print(type({1, 2, 3})) # <class 'set'>
#print({1, 2, 3, 3, 3, 3, 3}) # {1, 2, 3}

# nao é indexavel não da pra ficar acessando eles 

conj = {1, 2, 3, 3, 3, 3, 3}
print(conj) # não mostra as dups {1, 2, 3}

print(len(conj)) # e tbm não contabiliza elas = 3