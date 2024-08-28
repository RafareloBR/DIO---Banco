saldo = 0
extrato_bancario = {"Depósito":[], "Saque":[]}
contador_saques = 0
menu = -1
saque_maximo = 500
LIMITE_SAQUES = 3

def deposito (valor):

    global saldo    
    
    if valor > 0:
        saldo += valor
        extrato_bancario["Depósito"].append(valor)
        print("\nDepósito realizado com sucesso!\n")
    return saldo

def sacar (valor):

    global saldo
    global contador_saques

    if contador_saques < LIMITE_SAQUES:

        if valor > 0 and valor <= saldo and valor <= saque_maximo:
            saldo -= valor
            contador_saques += 1
            extrato_bancario["Saque"].append(valor)
            print("\nSaque realizado com sucesso!\n")
            
        elif valor < 0 or valor == 0:
            print("\nValor não aceitável.\n")

        elif valor > saque_maximo:
            print("\nO valor máximo de saque é R$500.0\n")
        
        elif valor > saldo and saldo == 0:
            print("\nSaldo insuficiente.\n ")
        
    else:
        print("\nVocê já atingiu o limite máximo de saques hoje.\n")
    
    return saldo

def extrato():
    print("=====EXTRATO BANCÁRIO=====")

    if extrato_bancario["Depósito"] == [] and extrato_bancario["Saque"] == [] :
            print("Não existem transações a serem exibidas.")

    for modalidade, valor in extrato_bancario.items():
        for item in valor:
            print(f"{modalidade} - R$ {item}")

while menu != 0:

    menu = int(input("Selecione uma opção: \n\n[0] - Para sair\n[1] - Para depositar \n[2] - Para sacar \n[3] - Para vizualizar o extrato \n\nOpção Desejada: "))

    match(menu):

        case 1:
            valor_deposito = float(input("Operação de Depósito - Informe o valor: "))
            deposito(valor_deposito)
        
        case 2:
            valor_saque = float(input("Operação de Saque - Informe o valor: "))
            sacar(valor_saque)
    
        case 3:
            extrato()
            print("\n")

print("\nSessão Finalizada.\n")