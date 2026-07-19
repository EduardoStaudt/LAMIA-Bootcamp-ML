from functools import reduce

alunos = [
    {'nome': 'Ana', 'nota': 7.2},
    {'nome': 'Breno', 'nota': 8.1},
    {'nome': 'Claudia', 'nota': 9.0},
    {'nome': 'Pedro', 'nota': 6.4},
    {'nome': 'Rafael', 'nota': 6.7}
]

somar = lambda a, b: a+b

alunos_aprovados  = [aluno for aluno in alunos if aluno['nota'] >= 7.0]
# o list croprehension funciona praticamente como um filter ele faz ess sunbstituição
notas_alunos_aprovados = [aluno['nota'] for aluno in alunos_aprovados]
# tbm substitui o map
total = reduce(somar, notas_alunos_aprovados, 0) 

# print(alunos)
print(alunos_aprovados)
print(total)