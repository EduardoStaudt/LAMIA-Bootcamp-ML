class Produto: # AQui é o molde 
    def __init__(self, nome, preco = 1.99, desc = 0):# func initserve para fazer a inisialização dos matributos e coloca um estado inicial se quise
        self.nome = nome    
        self.__preco = preco
        self.desc = desc
        
    @property #Essa eh a forma corrreta de se acessar um atributyo privado 
    def preco(self):
        return f'R$ {self.__preco}'
    
    @preco.setter # essa eh a forma de se alterar um atributo privado
    def preco(self, novo_preco):
        if novo_preco >= 0:
            self.__preco = novo_preco

    @property  # tranforma em um atributo calculadodo com outros valores da classe  
    def preco_final(self): 
        return self.__preco * (1 - self.desc)

p1 = Produto('Caneta', 10, 0.1) # é como se fosse um objeto fuito com com o molde Produto
p2 = Produto('Caderno', 14, 0.5) # mesma coisa mqas com outro atributo

p1.preco = 70.89 # alterando o atributo privado com o setter e nao diretamente pois ele é privado
p2.preco = -17.99 # não vai alterar pois o setter tem uma validação para não aceitar valores negativos

# <class '__main__.Produto'>
print(p1.nome, p1.preco, p1.desc, p1.preco_final) # se usa o ponto para fazer o acesso dos atrbutos de um obj
print(p2.nome, p2.preco, p2.desc, p2.preco_final) 

# encapsulamento
# da para deixar um atributo privado(não privado de verdade mas para pelo menos dar um erro cada vc tente puxa de fora da classe) através do __ antes do nome do atributo tipo: __nome
# mas como não é um private de verdade da para acessar com o _NomeDaClasse__nomeDoAtributo mas isso é uma quebra de regra da linguagem isso =é uma má utilização