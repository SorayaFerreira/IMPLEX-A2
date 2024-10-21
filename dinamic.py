# -*- coding: utf-8 -*-
# Estudantes: Sophya Ribeiro e Soraya Ferreira



"""
PENDÊNCIAS:
    Ordenar de modo não decrescente a lista de preços;
    A main() faz um pequeno teste, não testando com a lista de aleatórios;
    A lista de preços deve ser igual para todos os casos de teste? Ou gero listas diferentes a cada teste?
"""

import random

def gerar_precos(n: int) -> list:
    """
    Esta função recebe 'n' como o tamanho do vetor a ser 
    gerado e retorna uma lista com n números aleatórios, sendo
    que os valores dentro do vetor não podem ultrapassar o valor de 
    '2n'.
    """
 
    # 'n' limitação para manter o tempo do counting sort linear
    numeros = [random.randint(0, 2*n) for _ in range(n)]
    return numeros



def bottom_up_cut_rod(prices: list, total_size: int) -> int:

    storage = [0 for _ in range(0, total_size+1)]

    for i in range(1, total_size + 1):
        best_solu = float('-inf')
        for j in range(0, i):
            best_solu = max(best_solu, prices[j] + storage[i - j - 1])
        storage[i] = best_solu

    return storage[total_size]
       

def main():
    print("Tamanho total da tora de madeira: ", end="")
    valor = int(input())

    #gerando vetor de preços
    #prices = gerar_numeros_aleatorios(valor)
    prices = [1,  5,  8,  9, 10, 17, 17, 20, 24, 30]

    print(f"O valor máximo de revenda é R$ {bottom_up_cut_rod(prices, valor)}")  

if __name__ == '__main__':
    main()
