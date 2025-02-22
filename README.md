# Desafio de projeto "Sistema Bancário"
O código é um desafio proprosto pela DIO como parte do curso "Suzano - Python Developer", como forma de praticar o que foi ensinado nas aulas.  

## 1ª Fase
### O projeto teve apenas 3 funções:  
#### Depositar  
  Acrescenta um valor digitado pelo terminal ao saldo.

#### Sacar  
  Subtraía um valor digitado pelo terminal, desde que cumprisse os requisitos de saque máximo e saques diários.
  
#### Visualizar extrato  
  Registra toda movimentação feita pelo usuário (saque ou depósito).

## 2ª Fase
### Foi adicionado ao projeto uma lista com usuários e outra lista de contas correntes, além das funções: 
#### Criar usuário  
  Adiciona um registro contendo nome, CPF e residencia de um usuário. Também verificava apenas um CPF por usuário.
  
#### Criar conta corrente  
  Adicionava um registro contendo nome, agencia-conta, saldo, extrato e saques diários de um usuário. Verifica número da sequência da agencia-conta será utilizada. Um usuário pode ter mais de 1 conta.
  
#### Visualizar contas corrente  
  Lista quais contas o usuário possui, mostrando qual agencia-conta relaciona com qual usuário.
  
#### Selecionar conta  
  Seleciona, atraves do nome de usuário e o número da agencia-conta, qual será a conta/registro que utilizará as funções criadas na 1ª fase.

## 3ª Fase
### Foi implementado classes ao projeto:
#### Classe Usuário
  Possui nome, CPF e endero do usuário. Podendo criar contas correntes e listar as contas que o usuário possui.

#### Classe Conta
  Criada a partir de um usuário, contem o saldo e número da conta, além de servir de base para a Classe ContaCorrente. Possui funções básicas de deposito, saque e mostrar o extrado.

#### Classe ContaCorrente
  Adquire as funções da Classe Conta. É adicionádo a caractertísicas de limite de saque diário e valor máximo por saque, as quais são requisitos que são atribuídos à função sacar.