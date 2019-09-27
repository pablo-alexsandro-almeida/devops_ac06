class ContaCorrente:
	'''
	classe para conta corrente
	'''
	def __init__(self, numero, nomeCorrentista, saldo = 0.0):		
	self.numero = numero
        self.alterar_Nome(nomeCorrentista)
        self.saldo = saldo

    def alterar_Nome(self, nomeCorrentista):
		'''
		metodo parar o nome 
		'''
        self.nomeCorrentista = nomeCorrentista

    def deposito(self, valor):
		'''
		metodo para fazer deposito
		'''
        self.saldo += valor

    def saque(self, valor):
		'''
		metodo para fazer saque
		'''
        self.saldo -= valor

# TESTE DA CLASSE

'''conta = ContaCorrente(1222, 'pablo')
conta.alterarNome('julio')
conta.deposito(100)
print conta.saldo
conta.saque(100)
print conta.saldo'''
