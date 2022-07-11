maioralt = 0
menoralt = 1.5
maiorpeso = 0
menorpeso = 50
repeticoes = 5
for contador in range (repeticoes):
    peso = float(input('Peso:'))
    alt = float(input('Altura:'))
    if (alt>maioralt):
        maioralt=alt
    elif (alt<menoralt):
         menoralt=alt
    elif (peso>maiorpeso):
         maiorpeso=peso
    elif (peso<menorpeso):
         menorpeso=peso
print('Maior altura:', maioralt)
print('Menor altura:', menoralt)
print('Maior peso:', maiorpeso)
print('Menor peso:', menorpeso)
    

