from time import sleep
from classes import *

def linha():
    print("\033[38;5;129m-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")


todasContas = []

linha()
print("\033[38;5;129mBem vindo ao Bancool!")
print("Qual operação deseja realizar?")
print("1 - Adicionar Cliente\n2 - Sacar\n3 - Verificar se Cliente é cadastrado no Banco\n4 - Adicionar Saldo\n0 - Cancelar atendimento")
operacao = int(input())
linha()

while True:
    match operacao:
        case 1:
            agencia = int(input("Agência: "))
            numeroConta = int(input("Número da conta: "))
            saldo = float(input("Saldo inicial: "))
            tipoConta = str(input("Tipo da conta (Corrente / Poupanca): ")).upper()
            if tipoConta[0].strip() == "C":
                conta = ContaCorrente(agencia, numeroConta, saldo)
            elif tipoConta[0].strip() == "P":
                conta = ContaPoupanca(agencia, numeroConta, saldo)
            else:
                print("Tipo de conta errado!")
            nomeCliente = str(input("Nome do titular da conta: "))
            idadeCliente = int(input("Idade do Titular: "))
            cliente = Cliente(nomeCliente, idadeCliente, conta)
            banco = Banco(conta, cliente)
            if banco.verificaAgencia(cliente):
                todasContas.append(banco)
                linha()
                print("Conta criada com sucesso!")
            else:
                linha()
                print("Não foi possivel adicionar a conta!")
            
        case 2:
            numero = int(input("Número da conta: "))
            nome = str(input("Nome do Titular: "))
            agencia = int(input("Agencia do Titular: "))
            existe = False
            for c in todasContas:
                if c._conta.NumeroConta == numero and c._cliente.Nome == nome and c._conta.Agencia == agencia:
                    existe == True
                    banco = c
            if existe:                
                continuar = True
                while continuar:
                    print(f"Saldo atual: {banco._conta.Saldo}\nLimite atual: {banco._conta.Limite}")
                    valor = float(input("Quanto deseja sacar? R$ "))
                    banco._conta.Sacar(valor)
                    print(f"O valor de {valor} foi sacado da sua conta!")
                    print(f"Deseja fazer um novo saque?")
                    cont = str(input("(Sim / Nao) "))
                    if cont[0].upper().strip() == "N":
                        continuar = False
            else:
                linha()
                print(f"Algum dado informado está incorreto ou o cliente não possui conta neste banco!")
                sleep(2)
            
        case 3:
            existe = False
            numero = int(input("Número da conta: "))
            nome = str(input("Nome do Titular: "))
            agencia = int(input("Agencia do Titular: "))
            existe = False
            for c in todasContas:
                if c._conta.NumeroConta == numero and c._cliente.Nome == nome and c._conta.Agencia == agencia:
                    banco = c
            if banco.verificaAgencia(banco):
                linha()
                print(f"Agência: {banco._conta.Agencia}\nNumero da conta: {banco._conta.NumeroConta}\nSaldo em conta: {banco._conta.Saldo}\nTipo da conta: {banco._conta.__class__.__name__}\nNome do Titular: {banco._cliente.Nome}\nIdade do Titular: {banco._cliente.Idade}")
                sleep(5)
            else:
                linha()
                print("Não existe uma conta com estes dados informados!")
                sleep(1)
        
        case 4:
            existe = False
            numero = int(input("Número da conta: "))
            nome = str(input("Nome do Titular: "))
            agencia = int(input("Agencia do Titular: "))
            for c in todasContas:
                if c._conta.NumeroConta == numero and c._cliente.Nome == nome and c._conta.Agencia == agencia:
                    banco = c
            existe = banco.verificaAgencia(banco)
            if existe:
                linha()
                adicionar = float(input("Saldo a Adicionar: R$ "))
                print(f"Aguardando inserção do dinheiro...")
                sleep(2)
                banco._conta.Saldo += adicionar
                print(f"Seu saldo antigo de R$ {banco._conta.Saldo - adicionar} agora é de R${banco._conta.Saldo}")
                sleep(2)
            else:
                linha()
                print(f"Não existe uma conta com estes dados informados!")
                sleep(2)
        case _:
            False
            break
    
    linha()
    print("Qual operação deseja realizar agora?")
    print("1 - Adicionar Cliente\n2 - Sacar\n3 - Verificar se Cliente é cadastrado no Banco\n4 - Adicionar Saldo\n0 - Cancelar atendimento")
    operacao = int(input())
    linha()

linha()  
print(f"Nós do Bancool agradecemos sua visita!")
linha()