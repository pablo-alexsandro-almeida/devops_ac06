import pytest
from com.kuma.calcula_parcela import valorPagamento
from com.kuma.contaCorrente import ContaCorrente
from com.kuma.convertehora import converteHora

def test_deposito():
	contaCorrente = ContaCorrente(1222, "pablo")
	contaCorrente.deposito(100)
	assert contaCorrente.saldo == 100, "Valor e 100"
	
def test_alterarNome():
	contaCorrente = ContaCorrente(1222, "pablo")
	contaCorrente.alterarNome("julio")
	assert contaCorrente.nomeCorrentista == "julio", " Era Pablo"

def test_saque():
	contaCorrente = ContaCorrente(1222, "pablo")
	contaCorrente.saque(100)
	assert contaCorrente.saldo == -100, "Valor e 100"
	

def test_retornarNone():
	operacao = converteHora(24, 0)
	assert operacao == None, "Deveria ser None"
	
def test_retornarMeiodia():
	operacao = converteHora(0, 10)
	assert operacao == "12:10 AM", "Deveria ser 12:10 AM"

def test_retornarOnze():
	operacao = converteHora(9, 10)
	assert operacao == "09:10 AM", "Deveria ser 9:10 AM"
	
def test_retornarNone():
	operacao = converteHora(13, 10)
	assert operacao == "01:10 PM", "Deveria ser 1:10 AM"
    


def test_doisdiasAtraso():
	operacao = valorPagamento(100,2)
	assert operacao == 105, "Deveria ser 105"

def test_valorZero():
	operacao = valorPagamento(-1,0)
	assert operacao == None, "Deveria ser 0"
	
	
def test_semAtraso():
	operacao = valorPagamento(100,0)
	assert operacao == 100, "Deveria ser 100"

