## https://www.ufrgs.br/reamat/CalculoNumerico/livro-py/pdvdc-metodo_de_diferencas_finitas.html
##Variaveis globais
import numpy as np


k = [0] #contém o valor de k no intervalo correspondente
pos = [0] #define as fronteiras dos intervalos
nome = ["zero", "primeiro", "segundo", "terceiro", "quarto", "quinto", "sexto", "setimo", "oitavo", "nono", "decimo"]




def define_valores():
    partes = int(input('Quantos valores diferentes assume o k nesse problema? '))
    for numero in range(1, partes+1):
        posicao = float(input('O '+ str(nome[numero]) +' intervalo de k é de ' + str(pos[numero - 1]) + ' até ? '))
        pos.append(posicao)
        valor = float(input('E quanto vale k de '+ str(pos[numero - 1]) +' a ' + str(posicao) + '? '))
        k.append(valor)
 

#Chama função inicial que vai determinar os valores de K durante toda a execução
define_valores()

#ajusta o array de saída
k = k[1:]
pos = pos[1:]  
print(k)
print(pos)





##Inicio da resolucao do problema

##Define os valores constantes
N = 3
h = 0.25
A = np.zeros((N,N))  
b = np.zeros(N)  
 

 ##Preenche matriz A e b (as matrizes envolvidas no poblema)
A[0,0] = -2  
A[0, 1] = 1
b[0] = 2*h**2 -2
for i in np.arange(1,N-1):  
    A[i,i-1] = 1  
    A[i,i] = -2  
    A[i,i+1] = 1  
    b[i] = 2 * h**2
A[N-1,N-1] = -2  
A[N-1, N-2] = 1
b[N-1] = 2*h**2 -3

print('\n\nMatriz A: \n')
print(A)
print('\n\nMatriz B: \n')
print(b)

##Calcula o vetor de resposta (sistema de equacoes)
resp2 = np.linalg.solve(A, b)
print('\n\Resultado:\n')
print(resp2)
