a = 3
b = 4.4
texto = 'Sua idade eh '
idade = 23
print(a+b)
#print(texto+(a+b)) # isso da erro pois não d apra concattenar string e nuns
print(texto + str(idade)) # str() pra convertyer mas isso não é uma boa prática
print(f'{texto} {idade}')
""" pode ser usado com string com variavel = """ """
import pacote_aula.sub_aula.arquivo_aula
"""
saudacao = 'Bom dia '
print(3 * saudacao)

# constantes por convencao sao em maiusculo
PI = 3.14
PI = 3.1415 # no python n tem constante
# funcao input para coleta dados
#raio = input('informe o raio da circunferencia: ')
# da para por na variavel

# funcao type fala o tipo da variavel
#print(type(raio)) # <class 'str'>
# bota o float para fazer tipo um casting 
raio = float(input("informe o raio da circunferencia: "))
area = PI * raio * raio


print(type(raio)) ## <class 'float'> asr fica no tipo certo

print(f'A area da circunferencia  eh {area} m2')
# 314.15000000000003 resultado passando o 10 como raio como foi explicado no video estes resultados não são dfe total confiança pois o algoritmo do python e da maioria das linguagens é bem mais rapido mas acaba perdendo precisão