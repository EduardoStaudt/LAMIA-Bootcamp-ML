#Aqui busquei calcular média ponderada usando reduce as média ponderada de um dict como se fosse a calculadora de coeficiente absoluto da UTFPR
from functools import reduce

def calcular_coeficiente_absoluto(notas, pesos): # usando diversos conceitos tipo funcoes, labda tipos vairaveis 
    produto = reduce(lambda x, y: x + y, map(lambda n, p: n * p, notas, pesos)) 
    # primeirto o map(lambda n, p: n * p, notas, pesos) multiplica cada nota pelo seu peso correspondente aqui a pond. j[pa ta feita]
    # depois vai pro segundo lambda x, y: x + y que vai somar todas ponderadas da lista gerada no map e dai [por dim o reduce]
    # o redece eh quem aplica o primeiro lmbda a todos os elementos da lista gerada pelo map, somando todos os produtos das notas pelos pesos
    soma_pesos = sum(pesos) #  o sum soma os pessos
    return produto / soma_pesos if soma_pesos > 0 else 0 # depois eh so dividir o produto pela soma dos pesos, se a soma dos pesos for maior que 0, senao retorna 0
    # resumindo l1 =  l2 = soma os pesos l3 = divide o que o aluno tirou pelo peso total 

notas_por_materia = { # usando os conceitos de tipo do video 1
    'materia' : ['AEDIII', 'ES', 'PI1', 'IHC'],
    'notas' : [8.2, 8.9, 9.3, 9.9],
    'pesos' : [6, 6, 18, 6]
}

coeficiente = calcular_coeficiente_absoluto(notas_por_materia['notas'], notas_por_materia['pesos']) # aqui eu passei as notas e os pessoas para def 
print(f"Coeficiente Absoluto: {coeficiente}") # e por fim imprimo

#  o da UTF é mis complexo ele usa as notas de todas as matérias de todos os periodos para  calcular e alem disso tem o normalidado que usa a média do curso daí esse não tem copmo reproduzir aqui pq pra isso dependese das coeficientes normalizados de outros alunos