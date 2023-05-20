from abc import ABC, abstractmethod
from random import randint

# Classes remetentes a CONTA

class Conta(ABC):
    def __init__(self, Agencia, NumeroConta, Saldo):
        self._agencia = Agencia
        self._numeroConta = NumeroConta
        self._saldo = Saldo
    
    @property
    def Agencia(self):
        return self._agencia

    @Agencia.setter
    def Agencia(self, AgenciaCliente):
        self._agencia = AgenciaCliente
    
    @property
    def NumeroConta(self):
        return self._numeroConta
    
    @NumeroConta.setter
    def NumeroConta(self, NumeroContaCliente):
        self._numeroConta = NumeroContaCliente
    
    @property
    def Saldo(self):
        return self._saldo

    @Saldo.setter
    def Saldo(self, SaldoCliente):
        self._saldo = SaldoCliente

    @abstractmethod
    def Sacar(self, Valor) -> str:...

class ContaCorrente(Conta):
    def __init__(self, Agencia, NumeroConta, Saldo):
        super().__init__(Agencia, NumeroConta, Saldo)
        self._limite = randint(100, 2000)
    
    @property
    def Limite(self):
        return self._limite
    
    @Limite.setter
    def Limite(self):
        novoLimite = randint(self._limite, self._limite + 1000)
        if novoLimite < self._limite:
            print(f"O novo limite não pode ser liberado")
        else:
            print(f"O limite foi alterado para R${self._limite}")
    
    def Sacar(self, Valor) -> str:
        if Valor > (self._saldo + self._limite):
            return print(f"O valor de R$ {Valor:.2f} não pode ser sacado!")
        else:
            self._saldo = self._saldo - Valor
            return print(f"O valor de R$ {Valor:.2f} foi sacado, saldo atual: {self._saldo:.2f}")

class ContaPoupanca(Conta):
    def __init__(self, Agencia, NumeroConta, Saldo):
        super().__init__(Agencia, NumeroConta, Saldo)
        self._limite = randint(50, 1000)
    
    @property
    def Limite(self):
        return self._limite
    
    @Limite.setter
    def Limite(self):
        novoLimite = randint(self._limite, self._limite + 1000)
        if novoLimite < self._limite:
            print(f"O novo limite não pode ser liberado")
        else:
            print(f"O limite foi alterado para R${self._limite}")

    def Sacar(self, Valor) -> str:
        if Valor > (self._saldo + self._limite):
            return print(f"O valor de R$ {Valor:.2f} não pode ser sacado!")
        else:
            self._saldo = self._saldo - Valor
            return print(f"O valor de R$ {Valor:.2f} foi sacado, saldo atual: {self._saldo:.2f}")

# Classes remetentes a CLIENTE

class Pessoa(ABC):
    def __init__(self, Nome, Idade):
        self._nome = Nome
        self._idade = Idade
    
    @property
    def Nome(self):
        return self._nome
    
    @Nome.setter
    def Nome(self, NomeCliente):
        self._nome = NomeCliente

    @property
    def Idade(self):
        return self._idade

    @Idade.setter
    def Idade(self, IdadeCliente):
        self._idade = IdadeCliente
    
class Cliente(Pessoa):
    def __init__(self, Nome, Idade, Conta):
        super().__init__(Nome, Idade)
        self._conta = Conta

# Classes remetentes ao BANCO

class Banco:
    def __init__(self, Conta, Cliente):
        self._conta = Conta
        self._cliente = Cliente
        self._agenciaBanco = 22
    
    def verificaAgencia(self, Cliente) -> bool:
        if Cliente._conta._agencia == self._agenciaBanco:
            return True
        else:
            return False  
    
    
