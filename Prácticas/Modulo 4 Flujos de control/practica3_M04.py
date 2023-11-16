num=int(input('Ingrese el número a evaluar: '))
cont=0
divisor=2
while num>divisor:
    resto=num%divisor
    #print(num,divisor,resto)
    divisor+=1
    if resto==0:
        cont+=1
if cont==0 and num>=2:
    print(f'El número {num} es primo')
else:
    print(f'El número {num} no es primo')