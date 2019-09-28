import pytest
from com.kuma.calcula_parcela import valorPagamento
from com.kuma.contaCorrente import ContaCorrente
from com.kuma.convertehora import converteHora


def test_deposito():
    '''
    teste para deposito
    '''
    contacorrente = contacorrente(1222, "pablo")
    contacorrente.deposito(100)
    assert contacorrente.saldo == 100, "Valor e 100"


def test_alterarnome():
    '''
    teste para alterar o nome
    '''
    contacorrente = contacorrente(1222, "pablo")
    contacorrente.alterar_Nome("julio")
    assert contacorrente.nomeCorrentista == "julio", " Era Pablo"


def test_saque():
    '''
    teste para saque
    '''
    contacorrente = contacorrente(1222, "pablo")
    contacorrente.saque(100)
    assert contacorrente.saldo == -100, "Valor e 100"


def test_retornarnone():
    '''
    teste para retornar o nome
    '''
    operacao = convertehora(24, 0)
    assert operacao == None, "Deveria ser None"


def test_retornarmeiodia():
    '''
    teste para retinar o meio dia
    '''
    operacao = convertehora(0, 10)
    assert operacao == "12:10 AM", "Deveria ser 12:10 AM"


def test_retornaronze():
    '''
    teste para retornar o o onze
    '''
    operacao = convertehora(9, 10)
    assert operacao == "09:10 AM", "Deveria ser 9:10 AM"


def test_retornarnone():
    '''
    teste para retornar o nome
    '''
    operacao = convertehora(13, 10)
    assert operacao == "01:10 PM", "Deveria ser 1:10 AM"


def test_doisdiasatraso():
    '''
    teste para os dias de atraso
    '''
    operacao = valorpagamento(100, 2)
    assert operacao == 105, "Deveria ser 105"


def test_valorzero():
    '''
    teste para o valor de zero
    '''
    operacao = valorpagamento(-1, 0)
    assert operacao == None, "Deveria ser 0"


def test_sematraso():
    '''
    teste para sem atraso
    '''
    operacao = valorpagamento(100, 0)
    assert operacao == 100, "Deveria ser 100"
