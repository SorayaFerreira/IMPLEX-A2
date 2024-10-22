# -*- coding: utf-8 -*-
# Estudantes: Sophya Ribeiro e Soraya Ferreira

# Bibliotecas para funções auxiliares
import random
import sys
import time
# Bibliotecas para visualização do gráfico
import matplotlib.pyplot as plt
import numpy as np
import random


def gerar_numeros_aleatorios(n: int) -> list:
    """
    Esta função recebe 'n' como o tamanho do vetor a ser 
    gerado e retorna uma lista com n números aleatórios, sendo
    que os valores dentro do vetor não podem ultrapassar o número 
    'n'.
    """
 
    numeros = [random.randint(0, 2*n) for _ in range(n)]
    return numeros.sort()



def gerar_grafico_tempo(tamanhos, tempos_dp, tempos_greedy, stp: int):
    """
    Essa função tem o objetivo de gerar o gráfico para melhor visualização dos tempos
    de execução dos algoritmos. Ela recebe um vetor com todos os tamanhos de vetor testados,
    listas com os tempos de execução de cada algoritmo, conforme o tamanho, um inteiro para
    exibir o título do gráfico de acordo com a escolha de teste, e outro com o intervalo entre
    as medições do gráfico, para melhor visualização dos valores.
    """
    fig, ax = plt.subplots()

    ax.plot(tamanhos, tempos_dp, label='Dynamic Programming', marker='o')
    ax.plot(tamanhos, tempos_greedy, label='Greedy', marker='o')

    xticks_interval = stp
    plt.xticks(fontsize=6)
    xticks = np.arange(min(tamanhos), max(tamanhos) + xticks_interval, xticks_interval)
    ax.set_xticks(xticks)

    ax.set_xlabel('eixo x')
    ax.set_ylabel('eixo y')

    ax.set_title('Tempo de execução dos algoritmos')

    ax.legend()
    ax.grid(True)

    plt.show()

def gerar_grafico_vendas(tamanhos, venda_dp, venda_greedy, stp: int):
    """
    Essa função tem o objetivo de gerar o gráfico para melhor visualização dos tempos
    de execução dos algoritmos. Ela recebe um vetor com todos os tamanhos de vetor testados,
    listas com os tempos de execução de cada algoritmo, conforme o tamanho, um inteiro para
    exibir o título do gráfico de acordo com a escolha de teste, e outro com o intervalo entre
    as medições do gráfico, para melhor visualização dos valores.
    """
    fig, ax = plt.subplots()

    ax.plot(tamanhos, venda_dp, label='Dynamic Programming', marker='o')
    ax.plot(tamanhos, venda_greedy, label='Greedy', marker='o')

    xticks_interval = stp
    plt.xticks(fontsize=6)
    xticks = np.arange(min(tamanhos), max(tamanhos) + xticks_interval, xticks_interval)
    ax.set_xticks(xticks)

    ax.set_xlabel('eixo x')
    ax.set_ylabel('eixo y')

    ax.set_title('Valor total de venda')

    ax.legend()
    ax.grid(True)

    plt.show()


# ------ PROGRAMAÇÃO DINÂMICA ------- #

def testar_dp():

    ##codigo etc etc

    print()
    print(f"{'n':<8}{'vDP':<9}{'tDP':<10}{'vGreedy':<10}{'tGreedy':<10}{'%':<10}")


# ----------- GULOSO ------------- #

def testar_greedy():

    ##codigo etc etc

    print()
    print(f"{'n':<8}{'vDP':<9}{'tDP':<10}{'vGreedy':<10}{'tGreedy':<10}{'%':<10}")

#----------- MAIN -----------#
def main():

    # Foi necessário aumentar o limite de chamadas recursivas do python
    sys.setrecursionlimit(100000)


    inc = int(input("\tParâmetro inc (tamanho inicial do vetor): "))
    fim = int(input("\tParâmetro fim (tamanho final do vetor): "))
    stp = int(input("\tParâmetro stp (intervalos entre os tamanhos): "))
           
    testar_dp()
    testar_greedy()

    gerar_grafico_tempo()
    gerar_grafico_vendas()

if __name__ == '__main__':
    main()