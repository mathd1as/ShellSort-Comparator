# Arquivo principal
from Dados import Dados
from ShellSort1973 import ShellSort1973
from ShellSort1959 import ShellSort1959

# No linux o caminho do arquivo deve ser: '../base-de-dados/aleatorios/a100.txt'
# No windows o caminho do arquivo deve ser: '/base-de-dados/aleatorios/a100.txt'


data = Dados()

elementos = data.carregarBase('../base-de-dados/aleatorios/a2000000.txt')
shellSort1973 = ShellSort1973(elementos)
elementos, tempo_execucao = shellSort1973.executar()

#shellSort1959 = ShellSort1959(elementos)
#elementos, tempo_execucao = shellSort1959.executar()

file = open("testes_aleatorios_1973.txt", "a")
file.write("\n")
file.write(str(tempo_execucao))
file.close

# a100 = Dados()
# print("base-de-dados/aleatorios/a100.txt")
# elementos = a100.carregarBase("base-de-dados/aleatorios/a100.txt")

# shellSort1959 = ShellSort1959(elementos)
# shellSort1959.executar()
