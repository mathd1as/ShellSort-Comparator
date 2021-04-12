# -*- coding: utf-8 -*-
# Disponível em: https://github.com/TheAlgorithms/Python/blob/master/sorts/shell_sort.py
import math
import time


class ShellSort1959:

    def __init__(self, collection):
        self.collection = collection

    def executar(self):
        n = len(self.collection)

        # Calcula o tempo
        inicio = time.time()
        h = n // 2
        k = 1
        while h > 0:
            for i in range(h, n):
                c = self.collection[i]
                j = i
                while j >= h and c < self.collection[j - h]:
                    self.collection[j] = self.collection[j - h]
                    j = j - h
                    self.collection[j] = c
            k = k + 1
            h = n // pow(2, k)
        fim = time.time()

        tempo_execucao = fim - inicio
        print('Tempo de execucao: ')
        print(fim - inicio)

        return self.collection, tempo_execucao
