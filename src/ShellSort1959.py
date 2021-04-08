#Codigo modificado do geeksforgeeks
#Disponivel em: https://www.geeksforgeeks.org/python-program-for-shellsort/

class ShellSort1959:
    
    def __init__(self, elementosOrdenados):
       self.elementosOrdenados = elementosOrdenados

    def executar(self):
        # Start with a big gap, then reduce the gap
        n = int(len(self.elementosOrdenados))

        gap = int(n/2)
        # Do a gapped insertion sort for this gap size.
        # The first gap elements a[0..gap-1] are already in gapped 
        # order keep adding one more element until the entire self.elementosOrdenadosay
        # is gap sorted
        while gap > 0:
            
            for i in range(gap,n):
    
                # add a[i] to the elements that have been gap sorted
                # save a[i] in temp and make a hole at position i
                temp = self.elementosOrdenados[i]
    
                # shift earlier gap-sorted elements up until the correct
                # location for a[i] is found
                j = i
                while  j >= gap and self.elementosOrdenados[j-gap] >temp:
                    self.elementosOrdenados[j] = self.elementosOrdenados[j-gap]
                    j -= gap
    
                # put temp (the original a[i]) in its correct location
                self.elementosOrdenados[j] = temp
            gap /= 2
            gap = int(gap)