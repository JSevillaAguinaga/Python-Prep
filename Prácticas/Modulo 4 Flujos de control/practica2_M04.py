for i in range(1,14):   #rango del 1 al 13
    #print(i)
    if i>1:             # es decir, a partir del 2
        cont=0          # se crea una variable "contador"
        divisor=2       # se crea una variable "divisor"
        #print(i)
        while i>divisor and cont==0:    #mientras se cumpla que el elemento del rango sea mayor al divisor, y el contador sea igual a 0
            resto=i%divisor             #se calcule el resto de dividor i entre divisor
            #print(f'{i} entre {divisor} da un resto de: {resto}')
            divisor+=1                  #además, que el dividor aumente en 1
            if resto==0:                #además, si el resto es igual a 0
                #print(f'i: {i}, divisor: {divisor}, resto: {resto}, cont: {cont}')
                cont+=1                 #que el contador aumente en 1, para identificar a los números no primos
        if cont==0:                     # si el contador es igual a 0 (para los numeros primos)
            print(i)                    #que imprima esos números que tienen contador 0