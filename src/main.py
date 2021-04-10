#Arquivo principal
from Dados import Dados
from ShellSort1973 import ShellSort1973
from ShellSort1959 import ShellSort1959

#No linux o caminho do arquivo deve ser: '../base-de-dados/aleatorios/a100.txt'
#No windows o caminho do arquivo deve ser: '/base-de-dados/aleatorios/a100.txt'
caminhoDosArquivos = [
    "base-de-dados/aleatorios/a100.txt",
    "base-de-dados/aleatorios/a200.txt",
    "base-de-dados/aleatorios/a500.txt",
    "base-de-dados/aleatorios/a1000.txt",
    "base-de-dados/aleatorios/a2000.txt",
    "base-de-dados/aleatorios/a5000.txt",
    "base-de-dados/aleatorios/a7500.txt",
    "base-de-dados/aleatorios/a10000.txt",
    "base-de-dados/aleatorios/a15000.txt",
    "base-de-dados/aleatorios/a30000.txt",
    "base-de-dados/aleatorios/a50000.txt",
    "base-de-dados/aleatorios/a75000.txt",
    "base-de-dados/aleatorios/a100000.txt",
    "base-de-dados/aleatorios/a200000.txt",
    "base-de-dados/aleatorios/a500000.txt",
    "base-de-dados/aleatorios/a750000.txt",
    "base-de-dados/aleatorios/a1000000.txt",
    "base-de-dados/aleatorios/a1250000.txt",
    "base-de-dados/aleatorios/a1500000.txt",
    "base-de-dados/aleatorios/a2000000.txt",

    "base-de-dados/decrescentes/d100.txt",
    "base-de-dados/decrescentes/d200.txt",
    "base-de-dados/decrescentes/d500.txt",
    "base-de-dados/decrescentes/d1000.txt",
    "base-de-dados/decrescentes/d2000.txt",
    "base-de-dados/decrescentes/d5000.txt",
    "base-de-dados/decrescentes/d7500.txt",
    "base-de-dados/decrescentes/d10000.txt",
    "base-de-dados/decrescentes/d15000.txt",
    "base-de-dados/decrescentes/d30000.txt",
    "base-de-dados/decrescentes/d50000.txt",
    "base-de-dados/decrescentes/d75000.txt",
    "base-de-dados/decrescentes/d100000.txt",
    "base-de-dados/decrescentes/d200000.txt",
    "base-de-dados/decrescentes/d500000.txt",
    "base-de-dados/decrescentes/d750000.txt",
    "base-de-dados/decrescentes/d1000000.txt",
    "base-de-dados/decrescentes/d1250000.txt",
    "base-de-dados/decrescentes/d1500000.txt",
    "base-de-dados/decrescentes/d2000000.txt",

    "base-de-dados/ordenados/o100.txt",
    "base-de-dados/ordenados/o200.txt",
    "base-de-dados/ordenados/o500.txt",
    "base-de-dados/ordenados/o1000.txt",
    "base-de-dados/ordenados/o2000.txt",
    "base-de-dados/ordenados/o5000.txt",
    "base-de-dados/ordenados/o7500.txt",
    "base-de-dados/ordenados/o10000.txt",
    "base-de-dados/ordenados/o15000.txt",
    "base-de-dados/ordenados/o30000.txt",
    "base-de-dados/ordenados/o50000.txt",
    "base-de-dados/ordenados/o75000.txt",
    "base-de-dados/ordenados/o100000.txt",
    "base-de-dados/ordenados/o200000.txt",
    "base-de-dados/ordenados/o500000.txt",
    "base-de-dados/ordenados/o750000.txt",
    "base-de-dados/ordenados/o1000000.txt",
    "base-de-dados/ordenados/o1250000.txt",
    "base-de-dados/ordenados/o1500000.txt",
    "base-de-dados/ordenados/o2000000.txt",

    "base-de-dados/parcialmente-ordenados/po100.txt",
    "base-de-dados/parcialmente-ordenados/po200.txt",
    "base-de-dados/parcialmente-ordenados/po500.txt",
    "base-de-dados/parcialmente-ordenados/po1000.txt",
    "base-de-dados/parcialmente-ordenados/po2000.txt",
    "base-de-dados/parcialmente-ordenados/po5000.txt",
    "base-de-dados/parcialmente-ordenados/po7500.txt",
    "base-de-dados/parcialmente-ordenados/po10000.txt",
    "base-de-dados/parcialmente-ordenados/po15000.txt",
    "base-de-dados/parcialmente-ordenados/po30000.txt",
    "base-de-dados/parcialmente-ordenados/po50000.txt",
    "base-de-dados/parcialmente-ordenados/po75000.txt",
    "base-de-dados/parcialmente-ordenados/po100000.txt",
    "base-de-dados/parcialmente-ordenados/po200000.txt",
    "base-de-dados/parcialmente-ordenados/po500000.txt",
    "base-de-dados/parcialmente-ordenados/po750000.txt",
    "base-de-dados/parcialmente-ordenados/po1000000.txt",
    "base-de-dados/parcialmente-ordenados/po1250000.txt",
    "base-de-dados/parcialmente-ordenados/po1500000.txt",
    "base-de-dados/parcialmente-ordenados/po2000000.txt",
]

