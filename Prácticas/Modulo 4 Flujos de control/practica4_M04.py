ini=int(input('Ingresa un número natural desde el cual se van a mostrar los números primos: '))
fin=int(input('Ingresa un número natural hasta donde se van a mostrar los números primos: '))
if ini<=1:
    ini=2
for i in range(ini,fin):
    divisor=2
    cont=0
    while i>divisor:
        resto=i%divisor
        divisor+=1
        if resto==0:
            cont+=1
            break
    if cont==0:
        print(i)
        opc=str(input('Escriba "s" para ver el siguiente número primo'
                      '\no escriba cualquier otra tecla para finalizar: '))
        if opc!='s':
            print('Opción inválida')
            break