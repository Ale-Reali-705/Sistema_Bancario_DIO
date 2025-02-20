class Cliente:
    def __init__(self, nome, cpf, data, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data = data
        self.endereco = endereco
        self.contas = []

    def __str__(self):
        return f"Cliente: {self.nome} - {self.cpf}"
    
    def criar_conta_corrente(self):
        conta = ContaCorrente(self.nome)
        self.contas.append(conta)
        contas.append(conta)
        print("Conta corrente criada com sucesso.")


class Conta:
    def __init__(self, usuario):
        self.usuario = usuario
        self.agencia = '0001'
        self.conta = len(contas) + 1
        self.saldo = 0
        self.saques = 0
        self.extrato = []

    def __str__(self):
        return f"Conta: {self.usuario} - {self.agencia}-{self.conta:02}\nSaldo: R$ {self.saldo:.2f}"

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito:{' ' * 50-(len(f"Depósito:R$ {valor:.2f}"))}R$ {valor:.2f}")
            return True
        else:
            print('Valor inválido.')
            return False
        
    def sacar(self, valor):
        if self.saques == 0:
            if self.saldo >= valor:
                self.saldo -= valor
                self.saques -= 1
                self.extrato.append(f"Saque:{' ' * 50-(len(f"Saque:R$ {valor:.2f}"))}R$ {valor:.2f}")
                return True
            else:
                print('Saldo insuficiente.')
                return False
        else:
            print('Limite diário de saques atingido.\nVolte amanhã.')
            self.saques = 3
            return False
        
    def mostrar_extrato(self):
        if self.extrato:
            for movimento in self.extrato:
                print(movimento)

    
class ContaCorrente(Conta):
    def __init__(self, usuario):
        super().__init__(usuario)
        self.saques = 3

    def __str__(self):
        return "CONTA CORRENTE".center(50) + f"\n{self.usuario} - {self.agencia}-{self.conta:02}\nSaldo: R$ {self.saldo:.2f}"