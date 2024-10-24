# -*- coding: utf-8 -*-
# Estudantes: Sophya Ribeiro e Soraya Ferreira

# Bibliotecas para funções auxiliares
import random
import sys
import time
# Bibliotecas para visualização do gráfico
# import matplotlib.pyplot as plt
# import numpy as np
# Módulos dos algoritmos implementados
from dinamic import bottom_up_cut_rod
from greedy import greedy_cut_rod


# -------- GRAFICOS --------- #


# def gerar_grafico_tempo(tamanhos, tempos_dp, tempos_greedy, stp: int):
#     """
#     Essa função tem o objetivo de gerar o gráfico para melhor visualização dos tempos
#     de execução dos algoritmos. Ela recebe um vetor com todos os tamanhos de vetor testados,
#     listas com os tempos de execução de cada algoritmo, conforme o tamanho, um inteiro para
#     exibir o título do gráfico de acordo com a escolha de teste, e outro com o intervalo entre
#     as medições do gráfico, para melhor visualização dos valores.
#     """
#     fig, ax = plt.subplots()

#     ax.plot(tamanhos, tempos_dp, label='Dynamic Programming', marker='o')
#     ax.plot(tamanhos, tempos_greedy, label='Greedy', marker='o')

#     xticks_interval = stp
#     plt.xticks(fontsize=6)
#     xticks = np.arange(min(tamanhos), max(tamanhos) + xticks_interval, xticks_interval)
#     ax.set_xticks(xticks)

#     ax.set_xlabel('eixo x')
#     ax.set_ylabel('eixo y')

#     ax.set_title('Tempo de execução dos algoritmos')

#     ax.legend()
#     ax.grid(True)

#     plt.show()

# def gerar_grafico_vendas(tamanhos, venda_dp, venda_greedy, stp: int):
#     """
#     Essa função tem o objetivo de gerar o gráfico para melhor visualização dos tempos
#     de execução dos algoritmos. Ela recebe um vetor com todos os tamanhos de vetor testados,
#     listas com os tempos de execução de cada algoritmo, conforme o tamanho, um inteiro para
#     exibir o título do gráfico de acordo com a escolha de teste, e outro com o intervalo entre
#     as medições do gráfico, para melhor visualização dos valores.
#     """
#     fig, ax = plt.subplots()

#     ax.plot(tamanhos, venda_dp, label='Dynamic Programming', marker='o')
#     ax.plot(tamanhos, venda_greedy, label='Greedy', marker='o')

#     xticks_interval = stp
#     plt.xticks(fontsize=6)
#     xticks = np.arange(min(tamanhos), max(tamanhos) + xticks_interval, xticks_interval)
#     ax.set_xticks(xticks)

#     ax.set_xlabel('eixo x')
#     ax.set_ylabel('eixo y')

#     ax.set_title('Valor total de venda')

#     ax.legend()
#     ax.grid(True)

#     plt.show()

    
# ------ TESTE GERAL ---------------#

def gerar_precos(n: int) -> list:
    """
    Esta função recebe 'n' como o tamanho do vetor a ser 
    gerado e retorna uma lista com n números aleatórios, sendo
    que os valores dentro do vetor não podem ultrapassar o número 
    '2*n'.
    """
 
    numeros = [random.randint(0, 2*n) for _ in range(n)]
    return sorted(numeros)


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
    print(f"{'Tamanho (n)':<15}{'vDP':<15}{'tDP':<15}{'vGreedy':<15}{'tGreedy':<15}{'%':<15}")
    print("-" * 90) 

    vetor_precos = gerar_precos(fim)
    tempos_dinamic = []
    totais_venda_dinamic = []

    tempos_greedy = []
    totais_venda_greedy = []

    ind_testes = 0 
    # esse índice acompanha os testes p acessar posições respectivas dos vetores


    for n in range(inc, fim+1, stp):

        tamanhos_greedy  = [_ for _  in range(1, n + 1)]

        start = time.time()
        vdp = bottom_up_cut_rod(vetor_precos, n)
        end = time.time()
        tempos_dinamic.append(end - start)
        totais_venda_dinamic.append(vdp)

        start = time.time()
        vgreedy = greedy_cut_rod(tamanhos_greedy, vetor_precos)
        end = time.time()
        tempos_greedy.append(end - start)
        totais_venda_greedy.append(vgreedy)


        #diferenca = (vdp * 100 / 100 * vdp-vgreedy)

        diferenca = (vgreedy * 100) / vdp

        print(f"{n:<15}{totais_venda_dinamic[ind_testes]:<15}{tempos_dinamic[ind_testes]:<15.6f}{totais_venda_greedy[ind_testes]:<15}{tempos_greedy[ind_testes]:<15.6f}{diferenca:<12.2f}")

        ind_testes = ind_testes + 1
    print()

    
#----------- MAIN -----------#
def main():

    # Foi necessário aumentar o limite de chamadas recursivas do python
    sys.setrecursionlimit(100000)


    inc = int(input("\n\tParâmetro inc (tamanho inicial): "))
    fim = int(input("\tParâmetro fim (tamanho final): "))
    stp = int(input("\tParâmetro stp (intervalo entre os tamanhos): "))

    testar_algoritmos(inc, fim, stp)
           

if __name__ == '__main__':
    main()