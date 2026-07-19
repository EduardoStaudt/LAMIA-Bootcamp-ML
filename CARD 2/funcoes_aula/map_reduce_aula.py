from functools import reduce

notas = [6.4, 7.2, 5.8, 8.4]

def somar_nota(delta):
    def somar(nota):
        return nota + delta
    return somar

#  o map vem de mapear no cada um dos elementos e aplica individualmente um a função a cada um deles
notas_finais_1 = list(map(somar_nota(1.5), notas))
notas_finais_2 = list(map(somar_nota(1.6), notas))

print(notas_finais_1)
print(notas_finais_2)

total = 0
for n in notas:
    total += n

def somar(a, b):
    return a + b

total = reduce(somar, notas, 0) # junta tudo os valores em um 
## tipo ele percore um por um e somando após ser passado uma func
print(total)

# for i, nota in enumerate(notas):
#     notas[i] = nota + 1.5
    
# print(notas)

# notas = [6.4, 7.2, 5.8, 8.4]

# for i in range(len(notas)):
#     notas[i] = notas[i] + 1.5

# print(notas)