# -*- coding: utf-8 -*-
# Estudantes: Sophya Ribeiro e Soraya Ferreira

def greedy_cut_rod(sizes: list, prices: list) -> int:
    """
    Essa estratégia gulosa que prioriza as toras com maior densidade.
    """    
    # Densidade é a razão entre o preço do tamanho i e o tamanho i.

    best_value = 0
    total_size = len(sizes)

    while total_size > 0:
        best_density = 0
        best_density_i = -1

        for i in range(0, total_size):
            if sizes[i] <= total_size:
                density = prices[i] / sizes[i]
                if density > best_density:
                    best_density = density
                    best_density_i = i

        if best_density_i == -1:
            break

        best_value += prices[best_density_i]
        total_size -= sizes[best_density_i]
    return best_value

def main():
    print("Tamanho total da tora de madeira: ", end="")
    valor = int(input())

    #gerando vetor de preços
    #prices = gerar_numeros_aleatorios(valor)
    precos = [1,  5,  8,  9, 10, 17, 17, 20, 24, 30]
    tamanhos  = [_ for _  in range(1, valor + 1)]

    print(f"O valor máximo de revenda é R$ {greedy_cut_rod(tamanhos, precos)}")  

if __name__ == '__main__':
    main()