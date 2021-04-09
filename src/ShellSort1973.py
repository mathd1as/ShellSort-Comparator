# -*- coding: utf-8 -*-
# Disponível em: https://github.com/TheAlgorithms/Python/blob/master/sorts/shell_sort.py

class ShellSort1973:
    
    def __init__(self, collection):
       self.collection = collection

    def executar(self):
        n = len(self.collection)
        h = 1 # s = 1
        # while h < n
        while h < n / 3:
            h = h * 3 + 1 # h(s) = 3h(s - 1) + 1
        
        while h > 0:
                for i in range(h, n):
                    c = self.collection[i]
                    j = i
                    while j >= h and c < self.collection[j - h]:
                        self.collection[j] = self.collection[j - h]
                        j = j - h
                        
                        self.collection[j] = c
                print(h)
                h = int(h / 3)
                
        return self.collection