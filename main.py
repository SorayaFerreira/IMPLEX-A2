# -*- coding: utf-8 -*-
# Estudantes: Sophya Ribeiro e Soraya Ferreira

# Bibliotecas para funções auxiliares
import random
import sys
import time
# Bibliotecas para visualização do gráfico
import matplotlib.pyplot as plt
import numpy as np
# Módulos dos algoritmos implementados
from dinamic import bottom_up_cut_rod
from greedy import greedy_cut_rod



def gerar_precos(n: int) -> list:
    """
    Esta função recebe 'n' como o tamanho do vetor a ser 
    gerado e retorna uma lista com n números aleatórios, sendo
    que os valores dentro do vetor não podem ultrapassar o número 
    '2*n'.
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
# ------ TESTE GERAL ---------------#

def testar_algoritmos(inc: int, fim: int, stp: int):
    """
    Esta função chama os algoritmos de solução do problema 
    do Corte da Tora e executa todos os testes, conforme
    o tamanho total da tora de madeira. Recebe o tamanho inicial
    (inc), final (fim) e intervalos entre eles (stp). Ela armazena,
    em vetores, os tempos de execução de cada, os valores de venda,
    e realiza a contagem do número de acertos do algoritmo guloso.
    """


    print()
    print(f"{'n':<8}{'vDP':<9}{'tDP':<10}{'vGreedy':<10}{'tGreedy':<10}{'%':<10}")

    vetor_precos = gerar_precos(fim)
    tempos_dinamic = []
    totais_venda_dinamic = []

    tempos_greedy = []
    totais_venda_greedy = []

    ind_testes = 0 
    # esse índice acompanha os testes p acessar posições respectivas dos vetores.

    for n in range(inc, fim+1, stp):

        start = time.time()
        vdp = bottom_up_cut_rod(vetor_precos, n)
        end = time.time()
        tempos_dinamic.append(end - start)
        totais_venda_dinamic.append(vdp)

        start = time.time()
        vgreedy = greedy_cut_rod(vetor_precos, n)
        end = time.time()
        tempos_greedy.append(end - start)
        totais_venda_greedy.append(vgreedy)

    #print(f"{n:<10}{totais_venda_dinamic[]:<10.6f}{tempos_dinamic[]:<10.6f}{totais_venda_greedy[]:<10.6}{tempos_greedy[]}}{}")

    
'''

# ------ PROGRAMAÇÃO DINÂMICA ------- #

def executar_dp():

    ##codigo etc etc

    print()
    print(f"{'n':<8}{'vDP':<9}{'tDP':<10}{'vGreedy':<10}{'tGreedy':<10}{'%':<10}")


# ----------- GULOSO ------------- #

def testar_greedy():

    ##codigo etc etc

    print()
    print(f"{'n':<8}{'vDP':<9}{'tDP':<10}{'vGreedy':<10}{'tGreedy':<10}{'%':<10}")
'''

#----------- MAIN -----------#
def main():

    # Foi necessário aumentar o limite de chamadas recursivas do python
    sys.setrecursionlimit(100000)


    inc = int(input("\tParâmetro inc (tamanho inicial da tora de madeira): "))
    fim = int(input("\tParâmetro fim (tamanho final): "))
    stp = int(input("\tParâmetro stp (intervalo entre os tamanhos): "))

    #criar vetor com os tamanhos
    #tamanhos
    # ^ precisa não fia, o alg faz sozinho, ele é smart clever

    #criar vetores para armazenar os dados de vendas
    #venda_dp, venda_greedy

    #criar vetores para armazenar os tempos de execuçao dos algoritmos
    #tempo_dp, tempo_greedy

           
    testar_dp()
    testar_greedy()

    gerar_grafico_tempo(tamanhos, tempo_dp, tempo_greedy)
    gerar_grafico_vendas(tamanhos, venda_dp, venda_greedy)

if __name__ == '__main__':
    main()