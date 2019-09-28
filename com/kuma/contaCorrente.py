class ContaCorrente:

    def __init__(self, numero, nomeCorrentista, saldo=0.0):
        self.numero = numero
        self.alterarNome(nomeCorrentista)
        self.saldo = saldo

    def alterarNome(self, nomeCorrentista):
        self.nomeCorrentista = nomeCorrentista

    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor

# TESTE DA CLASSE

'''conta = ContaCorrente(1222, 'pablo')
conta.alterarNome('julio')
conta.deposito(100)
print conta.saldo
conta.saque(100)
print conta.saldo'''