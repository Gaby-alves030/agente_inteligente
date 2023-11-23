import copy
import matplotlib.pyplot as plt
from random import randint

cores = ['preto', 'roxo', 'rosa', 'vermelho', 'marrom', 'laranja', 'amarelo', 'verde', 'azul', 'preto']

tamanhoCombinacao = 10
tentativas = 100000

def geraCominacao(num):
    combinacao = []
    for c in range(num):
        combinacao.append(cores[randint(0, len(cores) - 1)])
    return combinacao

def caculaPontos(combinacao, tentativa):
    pontos = 0
    for i in range(len(combinacao)):
        if combinacao[i] == tentativa[i]:
            pontos += 1
    return pontos

def mudaCombinacao(tabuleiro):
    combinacao = tabuleiro
    pos = randint(0, len(combinacao) - 1)
    combinacao[pos] = cores[randint(0, len(cores) - 1)]
    return combinacao

def hillClimb():
    senha = geraCominacao(tamanhoCombinacao)
    tentativa = []
    for i in range(tamanhoCombinacao):
        tentativa.append(cores[0])
    pontosAtual = caculaPontos(senha, tentativa)
    pontosAnterior = pontosAtual
    counter = 0
    resultado = 'SUCESSO'
    pontuacaoHistorico = []
    while pontosAnterior != tamanhoCombinacao:
        tentativaNova = mudaCombinacao(copy.deepcopy(tentativa))
        pontosAtual = caculaPontos(senha, tentativaNova)
        if pontosAtual > pontosAnterior:
            tentativa = copy.deepcopy(tentativaNova)
            pontosAnterior = pontosAtual
        pontuacaoHistorico.append(pontosAnterior)
        if counter >= tentativas:
            resultado = 'FALHA'
            break
        counter += 1
        
    print(resultado)
    print(tentativa)
    x = range(len(pontuacaoHistorico))
    plt.plot(x, pontuacaoHistorico)
    plt.xlabel("Tentativas")
    plt.ylabel("Número de Acertos")
    plt.title("Variação da Função Objetivo")
    #plt.legend(loc="lower right")
    plt.show()
    
hillClimb()