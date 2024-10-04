from abc import ABC, abstractmethod

menu = -1
AGENCIA = "0001"
contas_contador = 0
LIMITE_SAQUES = 5
lista_clientes = []

def verifica_cadastro(cpf):

    if cpf not in lista_clientes:
        print("Você não está cadastrado em nosso banco. Antes de criar uma conta bancária, crie seu cadastro.")
        return False
    
    else:
        return True

def add_cadstro(cpf):
    lista_clientes.append(cpf)

class Transacao(ABC):
    @property
    def valor(self):#
        pass

    @abstractmethod
    def registrar(self, conta): #
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor (self):
        return self._valor

    def registrar (self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor (self):
        return self._valor

    def registrar (self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Conta:

    def __init__(self, numero, agencia, cliente, historico):

        self._saldo = 0
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        self._cliente = cliente
        self._numero = numero

    @property
    def saldo(self): #Retorna o saldo
        return self._saldo

    @property
    def numero_conta(self): #Retorna o numero da conta
        return self._numero
    
    @property
    def agencia(self): #Retorna a agência
        return self._agencia
    
    @property
    def cliente(self): #Retorna o cliente
        return self._cliente

    def sacar(self, valor): 
        saldo = self._saldo
        excedeu_saldo = valor > saldo
    
        if excedeu_saldo:
            print("Você não possui saldo suficiente.")
            return False
        
        elif valor > 0:
            self._saldo -= valor
            print("Saque realizado com sucesso!")
            return True
        
        else:
            print("O valor inserido é inválido.")
            return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Deposito realizado com sucesso.")
        else:
            print("O valor informado é inválido.")
            return False
        return True

class ContaCorrente(Conta):

    def __init__(self, numero, agencia, cliente, limite = 500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

class Historico:
    def adicionar_transacao(self, transacao): 
        self.transacao = transacao


        pass

class Deposito(Transacao):

    def __init__(self, valor):
        self._valor = valor

class Saque(Transacao):

    def __init__(self, valor):
        self._valor = valor

class Cliente:

    def __init__(self, cpf, endereco, contas = []):
        self._cpf = cpf
        self._endereco = endereco
        self._contas = contas or []
    
    def realizar_transacao(self, conta, transacao):#
        pass

    def adicionar_conta(self, conta):
        self._contas.append(conta)
    
    def mostrar_contas(self):
        for conta in self._contas:
            print(f"Conta: {conta._numero} | Saldo = {conta._saldo}")

print("\nSelecione uma opção:")

while menu != 0:

    print("""
    [1] - Cadastro
    [2] - Criar conta
    [3] - Criar conta corrente
    [4] - Realizar um saque
    [5] - Realizar um depósito
    [6] - Extrato
    [7] - Sair
    """)

    menu = int(input("Opção desejada: "))

    match(menu):

        case 1: 
            print("\nVamos precisar uma informação...\n")

            cpf_input = input("Digite seu CPF: ")
            endereco_input = input("Digite o seu endereço: ")

            novo_cliente = Cliente(cpf = cpf_input, endereco = endereco_input)

            lista_clientes.append(novo_cliente._cpf)
            print("\nCadastro Finalizado!")
                    
        case 2:
            
            verificar_cad = input("\nVamos verificar seu cadastro, informe seu CPF.\nCPF:")

            verifica_cadastro(verificar_cad)

            if verifica_cadastro(verificar_cad)==True:

                add_cadstro(verificar_cad)
                print("\nCPF encontrado!\n")
                print("\nCriando sua conta...\n")
                new_conta = Conta(numero=contas_contador+1, agencia=AGENCIA, cliente = novo_cliente, historico=Historico())
                contas_contador += 1
                
                print("\nConta criada com sucesso.")

        case 4:

            valor_saque = input("\nDigite o valor para sacar:\nValor: ")
            new_conta.sacar(valor_saque)        



        case 3:
            print("\nCriando sua conta corrente...")
            new_conta.nova_conta(new_conta._cliente, numero = contas_contador+1)
                    
        case 6:
            print("\nSaindo do sistema...\n")
            break



