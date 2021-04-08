#Arquivo principal
from Dados import Dados
from ShellSort1959 import ShellSort1959

#Exemplo de como usar as classes criadas
a100 = Dados()
a100.carregarBase('base-de-dados/aleatorios/a100.txt')

shellSort1959 = ShellSort1959(a100.elementos)
shellSort1959.executar()
#array de elementos ordenados
print(shellSort1959.elementosOrdenados)