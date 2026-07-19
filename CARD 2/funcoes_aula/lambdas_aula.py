from functools import reduce

alunos = [
    {'nome': 'Ana', 'nota': 7.2},
    {'nome': 'Breno', 'nota': 8.1},
    {'nome': 'Claudia', 'nota': 9.0},
    {'nome': 'Pedro', 'nota': 6.4},
    {'nome': 'Rafael', 'nota': 6.7}
]

aluno_aprovado = lambda aluno: aluno['nota'] >= 7.0
aluno_honra = lambda aluno: aluno['nota'] >= 9.0
obter_nota = lambda aluno: aluno['nota']
somar = lambda a, b: a+b

# lambda avisa que é uma def inline - > aluno é o parametro: e  or estante é a condição

alunos_aprovados  = list(filter(aluno_aprovado, alunos))
alunos_honra  = list(filter(aluno_honra, alunos))
notas_alunos_aprovados = list(map(obter_nota, alunos_aprovados))
total = reduce(somar, notas_alunos_aprovados, 0) 
# o filter funcoiona como um for com if else por isso ele percorre e vai excluido os que não passam no filtro o mais legal é que ele cria uma nova lista e não apaga o original

print(total / len(alunos_aprovados))

print(list(alunos_honra))

print(alunos)
print(alunos_aprovados)
print(alunos_honra)
print(obter_nota(alunos[2]))
print(notas_alunos_aprovados)