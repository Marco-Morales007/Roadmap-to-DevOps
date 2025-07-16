#crear una calculadora basica

print("Menu: \n1-Suma\n2-Resta\n3-Multiplicacion\n4-Division")
opcion1 = int(input("Opcion seleccionada: "))
while opcion1<1 or opcion1>4:
    print("Opcion no Valida....")
    opcion1 = int(input("Opcion seleccionada: "))

op_salir = 1
if opcion1==1:#suma
    while op_salir == 1:
        print("Ingrese los valores a sumar")
        opcion2 = 'x'
        suma = 0
        while opcion2 == "x":
            valor1 = int(input())
            suma = suma + valor1
            opcion2 = input("Ingrese x para sumar otro numero:  ")
        print(f"Resultado = {suma}")
        op_salir = int(input("Hacer otra suma: 1-SI 2-NO: "))
elif opcion1==2:#resta
    while op_salir == 1:
        print("Ingrese los valores a restar")
        valor1 = int(input())
        valor2 = int(input())
        resta = valor1 - valor2
        print(f"Resultado = {resta}")
        op_salir = int(input("Hacer otra resta: 1-SI 2-NO: "))
elif opcion1==3:#multiplicacion
    while op_salir == 1:    
        print("Ingrese los valores a multiplicar")
        valor1 = int(input())
        valor2 = int(input())
        multiplicacion = valor1*valor2
        print(f"Resultado = {multiplicacion}")
        op_salir = int(input("Hacer otra multiplicacion: 1-SI 2-NO: "))
else: #division
    while op_salir == 1:    
        print("Ingrese los valores a dividir:")
        valor1 = int(input())
        valor2 = int(input())
        division = valor1/valor2
        print(f"Resultado = {division}")
        op_salir = int(input("Hacer otra division: 1-SI 2-NO: "))

