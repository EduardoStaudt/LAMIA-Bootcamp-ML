def saudacao(nome= 'Pessoa', idade= 20):
    print(f'Bom dia {nome}! \nVc nem parece ter {idade} anos!')

# def saudacao():
#     print('Boa tarde') # o python ñ tem sobrecarga

def  soma_e_mult(a, b, x):
    return a + b * x

if __name__ == '__main__': # verifica se o arquivo começou por aqui ou se foi chamado em outro lugar 
    saudacao(nome = 'Ana', idade = 30) #se foi roda isso