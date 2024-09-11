from datetime import datetime
import unicodedata

saldo = 0
extrato_bancario = [] #Lista para armazenar as operações de extrato e saque
contador_operacoes = 0
menu = -1
saque_maximo = 500
LIMITE_OPERACOES = 10
mascara_dia = "%d/%m/%Y"
dia_atual = datetime.now().strftime(mascara_dia)
AGENCIA = "0001"
list_users ={} #Dicio para ter todas as informações de novos usuários
list_contas = {} #Dicio que correlaciona CPF, agência e conta corrente
contas_contador = 0

new_user = {

    "Conta Corrente" : {AGENCIA:[]}, 
    "Nome" : None,
    "Data de nascimento" : None,
    "CPF" : None,
    "Endereço" : {

        "Rua" : None,
        "Número" : None,
        "Bairro" : None,
        "Cidade" : None,
        "Estado" : None
    }
}

def get_state_abbreviation(state): #Uma função para filtrar o Estado

    frasenfd = unicodedata.normalize('NFD', state)
    
    state_sem_acentos = ''.join(c for c in frasenfd if not unicodedata.combining(c))
  
    state_cleaned = state_sem_acentos.lower()

    match state_cleaned:
        case 'acre':
            return 'AC'
        case 'alagoas':
            return 'AL'
        case 'amapa':
            return 'AP'
        case 'amazonas':
            return 'AM'
        case 'bahia':
            return 'BA'
        case 'ceara':
            return 'CE'
        case 'distrito federal':
            return 'DF'
        case 'espirito santo':
            return 'ES'
        case 'goias':
            return 'GO'
        case 'maranhao':
            return 'MA'
        case 'mato grosso':
            return 'MT'
        case 'mato grosso do sul':
            return 'MS'
        case 'minas gerais':
            return 'MG'
        case 'para':
            return 'PA'
        case 'paraiba':
            return 'PB'
        case 'parana':
            return 'PR'
        case 'pernambuco':
            return 'PE'
        case 'piaui':
            return 'PI'
        case 'rio de janeiro':
            return 'RJ'
        case 'rio grande do norte':
            return 'RN'
        case 'rio grande do sul':
            return 'RS'
        case 'rondonia':
            return 'RO'
        case 'roraima':
            return 'RR'
        case 'santa catarina':
            return 'SC'
        case 'sao paulo':
            return 'SP'
        case 'sergipe':
            return 'SE'
        case 'tocantins':
            return 'TO'

def format_cpf(cpf): #Função de máscara para o CPF - Remove ".", "," e "-"

    cleaned_cpf = str(cpf.replace('.', '').replace('-', '').replace(',', ''))

    return cleaned_cpf

def criar_usuario(): #Método para criar um usuário recebendo as informações do mesmo
    cpf = input("\nDigite o CPF para a criação de usuário:\nCPF: ")
    cpf_user = format_cpf(cpf)
    
    if cpf_user not in list_users.values():

        print("\nAgora precisamos te conhecer melhor...")

        user_name = input("\nDigite o seu nome completo\nNome: ")
        new_user["Nome"] = user_name

        user_birthday = input("\nDigite a data do seu nascimento\nData: ")
        new_user["Data de nascimento"] = user_birthday

        user_adress_street = input("\nAgora informe seu endereço, vamos começar pela rua\nRua: ")
        new_user["Endereço"]["Logradouro"] = user_adress_street

        user_adress_number = input("\nAgora informe o número\nNúmero: ")
        new_user["Endereço"]["Número"] = user_adress_number

        user_adress_neighborhood = input("\nAgora informe o bairro\nBairro: ")
        new_user["Endereço"]["Bairro"] = user_adress_neighborhood

        user_adress_city = input("\nQual o nome da sua cidade?\nCidade: ")
        new_user["Endereço"]["Cidade"] = user_adress_city

        user_adress_state = input("\nE por último o nome do seu estado\nEstado: ")
        new_user["Endereço"]["Estado"] = get_state_abbreviation(user_adress_state)

        list_users[cpf_user] = new_user
        list_contas[cpf_user] = new_user["Conta Corrente"]

        print(f"\nSeja bem-vindo, {user_name}. Seu usuário foi criado com sucesso!\n")

        return new_user["CPF"]

    else:
        print("CPF já cadastrado. Só é possível um CPF por usuário.")

def criar_conta_corrente():#Cria uma conta corrente já relaciona o CPF com a conta na list_contas

    catch_cpf = input("\nPara criar uma conta, digite seu CPF:\nCPF: ")
    cpf = format_cpf(catch_cpf)

    if cpf in list_contas:

        global contas_contador
        conta_user = contas_contador + 1

        list_contas[cpf][AGENCIA].append(conta_user)

        print(f"\nSua conta de número {conta_user} foi criada com sucesso.")

        return conta_user

    else:
        print("\nSeu CPF não está cadastrado. Antes de criar uma conta, crie um usuário.")
    
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

    menu = int(input(

    '''\nSelecione uma opção:\n
    [0] - Sair\n
    [1] - Depositar\n
    [2] - Sacar\n
    [3] - Extrato\n
    [4] - Criar um usuário\n
    [5] - Criar uma conta corrente\n
    Opção Desejada: '''))

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
        
        case 4:
            criar_usuario()
        
        case 5:
            criar_conta_corrente()

print("\nSessão Finalizada.\n")