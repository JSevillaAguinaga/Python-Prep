def sera_primo(num):
    divisor = 2
    primo = True
    while num > divisor:
        r = num % divisor
        divisor += 1
        if r == 0:
            primo = False
    if primo and num>1:
        print(f"El número {num} es primo")
    else:
        print(f"El número {num} no es primo")

sera_primo(6)
