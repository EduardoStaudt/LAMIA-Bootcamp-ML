# aqui busquei fazer uma calculadora de IMC com os conceitos mais básicos da primeira aula, usando estruturas de controle

def  menu():
    print('=== CALCULADORA DE IMC ===')
    print('1 - Calcular IMC')
    print('2 - Sair')
    opcao = input('Escolha uma opção: ')
    return opcao

opcao = '1'
while opcao == '1':
    opcao = menu()
    if opcao == '1':
        peso = float(input('Digite seu peso (kg): '))
        altura = float(input('Digite sua altura (m): '))
        imc = peso / (altura ** 2)
        print(f'Seu IMC é: {imc:.2f}')
        if imc < 18.5:
            print('Abaixo do peso ideal! =(')
        elif imc < 25:
            print('Você está com o peso ideal! =)')
        elif imc < 30:
            print('Você está com sobrepeso! =(')
        else:
            print('Você está com obesidade! =/')
    else:
        print('Saindo da calculadora de IMC...')
