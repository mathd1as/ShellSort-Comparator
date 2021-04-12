# -*- coding: utf-8 -*-
import time

class ShellSort1973:

    def __init__(self, collection):
        self.collection = collection

    def executar(self):
        n = len(self.collection)
        # Começa contar o tempo de execução do algoritmo
        start = time.time()
        h = 1

        while h < n:
            h = h * 3 + 1

        while h > 0:
            for i in range(h, n):
                c = self.collection[i]
                j = i
                while j >= h and c < self.collection[j - h]:
                    self.collection[j] = self.collection[j - h]
                    j = j - h
                        
                    self.collection[j] = c
            h = h // 3
            
        # Pega o tempo apos a execução do algoritmo
        end = time.time()
        # Calcula o tempo de execução
        executionTime = (end - start)
        return executionTime
