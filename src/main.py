#Arquivo principal
from Dados import Dados
from ShellSort1973 import ShellSort1973
from ShellSort1959 import ShellSort1959

a100 = Dados()
#No linux o caminho do arquivo deve ser: '../base-de-dados/aleatorios/a100.txt'
#No windows o caminho do arquivo deve ser: '/base-de-dados/aleatorios/a100.txt'
elementos = a100.carregarBase('../base-de-dados/aleatorios/a100.txt')
# print('Elementos em ordem aleatoria: ')
# print(elementos)

shellSort1973 = ShellSort1973(elementos)
elementosOrdenados = shellSort1973.executar()
print('Elementos ordenados: ')
print(elementosOrdenados)

# shellSort1959 = ShellSort1959(elementos)
# shellSort1959.executar()

