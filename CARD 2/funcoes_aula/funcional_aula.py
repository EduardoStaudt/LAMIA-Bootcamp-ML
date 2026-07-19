def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

somar = soma
print(somar(3, 4)) 

def operacao_aritimética(fn, op1, op2):
    return fn(op1, op2) # função que chma outar funcão

resultado = operacao_aritimética(soma, 13, 48)
print(resultado)

resultado = operacao_aritimética(sub, 13, 48)
print(resultado)

#funcão com retun de função
def soma_parcial(a):
    # processamento pessado 1 - 10s
    # processamento pessado 22 - 10s
    # processamento pessado 3 - 40s
    def concluir_soma(b):
        return a + b # 10s
    return concluir_soma
# ela é muito importante pois muitas vzes podemos ainda não ter por exemplo o parametro b
# tipo se a parte a demora um minuto e a parte b 10 s se eu for passar a func inteira toda ves eu teria de esperar 70seg toda vez nesses casos aqui 1, 2 - 1, 3 - 1, 4 tudo isso só porque eu troquei o b mas como o resutado parcial é uma func eu quardo ela em uma variavel e dai só chamo a função quardada com o 2, 3, 4 demorando assim só 10 seg para cada uma total de 90s no total para todas estas operações e da outra forma eu demoraria para ter os mesmos resultados 210 seg
soma_1 = soma_parcial(1) # aqui ja fez o processamento que demora um min
r1 = soma_1(2) #10s
r2 = soma_1(3) #10s
r3 = soma_1(4) #10s
print(r1, r2, r3) # assim o tempo de processamento é muito mais rapido isso tem a ver com programação funcional