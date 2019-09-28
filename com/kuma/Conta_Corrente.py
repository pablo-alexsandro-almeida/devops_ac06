class contacorrente:
    '''
    conta corrente
    '''
    def __init__(self, numero, nomecorrentista, saldo=0.0):
        self.numero = numero
        self.alterarNome(nomecorrentista)
        self.saldo = saldo

    def alterarnome(self, nomecorrentista):
        '''
        alterar nome
        '''
        self.nomecorrentista = nomecorrentista

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
