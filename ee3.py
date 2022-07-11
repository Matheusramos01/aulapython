repeticoes = 4
for contador in range (repeticoes):
    n= (input('Name:'))
    alt = float(input('Altura:'))
    peso = float(input('Peso:'))
    imc = peso/(alt*alt)
    if imc>=40:
        print ('Obesidade classe 3')
    elif imc>=35 and imc<=39.9:
        print ('Obesidade classe 2')
    elif imc>=30 and imc<=34.9:
        print ('Obesidade classe 1')
    elif imc>=25 and imc<=29.9:
        print('Excesso de peso')
    elif imc>=18.5 and imc<=24.9:
            print('Peso Normal')                
    elif imc< 18.5:
        print('Abaixo do peso normal.')