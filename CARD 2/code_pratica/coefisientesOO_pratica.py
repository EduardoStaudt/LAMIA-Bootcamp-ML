# aqui eu continuei a segunda pratica mas implementando OO Tranformei  as matérias em uma Classe Diciplina da as diplinas são intanciadas dai depois usei Herança e Encapsulamento que foram vistos não aulas adicionei optativas e tipo um IC pra ficar mais que nem a realidade  depois no fim mostra o coeficiente absoluto do semestre e a carga horaria de materias regulares e optativas tirei map filter e reduce por conta da dificuldade e tava quase na hr de entregar sksksk

# PRA LIGAR E DESLIGAR O PRESET É SÓ IR NO PRESETS = True E MUDAR PRA False que daí coloca manualmente

class Diciplina:
    def __init__(self, nome= ' ', carga_horaria = 0, nota = 0): # ja deixei defaults para caso n'ao sejam preenchidos
        self.__nome = nome # deixei todos os atributos de instancia privados para aplicar o encapsulamento 
        self.__carga_horaria = carga_horaria
        self.__nota = nota

    @property
    def nome(self):
        return self.__nome

    @property
    def carga_horaria(self):
        return self.__carga_horaria

    @property
    def nota(self):
        return self.__nota

    @nota.setter
    def nota(self, nota):
        if nota < 0 or nota > 10:
            print("Nota inválida tem que se de 0 a 10") # coloquei a verifica;a'o principalmente por causa de negatico  e pq colocando mais que 10 vai estourar a nota tipo se confunde 10 ou 100
        else:
            self.__nota = nota
    
    def peso_coeficiente(self):
        return self.__carga_horaria # devolve a CH

class DiciplinaOptativa(Diciplina):
    pass

class DiciplinaIC(Diciplina):
    def peso_coeficiente(self):
        return 0 # devolve a CH zerada

# True usa os presets e o False nao Usa
PRESETS = True # aqui escolhe se que usar os presets ou passar um a um na m'ao no caso o wehile deixei ele como contante para mudar so aqui n'ao no tempo de execu;'ao

if PRESETS:
    diciplinas = []
    # criei uma lista e adicionei as do meu semestre pra ser um preset para testar se ta funcionando
    diciplinas.append(Diciplina(nome="Algoritmos e Estrutura de Dados III", carga_horaria=60, nota=8.2)) # entra no coeficiente
    diciplinas.append(Diciplina(nome="Cálculo", carga_horaria=60, nota=8.2)) # entra no coeficiente
    diciplinas.append(Diciplina(nome="Projeto Integrador I", carga_horaria=180, nota=9.3)) # entra no coeficiente
    diciplinas.append(Diciplina(nome="Engenharia de Software", carga_horaria=60, nota=8.9)) # entra no coeficiente
    diciplinas.append(Diciplina(nome="Interação Humano Computador", carga_horaria=60, nota=9.9)) # entra no coeficiente
    diciplinas.append(Diciplina(nome="Probabilidade e Estatística", carga_horaria=60, nota=9.1)) # entra no coeficiente
    diciplinas.append(Diciplina(nome="Arquitetura e Organização de Computadores", carga_horaria=90, nota=9.3)) # entra no coeficiente
    diciplinas.append(DiciplinaOptativa(nome="Metodologia da Pesquisa", carga_horaria=30, nota=9.5)) # entra no coeficiente
    diciplinas.append(DiciplinaIC(nome="NNAdsorption", carga_horaria=180, nota=10.0)) #o IC n'ao entra no calculo do coeficiente pois é um projeto externo
    
    print("\nDisciplinas cadastradas:")
    for d in diciplinas:
        print(f"  -  Nome: {d.nome}, Carga Horária: {d.carga_horaria}, Nota: {d.nota}")
else:
        diciplinas = [] 
        while True:
            nome = input("Digite o nome da disciplina (ou 'sair' para encerrar): ")
            if nome.lower() == 'sair': # usei o lower pra aceitar tanto maiusculo quanto minusculo pesquisei essa no google pois já usava no java daí fui procurar pra ver se tinha no python apliquei em praticamente todas as 
                break # sai do do while e encerra o programa
            carga_horaria = int(input("Digite a carga horária da disciplina: ")) # pra fazer a ponderada
            nota = float(input("Digite a nota da disciplina: ")) #nota * ch  = ponderada
            optativa = input("A disciplina é optativa? (s/n): ").lower() == 's' # pergunta se eh optativa aoptativa eh somada suma carga horaria separada
            ic = input("A disciplina é um IC? (s/n): ").lower() == 's' # pergunta se eh um projeto de IC

            if ic:
                diciplina = DiciplinaIC(nome, carga_horaria, nota) # aqui n'ao vai considerar a ch
            elif optativa:
                diciplina = DiciplinaOptativa(nome, carga_horaria, nota) # aqui a CH vai ser somada na optativa
            else:
                diciplina = Diciplina(nome, carga_horaria, nota) # aqui a ch vai normal pra regulaar

            diciplinas.append(diciplina) # add na list

        print("\nDisciplinas cadastradas:")
        for d in diciplinas:
            print(f"  -  Nome: {d.nome}, Carga Horária: {d.carga_horaria}, Nota: {d.nota}") # como eu usei o encapsulamento e o @property eu acesso o s metodos como se fosem atributos mesmo

soma_ponderada = sum(d.nota * d.peso_coeficiente() for d in diciplinas) #nota x peso de cada uma
soma_pesos = sum(d.peso_coeficiente() for d in diciplinas) # soma dos pesos, IC entra com 0
coeficiente_absoluto = soma_ponderada / soma_pesos if soma_pesos > 0 else 0 # divisao

# aqui eu calculo a carga hr das optativas e das regulares a de IC n'ao entra em nenhuma das duas
ch_regular_total = sum(d.carga_horaria for d in diciplinas if not isinstance(d, DiciplinaIC))# passa somando em todas e desconsidera as ch de IC
ch_optativa_total = sum(d.carga_horaria for d in diciplinas if isinstance(d, DiciplinaOptativa)) # aqui desconsidera as regulares e as de IC s[o aceita se for da classe DiciplinaOptativa
# esse isinstace eu tive que que aprender por fora e ele porque o meu codigo tava quebrando ele serve para perguntar esse objeto eh dessa classe? com isso deu pra mim usar a heranca 

print('=============================================')
print(f"Coeficiente absoluto do semestre: {coeficiente_absoluto:.3f}") # o :.3f limita as casas decimais
print('=============================================')
print(f'Carga de Horaria de Materias Regulares: {ch_regular_total}') # print
print('=============================================')
print(f'Carga de Horaria de Materias Optativas: {ch_optativa_total}') # print
print('=============================================')

