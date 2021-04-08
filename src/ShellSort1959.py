# Disponível em: https://github.com/TheAlgorithms/Python/blob/master/sorts/shell_sort.py

class ShellSort1959:
    
    def __init__(self, collection):
       self.collection = collection

    def executar(self):
        """Pure implementation of shell sort algorithm in Python
        :param collection:  Some mutable ordered collection with heterogeneous
        comparable items inside
        :return:  the same collection ordered by ascending
        >>> shell_sort([0, 5, 3, 2, 2])
        [0, 2, 2, 3, 5]
        >>> shell_sort([])
        []
        >>> shell_sort([-2, -5, -45])
        [-45, -5, -2]
        """
        # Marcin Ciura's gap sequence
        # Verificar a questao dos gaps (h)
        gaps = [701, 301, 132, 57, 23, 10, 4, 1]
        for gap in gaps:
            for i in range(gap, len(self.collection)):
                insert_value = self.collection[i]
                j = i
                while j >= gap and self.collection[j - gap] > insert_value:
                    self.collection[j] = self.collection[j - gap]
                    j -= gap
                if j != i:
                    self.collection[j] = insert_value
        return self.collection
