class Funciones:
    def __init__(self, lista_fun):
        self.lista_fun = lista_fun

    # Función 'Verificar primo'
    def sera_primo(self, num):
        divisor = 2
        primo = True
        while num > divisor:
            r = num % divisor
            divisor += 1
            if r == 0:
                primo = False
                break
        if primo and num > 1:
            return True
        else:
            return False

    # Función de verificación de primos para listas
    def lista_primos(self):
        for i in self.lista_fun:
            if self.sera_primo(i) == True:
                print(f"El número {i} es primo.")
            else:
                print(f"El número {i} no es primo.")

    # Función para contar repeticiones de un número
    def repeticiones(self, p_listas):
        mas_repetido = max(p_listas, key=p_listas.count)
        reps = p_listas.count(mas_repetido)
        print(f"{mas_repetido}, {reps}")

    # Función para contar repeticiones de un número, con lista de la clase
    def mas_repetido(self):
        lista_unicos = []
        lista_reps = []
        if len(self.lista_fun) != 0:
            for j in self.lista_fun:
                if j not in lista_unicos:
                    lista_unicos.append(j)
                    lista_reps.append(self.lista_fun.count(j))
            mas_rep = lista_unicos[lista_reps.index(max(lista_reps))]
            reps = max(lista_reps)
            return mas_rep, reps  # print(f"{mas_rep}, {reps}")
        else:
            return print("La lista está vacía")

    def imprimir_reps(self):
        for i in self.lista_funciones:
            if self.lista_funciones.count(i) > 1:
                continue

    # Función "Conversión grados"
    def conversion_temperatura(self, valor, medida_o, medida_d):
        if medida_o == "C" and valor >= -273.15:
            if medida_d == "F":
                resultado = (valor * 9 / 5) + 32
            elif medida_d == "K":
                resultado = valor + 273.15
            elif medida_d == "C":
                resultado = valor
            else:
                print("Tempreratura de destino inválida.")
        elif medida_o == "F" and valor >= -459.67:
            if medida_d == "C":
                resultado = 5 / 9 * (valor - 32)
            elif medida_d == "K":
                resultado = 5 / 9 * (valor - 32) + 273.15
            elif medida_d == "F":
                resultado = valor
            else:
                print("Tempreratura de destino inválida.")
        elif medida_o == "K" and valor >= 0:
            if medida_d == "C":
                resultado = valor - 273.15
            elif medida_d == "F":
                resultado = (9 / 5) * (valor - 273.15) + 32
            elif medida_d == "K":
                resultado = valor
            else:
                print("Tempreratura de destino inválida.")
        elif medida_o and medida_d not in ["C", "F", "K"]:
            print("Temperatura de origen y destino inválidas.")
        elif medida_o not in ["C", "F", "K"]:
            print("Temperatura de origen inválida.")
        else:
            print(
                f"Valor ingresado para la medida °{medida_o} no es válido. El límite más bajo de temperatura es 0°K, -273.15°C o -459.67°F."
            )
        try:
            return round(resultado, 2)
        except UnboundLocalError:
            print('Colocar medida de origen o destino válida: "C", "F" o "K".')

    # Función "todos_grados"
    def todos_grados(self):
        for i in self.lista_fun:
            for t1 in list(["C", "F", "K"]):
                print(f"{i}°{t1} es equivalente a:")
                for t2 in list(["C", "F", "K"]):
                    if t1 == t2:
                        continue
                    else:
                        print(f"✅{self.conversion_temperatura(i,t1,t2)}°{t2}")

    # Función "Factorial"
    def factorial(self, num):
        if type(num) == int and num > 0:
            num = num * self.factorial(num - 1)
            return num
        elif num == 0:
            return 1
        else:
            return print("Solo se puede ingresar números enteros no negativos.")

    def factorial_todo(self):
        for i in self.lista_fun:
            print(f"El factorial de {i} es {self.factorial(i)}")
