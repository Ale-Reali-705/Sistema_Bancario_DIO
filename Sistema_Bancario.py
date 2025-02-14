'''
Sistema Bancario: depósito, saque e extrato.

depósito:
    apenas valores positivos
    armazenar o valor depositado na variavel extrato

saque:
    limite diário de 3 saques
    500 reais por saque
    em caso de saldo insuficiente, informar ao usuário
    armazenar o valor sacado na variavel extrato

extrato:
    listar todos os depósitos e saques realizados
    se não houver movimentações, informar ao usuário "Não foram realizadas movimentações."
    formato: "Depósito: R$ 1000.00"
'''

menu = '''
Escolha uma opção:
(1) Depósito
(2) Saque
(3) Extrato
(0) Sair
Opção: '''

extrato = []
saldo = 0
saques = 0

def deposito():
    global saldo
    valor = float(input('\nValor do depósito: R$ ').replace(',', '.'))

    if valor > 0:
        extrato.append(f'Depósito: R$ {valor:.2f}')
        print(f'\nDepósito de R$ {valor:.2f} realizado com sucesso.')
        saldo += valor

    else:
        print('\nValor inválido.')


def saque():
    global saques, saldo
    saques += 1
    
    if saques > 3:
        print('\nLimite diário de saques atingido.\nVolte amanhã.')
        saques = 0
    
    else:
        valor = float(input('\nValor do saque: R$ ').replace(',', '.'))
    
        if valor > 500:
            print('\nValor máximo por saque é de R$ 500.00')
            saques -= 1
    
        elif valor > saldo:
            print('\nSaldo insuficiente.')
    
        else:
            extrato.append(f'Saque: R$ {valor:.2f}')
            print(f'\nSaque de R$ {valor:.2f} realizado com sucesso.')
            saldo -= valor


def mostrar_extrato():
    
    if extrato:
        print()
        for movimentacao in extrato:
            print(movimentacao)
        print(f'\nSaldo: R$ {saldo:.2f}')

    else:
        print('\nNão foram realizadas movimentações.')

while True:

    print('\n', "MENU".center(20, '='), sep='', end='')
    opcao = input(menu)

    if opcao == '0':
        break

    elif opcao == '1':
        deposito()
    
    elif opcao == '2':
        saque()
    
    elif opcao == '3':
        mostrar_extrato()   
