num=[]
n=1
for n in range (1,11):
    n=int(input("Digite n:"))
    if n!=0: num.append(n)
print(num[::-1])