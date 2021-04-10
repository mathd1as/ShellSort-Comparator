# -*- coding: utf-8 -*-
# Disponível em: https://github.com/TheAlgorithms/Python/blob/master/sorts/shell_sort.py
import math
import time
class ShellSort1959:
    
    def __init__(self, collection):
       self.collection = collection

    def executar(self):
        n = len(self.collection)
        #come a calcular o tempo
        inicio = time.time()
        h = n // 2
        
        while h > 0:
                for i in range(h, n):
                    c = self.collection[i]
                    j = i
                    while j >= h and c < self.collection[j - h]:
                        self.collection[j] = self.collection[j - h]
                        j = j - h
                        
                        self.collection[j] = c
                h = h // 2
        fim = time.time()
        #printa o tempo de execucao  
        print('tempo de execucao: ')
        print(fim - inicio)       
        return self.collection