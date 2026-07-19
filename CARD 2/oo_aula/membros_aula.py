class Contador:
    contador = 0 # atributo de classe]
    
    def inc_maluco(self):
        self.contador += 1 #self não considera valores já exitente na classe, ele cria um atributo de instância, que é diferente do atributo de classe
        return self.contador

    @classmethod
    def inc(cls):
        cls.contador += 1
        return cls.contador

    @classmethod    # indicxa que é u mmetodo de classe
    def dec(cls): # cls=classe
        cls.contador -= 1
        return cls.contador
    
    @staticmethod   
    def mais_um(n):
        return n + 1

c1 = Contador()

# print(c1.inc_maluco())
# print(c1.inc_maluco())

print(Contador.inc())
print(Contador.inc())
print(Contador.inc())
print(Contador.dec())
print(Contador.dec())
print(Contador.dec())

print(c1.inc_maluco())
print(c1.inc_maluco())

print(Contador.mais_um(99))