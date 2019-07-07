##Variaveis globais


kx = [0] #contém o valor de k no intervalo correspondente
pos = [0] #define as fronteiras dos intervalos
nome = ["zero", "primeiro", "segundo", "terceiro", "quarto", "quinto", "sexto", "setimo", "oitavo", "nono", "decimo"]
passos =[0.0]
ponto_medio = 0

def define_valores():
    p=0
    q=0
    partes = int(input('Quantos valores diferentes assume o k nesse problema? '))
    for numero in range(1, partes+1):
        posicao = float(input('O '+ str(nome[numero]) +' intervalo de k é de ' + str(pos[numero - 1]) + ' até ? '))
        if posicao not in passos:
                print('Não é possível!')
                exit(1)
        pos.append(posicao)
        valor = float(input('E quanto vale k de '+ str(pos[numero - 1]) +' a ' + str(posicao) + '? '))
        for i in range(p, len(passos)):
                p = p+1
                q = q+1
                if passos[i] == posicao:
                        break
        for i in range(q):
                kx.append(valor)
        q = 0

 

#Chama função inicial que vai determinar os valores de K durante toda a execução
define_valores()


