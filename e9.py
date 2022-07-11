cnum= 4
repeticoes=96
for contador in range (repeticoes):
    cnum = cnum + 1
    if (cnum%7==0) and (cnum%5!=0):        
        print(cnum)