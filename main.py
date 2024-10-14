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
 
    # 'n' limitação para manter o tempo do counting sort linear
    numeros = [random.randint(0, n) for _ in range(n)]
    return numeros


'''
def gerar_grafico(tamanhos, tempos_bubble, tempos_insertion, tempos_merge, tempos_quick, tempos_heap, tempos_counting, escolha: int, stp: int):
    """
    Essa função tem o objetivo de gerar o gráfico para melhor visualização dos tempos
    de execução dos algoritmos. Ela recebe um vetor com todos os tamanhos de vetor testados,
    listas com os tempos de execução de cada algoritmo, conforme o tamanho, um inteiro para
    exibir o título do gráfico de acordo com a escolha de teste, e outro com o intervalo entre
    as medições do gráfico.
    """
    fig, ax = plt.subplots()

    ax.plot(tamanhos, tempos_bubble, label='Bubble', marker='o')
    ax.plot(tamanhos, tempos_insertion, label='Insertion', marker='o')
    ax.plot(tamanhos, tempos_merge, label='Merge', marker='o')
    ax.plot(tamanhos, tempos_quick, label='Quick', marker='o')
    ax.plot(tamanhos, tempos_heap, label='Heap', marker='o')
    ax.plot(tamanhos, tempos_counting, label='Counting', marker='o')

    xticks_interval = stp
    plt.xticks(fontsize=6)
    xticks = np.arange(min(tamanhos), max(tamanhos) + xticks_interval, xticks_interval)
    ax.set_xticks(xticks)

    ax.set_xlabel('eixo x')
    ax.set_ylabel('eixo y')

    if escolha == 1 :
        ax.set_title('title1')
    elif escolha == 2:
        ax.set_title('title2')
    elif escolha == 3:
        ax.set_title('title3')
    else:
        # Se a escolha for 4
        ax.set_title('title4')
    ax.legend()
    ax.grid(True)

    plt.show()

--------------------------------------
#linhas que imprimem tabela: 
print(f"{'Tamanho':<10}{'Dinamic':<10}{'Greedy':<10}")
print(f"{n:<10}{tempos_dinamic[indice_tempos]:<10.6f}{tempos_greedy[indice_tempos]:<10.6f}")
'''

#----------- MAIN -----------#
def main():

    # Foi necessário aumentar o limite de chamadas recursivas do python
    sys.setrecursionlimit(100000)

    print("\n\
          \t[1] Testar;\n\
           \t[2] Testar ;\n\
           \t[3] Testar ;\n\
           \t[4] Testar ;\n\
           Escolha: ", end='')   
    escolha = int(input())

    inc = int(input("\tParâmetro inc (tamanho inicial do vetor): "))
    fim = int(input("\tParâmetro fim (tamanho final do vetor): "))
    stp = int(input("\tParâmetro stp (intervalos entre os tamanhos): "))

    if escolha == 1:
        start = time.time()

        end = time.time()
        print(f"\nTempo total: {(end-start)//60}")

    elif escolha == 2:
        start = time.time()
        
        end = time.time()
        print(f"\nTempo total: {(end-start)//60}")

    elif escolha == 3:
        start = time.time()
        
        end = time.time()
        print(f"\nTempo total: {(end-start)//60}")

    elif escolha == 4:
        start = time.time()
        
        end = time.time()
        print(f"\nTempo total: {(end-start)//60}")

    else:
        print("Escolha inválida!")
           

if __name__ == '__main__':
    main()