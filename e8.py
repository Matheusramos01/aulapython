s = float(input('Salário: R$'))
ns=0
if s>1000:
    ns=s+s*(5/100)
if s>=500 and s<=1000:
    ns=s+s*(10/100)
if s<500:
    ns=s+s*(15/100)
print('Novo salário é: R$', ns)        