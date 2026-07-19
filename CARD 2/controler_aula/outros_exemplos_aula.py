pessoas = ['Gui', 'Rebeca']
adjetivos = ['Sapeca', 'Inteligente']

for p in  pessoas: # for das pessoas
    for a in adjetivos: ## for dos adjetivos 2 desse pra ccada pessoa
        print(f'{p} é {a}!')# vai mostarr todas as possibilidades

for i in [1, 2, 3]:
    pass # para posder deixar sem nada dentros

for i in range(1, 11): # vai mostar só os pares
    if i % 2 == 1:
        continue # pula esse
    print(i)

for i in range(1, 11): # vai mostrar do a ao 4
    if i == 5:
        break # sai do laçõ
    print(i)

print('Fim!')