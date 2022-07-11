tv1 = 0
tv2= 0
tv3 = 0
tv4 = 0
pv1= 0
pv2= 0
pv3 = 0
pv4 = 0
repeticoes = 5
for contador in range (repeticoes):
    name = (input('Name:'))
    v = int(input('Voto:'))

    if (v==1):
        print('Votou no candidato 1')
        tv1 = tv1 + 1
    elif (v==2):
        print('Votou no candidato 2')
        tv2= tv2 + 1
    elif (v==3):
        print("Votou nulo")
        tv3 = tv3 + 1
    elif (v==4):
        print('Votou Branco')
        tv4 = tv4 + 1
print('Votação Concluída')
pv1=(tv1/5)*100
pv2=(tv2/5)*100
pv3=(tv3/5)*100
pv4=(tv4/5)*100
print('Total de votos candidato 1:', tv1)
print('% de votos candidato 1:', pv1)
print('Total de votos candidato 2:', tv2)
print('% de votos candidatos 2:', pv2)
print('Total de votos nulos:', tv3)
print('% de votos nulos:', pv3)
print('Total de votos brancos:', tv4)
print('% de votos brancos:', pv4)
