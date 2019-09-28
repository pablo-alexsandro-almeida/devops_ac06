class conta_corrente:
    '''
    conta corrente
    '''
    def __init__(self, numero, nomeCorrentista, saldo=0.0):
        self.numero = numero
        self.alterarNome(nomeCorrentista)
        self.saldo = saldo

    def alterarNome(self, nomeCorrentista):
        '''
        alterar nome
        '''
        self.nomeCorrentista = nomeCorrentista

    def deposito(self, valor):
        '''
        deposito
        '''
        self.saldo += valor

    def saque(self, valor):
        '''
        saque
        '''
        self.saldo -= valor

# TESTE DA CLASSE

'''conta = ContaCorrente(1222, 'pablo')
conta.alterarNome('julio')
conta.deposito(100)
print conta.saldo
conta.saque(100)
print conta.saldo'''
