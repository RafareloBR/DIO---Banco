from datetime import datetime

saldo = 0
extrato_bancario = []
contador_operacoes = 0
menu = -1
saque_maximo = 500
LIMITE_OPERACOES = 10
mascara_dia = "%d/%m/%Y"
dia_atual = datetime.now().strftime(mascara_dia)

def deposito (valor):

    global saldo    
    global contador_operacoes
    
    if valor > 0 and contador_operacoes < LIMITE_OPERACOES:

        saldo += valor

        data_operacao = datetime.now().strftime(mascara_dia)

        if data_operacao == dia_atual:
            contador_operacoes +=1
        
        extrato_bancario.append(["Depósito", valor, data_operacao])
        
        print("\nDepósito realizado com sucesso!\n")
    

    elif contador_operacoes >= LIMITE_OPERACOES:
        print("\nVocê já atingiu o número máximo de operações diárias.\n")

    else:
        print("\nValor inválido.\n")
    
    return saldo

def sacar (valor):

    global saldo
    global contador_operacoes

    if contador_operacoes < LIMITE_OPERACOES:

        if valor > 0 and valor <= saldo and valor <= saque_maximo:
            saldo -= valor
            contador_operacoes += 1
            data_operacao = datetime.now().strftime(mascara_dia)

            if data_operacao == dia_atual:
                contador_operacoes +=1

            extrato_bancario.append(["Saque", valor, data_operacao])
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
    print("\n=====EXTRATO BANCÁRIO=====\n")

    if extrato_bancario == []:
            print("Não existem transações a serem exibidas.")

    for modalidade, valor, data in extrato_bancario:
        print(f"{modalidade} - R$ {valor} | {data}")
    
    print("\n==========================\n")

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