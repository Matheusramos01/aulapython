print('Leia 3 valores e calcular a média:\n')

repeticoes = 3
for contador in range (repeticoes):
    name = (input('Name:'))
    n1 = float(input('N1:'))
    n2 = float(input('N2:'))
    n3 = float(input('N3:'))
    media = (n1 + n2 + n3)/3

    print('A média é:', media)
    if (media<=5.0):
        print(name, 'está reprovado')
    elif (media>=7.0):
        print(name, 'está aprovado')
    else:
        print(name, 'está aprovado com distinção')
    