# for i in range(19):

#     a100 = Dados()
#     print(caminhoDosArquivos[i])
#     elementos = a100.carregarBase(caminhoDosArquivos[i])

#     shellSort1959 = ShellSort1959(elementos)
#     shellSort1959.executar()

#     shellSort1959 = ShellSort1959(elementos)
#     shellSort1959.executar()

#     shellSort1959 = ShellSort1959(elementos)
#     shellSort1959.executar()

#     shellSort1959 = ShellSort1959(elementos)
#     shellSort1959.executar()

#     shellSort1959 = ShellSort1959(elementos)
#     shellSort1959.executar()

#     shellSort1959 = ShellSort1959(elementos)
#     shellSort1959.executar()




    # shellSort1973 = ShellSort1973(elementos)
    # shellSort1973.executar()


a100 = Dados()
print('base-de-dados/aleatorios/a100.txt')

elementos = a100.carregarBase('base-de-dados/aleatorios/a2000000.txt')
print("Executando a primeira vez")
shellSort1959 = ShellSort1959(elementos)
shellSort1959.executar()
elementos = []

elementos = a100.carregarBase('base-de-dados/aleatorios/a2000000.txt')
print("Executando a primeira vez")
shellSort1959 = ShellSort1959(elementos)
shellSort1959.executar()
elementos = []

elementos = a100.carregarBase('base-de-dados/aleatorios/a2000000.txt')
print("Executando a segunda vez")
shellSort1959 = ShellSort1959(elementos)
shellSort1959.executar()
elementos = []

elementos = a100.carregarBase('base-de-dados/aleatorios/a2000000.txt')
print("Executando a terceira vez")
shellSort1959 = ShellSort1959(elementos)
shellSort1959.executar()
elementos = []

elementos = a100.carregarBase('base-de-dados/aleatorios/a2000000.txt')
print("Executando a quarta vez")
shellSort1959 = ShellSort1959(elementos)
shellSort1959.executar()
elementos = []

elementos = a100.carregarBase('base-de-dados/aleatorios/a2000000.txt')
print("Executando a quinta vez")
shellSort1959 = ShellSort1959(elementos)
shellSort1959.executar()
elementos = []

elementos = a100.carregarBase('base-de-dados/aleatorios/a2000000.txt')
print("Executando a sexta vez")
shellSort1959 = ShellSort1959(elementos)
shellSort1959.executar()
elementos = []

# a100 = Dados()
# print("base-de-dados/aleatorios/a100.txt")
# elementos = a100.carregarBase("base-de-dados/aleatorios/a100.txt")

# shellSort1959 = ShellSort1959(elementos)
# shellSort1959.executar()
