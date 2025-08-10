#crear una calculadora basica con funciones

def menu():
    op = 0
    while op <1 or op>5:
        print("\n\tCalculadora basica" \
        "\n1.Suma" \
        "\n2.Resta" \
        "\n3.Multiplicacion" \
        "\n4.Division" \
        "\n5.Salir")
        op = int(input("Opcion: "))
    return op

def sumar():
    valor1 = int(input())
    valor2 = int(input())
    sumatoria = valor1 + valor2
    print(f"Resultado = {sumatoria}")    
        
def restar():
    valor1 = int(input())
    valor2 = int(input())   
    restar = valor1 - valor2
    print(f"Resultado = {restar}")

def multiplicar():
    valor1 = int(input())
    valor2 = int(input())
    multiplicacion = valor1 * valor2
    print(f"Resultado = {multiplicacion}") 

def dividir():
    valor1 = int(input())
    valor2 = int(input())
    division = valor1 / valor2
    print(f"Resultado = {division}") 

opcion = menu()

if opcion == 1:  
    sumar()
elif opcion == 2:
    restar()
elif opcion == 3:
    multiplicar()
else:
    dividir()

