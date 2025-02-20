contas = []

class Cliente:
    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.contas = []
        print("\nCliente cadastrado com sucesso.")

    def __str__(self):
        return f"Cliente: {self.nome} - {self.cpf}"
    
    def criar_conta_corrente(self):
        conta = ContaCorrente(self.nome)
        self.contas.append(conta)
        contas.append(conta)
        print("Conta corrente criada com sucesso.")

    def listar_contas(self):
        print(f"Contas do cliente: {self.nome}")
        for i, conta in enumerate(self.contas):
            print(f"({i}) - {conta}")
        
        


class Conta:
    def __init__(self, usuario):
        self.usuario = usuario
        self.agencia = '0001'
        self.conta = len(contas) + 1
        self.saldo = 0
        self.saques = 0
        self.saques_max = 0
        self.extrato = []

    def __str__(self):
        return f"{self.usuario} - {self.agencia}-{self.conta:02}"

    def depositar(self, valor:float):
        if valor >= 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            return True
        else:
            print('Valor inválido.')
            return False
        
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.saques -= 1
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            return True
        else:
            print('Saldo insuficiente.')
            return False
        
    def mostrar_extrato(self):
        for movimento in self.extrato:
            print(movimento)

    
class ContaCorrente(Conta):
    def __init__(self, usuario):
        super().__init__(usuario)
        self.saques = 3
        self.saque_max = 500

    def __str__(self):
        return f"Usuário: {self.usuario} - {self.agencia}-{self.conta:02}"

    def sacar(self, valor):
        if self.saques > 0:
            if valor <= self.saque_max:
                self.saques -= 1
                return super().sacar(valor)
            else:
                print(f'Valor máximo por saque é de R$ {self.saque_max:.2f}')
                return False
        else:
            print('Limite diário de saques atingido.\nVolte amanhã.')
            self.saques = 3
            return False
            