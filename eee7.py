mat = []
# para cada linha de 0 ate 2
for i in range (3):
    # linha começa vazia
    l=[]
    # para cada coluna de 0 ate 3
for j in range (4):
    #preenche colunas da linha i
    l.append(i*j)
    #adicione linha na matriz
    mat.append(l)
    print(mat)

