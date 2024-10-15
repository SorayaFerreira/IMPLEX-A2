# -*- coding: utf-8 -*-
# Estudantes: Sophya Ribeiro e Soraya Ferreira

def bottom_up_cut_rod(prices, total_size):
    r = [0 for _ in range(total_size)]
    
    for j in range(total_size):
        q = float('-inf')
        for i in range(j):
            q = max(q, p[i] + r[j-i])
               
        r[j] = q
    return r[total_size]

def main():
    
   

if __name__ == '__main__':
    main()
