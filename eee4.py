#procura o indice do valor 8 a resposta de ver ser 2
lista = [2,7,8,9,7]
valorprocurado = 8
for i in range (len(lista)):
    if valorprocurado == lista[i]:
        print ("Valor procurado do índice é:", i)
    else:
        print ("Diferente") 