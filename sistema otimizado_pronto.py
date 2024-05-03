menu = """

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Criar Usuário
    [5] Criar conta corrente
    [6] Sair

"""


saldo = 1000 
limite_valor = 500
limite_saques = 3
numero_saques = 0
deposito = 0 
saque = 0
extrato = ""
usuarios = []
contas = []


def depositar(saldo, deposito, extrato , /):
    
    
    if deposito >= 0:
        print(f"R$ {deposito:.2f}")
        saldo = (saldo + deposito)
        extrato += f"Depósito: R$ {deposito:.2f}\n"
        print(f"operação feita, novo saldo R$ {saldo:.2f}")       
    else:
        print("Operação restrita: valor inválido. Voltando ao menu")
    
    return saldo, extrato

def sacar (* , saldo, saque, extrato, limite_valor, numero_saques, limite_saques):
   
    if saque > saldo:
        print ("Saldo indisponível. Voltando ao menu")
    elif saque <= saldo and saque >= limite_valor:
        print("limite indisponivel, voltando ao menu")
    elif saque <= saldo and saque <= limite_valor:
        if numero_saques < limite_saques:
            print("saque efetuado, retire o dinheiro no caixa")
            saldo = (saldo - saque)
            numero_saques += 1
            extrato += f"Saque: R$ {saque:.2f}\n"
            print(f"numero de saques realizados" , numero_saques)
        elif numero_saques >= limite_saques:
            print(f"numero de saques atingido. saques realizados: " , numero_saques , "de " , limite_saques )
    
    return saldo , extrato , numero_saques

def exibir_extrato ( saldo , extrato ):
    
    if deposito > 0 or saque > 0:
        print(extrato)
        print(f"saldo atual R$ {saldo:.2f}\n")
    else:
        print("não foram realizadas operações")
    
def criar_usuario(usuarios):
    cpf = input("Informe o numero de cpf - somente numeros: ")
    usuario = verificar_usuarios(cpf , usuarios)
    if usuario:
        print("usuario existente")
        return
    
    nome = input("Informe o nome completo: ")
    data_nasci = input ("Informe a data de nascimento (dd/mm/aa): ")
    endereco = input("informe o endereço: ")
    print("Novo usuario cadastrado")
    usuarios.append({"nome" : nome , "data_nasci": data_nasci , "endereco": endereco , "cpf": cpf})
    
def verificar_usuarios(cpf, usuarios):
    usuarios_verificados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_verificados[0] if usuarios_verificados else None
    
def criar_conta(contas):

    usuario = input("informe o usuário: ")
    conta = input("informe o numero da conta (começando em 1): ")
    usuario1 = verificar_conta(conta , contas)
    if usuario1:
        print("conta existente")
        return

    agencia = input("informe o numero da agencia: (deve ser 0001) ")
    if agencia == "0001":
        print("cadastrado")
        contas.append({"agencia": agencia , "conta": conta, "usuario": usuario})
    else:
        print("formato de agencia invalido")
        return

def verificar_conta(conta , contas):
    contas_verificadas = [usuario1 for usuario1 in contas if usuario1["conta"] == conta]
    return contas_verificadas[0] if contas_verificadas else None
    

while True:
    opcao = input(menu)
    if opcao == "1":
        print("---------------Deposito---------------")
        deposito = float (input ("informe o valor que deseja depositar:\n "))
        saldo , extrato = depositar( saldo, deposito, extrato)
    elif opcao == "2":
        print("---------------Saque---------------")
        print(f"Saldo disponivel R$  {saldo:.2f}")
        saque = float (input("informe o valor desejado para saque:\n "))
         
        saldo , extrato , numero_saques = sacar(saldo = saldo , saque = saque , extrato = extrato, limite_valor = limite_valor,
      numero_saques = numero_saques , limite_saques= limite_saques)
    elif opcao == "3":
        print("---------------Extrato---------------")
        exibir_extrato(saldo , extrato)
    elif opcao == "4":
        criar_usuario(usuarios)
    elif opcao == "5":
        criar_conta(contas)
    elif opcao == "6":
        break
    
    else:
        print("Operação inválida, por favor selecione a opção desejada")





