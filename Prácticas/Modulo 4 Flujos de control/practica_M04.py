print('TABLAS DE MULTIPLICAR HASTA N')
num=int(input('Escribe un número para ver su tabla de multiplicar: '))
lim=int(input('Escribe el límite del multiplicando: '))

multipl=1
print(f'TABLA DEL {num}:')
while multipl<=lim:
    prod=num*multipl
    print(f'{num} x {multipl} = {prod}')
    multipl+=1