from Sistema_Bancario import *

menu_pricipal = '''
Escolha uma opção:
(1) Criar usuário
(2) Criar conta corrente
(3) Listar contas correntes
(4) Selecionar conta corrente
(0) Sair

Opção: '''

menu_conta = '''
Escolha uma opção:
(1) Depósito
(2) Saque
(3) Extrato
(0) Sair

Opção: '''


while True:
    print("=" * 50)
    print("MENU PRINCIPAL".center(50)) 
    opcao = input(menu_pricipal)
    print("=" * 50)

    if opcao == '1':
        print("-" * 50)
        print("CRIAR USUÁRIO".center(50))
        criar_usuario()
        print("-" * 50)

    elif opcao == '2':
        print("-" * 50)
        print("CRIAR CONTA CORRENTE".center(50))
        if usuarios:
            criar_conta()
            
        else:
            print('\nNão há usuários cadastrados.')
        
        print("-" * 50)
    
    elif opcao == '3':
        print('-' * 50)
        print('LISTAR CONTAS CORRENTES'.center(50), end='\n\n')

        if contas:
            listar_contas_correntes()
        
        else:
            print('\nNão há contas correntes cadastradas.')

        print('-' * 50)

    elif opcao == '4':
        if contas:
            print('-' * 50)
            print('SELECIONAR CONTA CORRENTE'.center(50))
            conta = selecionar_conta_corrente()
            print('-' * 50)

            if conta:

                while True:
                    print("=" * 50)
                    print(f"CONTA CORRENTE".center(50))
                    print(conta)
                    print(f"Saldo: R$ {conta.saldo:.2f}")
                    opcao = input(menu_conta)
                    print("=" * 50)
                    
                    if opcao == '1':
                        print('-' * 50)
                        print('DEPÓSITO'.center(50))
                        if deposito(conta):
                            print('\nDeposito realizado com sucesso.')
                        print('-' * 50)
                    
                    elif opcao == '2':
                        print('-' * 50)
                        print('SAQUE'.center(50))

                        if conta.saldo:
                            if saque(conta):
                                print('\nSaque realizado com sucesoo.')
                        else:
                            print('\nSaldo insuficiente.')

                        print('-' * 50)
                    
                    elif opcao == '3':
                        print('-' * 50)
                        print('EXTRATO'.center(50))

                        if conta.extrato:
                            conta.mostrar_extrato()
                        
                        else:
                            print('\nNão houve movimentação na conta.')

                        print('-' * 50)
                    
                    elif opcao == '0':
                        break
                    
                    else:
                        print('\nOpção inválida.') 

        else:
            print('\nNão há contas correntes cadastradas.')
            print('-' * 50)
        
    elif opcao == '0':
        break

    else:
        print('\nOpção inválida.')
        print('-' * 50)
