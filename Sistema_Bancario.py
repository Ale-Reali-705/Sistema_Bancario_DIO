'''
Sistema Bancario: depósito, saque e extrato.

parte 1:
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
        formato:
            "Depósito: R$ 1000.00"
            "Saque: R$ 500.00"

parte 2:
    criar usuário (cliente):
        lista = [{'Nome': str, 'CPF': apenas números, 'Endereço': cidade/ESTADO}]
        não podem haver CPFs repetidos

    criar conta corrente (banco):
        lista = [{'agencia': '0001', 'conta': sequencia, 'usuario': str}]

    listar contas correntes:
        listar todas as contas correntes cadastradas
        
'''

usuarios = [{'Nome': 'Fulano', 'CPF': '12345678900', 'Endereco': 'Fortaleza/CE'}]
contas = []

def criar_usuario():
    '''
    Recebe strings nome, cpf e endereco.
    Adiciona um dicionário com esses valores na lista usuarios.
    '''

    nome = input('\nNome: ')
    endereco = input('Endereço (Cidade/UF): ')
    cpf = input('CPF (apenas números): ')

    try:
        if not cpf.isdigit():
            raise Exception('CPF deve conter apenas números.')
        if cpf in [usuario['CPF'] for usuario in usuarios]:
            raise Exception('\nCPF já cadastrado.')
    
    except Exception as e:
        print(f"\nNão foi posível cadastrar usuário.\nERRO: {e}")
        return None
    
    else:
        usuarios.append({'Nome': nome, 'CPF': cpf, 'Endereco': endereco})
        return print('\nUsuário cadastrado com sucesso.')
    

def criar_conta_corrente():
    '''
    Adiciona um dicionário com agencia, conta e usuário na lista de contas.
    '''

    print("\nSelecione um usuário:")
    lista_nomes = [usuario['Nome'].title() for usuario in usuarios]
    print(*[f"({i}) {nome}" for i, nome in enumerate(lista_nomes)], sep='\n')

    try:
        indice = int(input("\nOpção: "))
        if indice not in range(len(lista_nomes)):
            raise Exception()
        
    except Exception:
        print('\nOpção inválida.')
        return None

    else:
        contas.append({'Agencia': '0001', 'Conta': len(contas) + 1, 'Usuario': lista_nomes[indice], 'Saldo': 0, 'Extrato': '', 'Saques': 0})
        return print('\nConta corrente criada com sucesso.')


def listar_contas_correntes():
    '''
    Lista todas as contas correntes cadastradas.
    '''

    print(f"\n{'USUÁRIO':37}AGENCIA-CONTA")
    for conta in contas:
        print(f"{conta['Usuario']:43}{conta['Agencia']}-{conta['Conta']:02}")


def selecionar_conta_corrente():
    '''
    Filtra as contas correntes pelo nome do usuário.
    Seleciona a conta corrente pelo número.
    '''

    nome = input('\nBucar por nome do usuário: ').lower()
    
    if nome not in [conta['Usuario'].lower() for conta in contas]:
        print('\nUsuário não possui conta corrente.')
        return None
    
    else:
        contas_usuario = [conta for conta in contas if conta['Usuario'].lower() == nome]
        print('\nO usuário possui as seguintes contas corrente:')
        print(*[f"{conta['Agencia']}-{conta['Conta']:02}" for conta in contas_usuario], sep='\n')

        try:
            cod_conta = int(input('\nDigite o número da conta corrente: 0001-'))
            if cod_conta not in [int(conta['Conta']) for conta in contas_usuario]:
                raise Exception()
            
        except Exception:
            print('\nConta inválida.')
            return None

        else:
            return [conta for conta in contas if conta['Conta'] == cod_conta][0]


def deposito(conta:dict):
    '''
    Recebe um dicionário conta.
    Adiciona um valor ao saldo da conta.
    '''

    try:
        valor = float(input('\nValor do depósito: R$ ').replace(',', '.'))
    
    except ValueError:
        print('\nValor inválido.')
        return None
        
    else:
        if valor > 0:
            conta['Extrato'] += 'Depósito: {}{}\n'.format(' ' * (40 - len(f'R$ {valor:.2f}')), f'R$ {valor:.2f}')
            print(f'\nDepósito de R$ {valor:.2f} realizado com sucesso.')
            conta['Saldo'] += valor

        else:
            print('\nValor inválido.')


def saque(conta:dict):
    '''
    Recebe um dicionário conta.
    Realiza um saque na conta.
    Respeitando o limite diário de 3 saques diário e o valor máximo de 500 reais.
    '''
    
    try:
        valor = float(input('\nValor do saque: R$ ').replace(',', '.'))
    
    except ValueError:
        print('\nValor inválido.')
        return None

    else:
        if valor > 500:
            print('\nValor máximo por saque é de R$ 500.00')

        elif valor > conta['Saldo']:
            print('\nSaldo insuficiente.')
            return None
    
        else:
            conta['Extrato'] += 'Saque: {}{}\n'.format(' ' * (43 - len(f'R$ {valor:.2f}')), f'R$ {valor:.2f}')
            print(f'\nSaque de R$ {valor:.2f} realizado com sucesso.')
            conta['Saldo'] -= valor
            conta['Saques'] += 1


def mostrar_extrato(conta:dict):
    '''
    Recebe um dicionário conta.
    Mostra o extrato da conta.
    '''
    
    saldo = conta.get('Saldo')

    print(conta['Extrato'])
    print("Saldo: {}{}".format(' ' * (43 - len(f"R$ {saldo}")), f"R$ {saldo:.2f}"))
