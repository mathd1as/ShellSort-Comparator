#Classe responsavel pelo tratamente e leitura dos dados

class Dados:

    def __init__(self):
        self.elementos = []

    def carregarBase(self, caminhoDoArquivo):
        self.caminhoDoArquivo = caminhoDoArquivo

        arquivo = open(self.caminhoDoArquivo, 'r')
        self.elementos = arquivo.readlines()
        
        for i in range(len(self.elementos)):
            # Convertendo as strings para integer antes de aplicar o algoritmo
            self.elementos[i] = int(self.elementos[i])

        arquivo.close()
        return self.elementos
       


