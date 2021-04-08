#Arquivo principal
from Dados import Dados
from ShellSort1959 import ShellSort1959

a100 = Dados()
elementos = a100.carregarBase('base-de-dados/aleatorios/a100.txt')
print('elementos em ordem aleatoria \n',elementos)

shellSort1959 = ShellSort1959(elementos)
elementosOrdenados = shellSort1959.executar()
print('\nelementos ordenados \n', elementosOrdenados)
