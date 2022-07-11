n = int(input('Número:'))
divisores =0
for divisor in range(1, n):
    if n % divisor ==0:
        divisores = divisores + 1
        if divisores > 1:
            break
if divisores > 1:
    print('Não é primo')
else: 
    print('É primo')        