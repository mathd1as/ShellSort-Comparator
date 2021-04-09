# -*- coding: utf-8 -*-
#Classe responsável pela leitura e conversão dos dados

class Dados:

    def __init__(self):
        self.elementos = []

    def carregarBase(self, caminhoDoArquivo):
        self.caminhoDoArquivo = caminhoDoArquivo

        arquivo = open(self.caminhoDoArquivo, 'r')
        self.elementos = arquivo.readlines()

        # Convertendo os elementos para inteiro
        for i in range(len(self.elementos)):
            self.elementos[i] = int(self.elementos[i])
        
        arquivo.close()
        return self.elementos
       


