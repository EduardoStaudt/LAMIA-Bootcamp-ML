def soma(*nums): # é uma tupla
    total = 0
    for n in nums:
        total += n
    return total

def resultado_final(**kwargs): # é um dict no caso key : value
    status = 'aprovado(a) ' if kwargs['nota'] >= 7.0 else 'reprovado(a) '
    return f'{kwargs['nome']} foi {status}'