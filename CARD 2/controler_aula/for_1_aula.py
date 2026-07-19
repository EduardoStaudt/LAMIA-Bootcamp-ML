for i in range(10): # vai de 0 a 9
    print(i, end = " ")
print("")
for i in range(11): # vai de 0 a 10
    print(i, end = " ")
print("")
for i in range(1, 100, 7): # vai de 1 a 99 com step de 7
    print(i, end = " ")
print("")
for i in range(20, 0, -3): # vai de 1 a 99 com step de 7
    print(i, end = " ")
print("")
nums = [2, 4, 6, 8]

for n in nums:
    print(n, end= ", ")
print("")
texto = "Python é muito massa !"

for letra in texto:
    print(letra, end= " ")
print("")
for n in {1, 2, 3, 4, 4, 4}: # vai de 1 a 99 com step de 7
    print(n, end=" ")

produto = {
    "nome": "Caneta",
    "preco": 8.80,
    "desc": 0.5
}
print("")
for atrib in produto:
    print(atrib, "==>", produto[atrib], end = " ") # printar as chave valor com percorrimento no indice
print("")
for atrib, valor in produto.items():
    print(atrib, "=>", valor, end = " ") # printar as chave valor com .items
print("")
for valor in produto.values():
    print(valor, end = " ") # printar as os valores com o .values
print("")
for keys in produto.keys():
    print(keys, end= ' ') # printar as chaves com o .keys