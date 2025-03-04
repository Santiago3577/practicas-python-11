def sumar(a,b):
    return a + b

def resta(a,b):
     return a - b 

def multiplicar(a,b):
    return a * b 

def division(a,b):
    return a / b 

def division(a,b):
    if b == 0: 
        return "Error: División por cero" 

def mostrar_menu():
    print ("calculadora Básica SantiagoCelisyOscarDiaz")
    print ("1. sumar")
    print ("2. restar") 
    print ("3. multiplicar")
    print ("4. dividir")
    print ("5. salir")  

def calculadora():
    while True:
        mostrar_menu() 
        opcion = input("selecciona una opción(1-5): ")
        if opcion == '5':
            print("Saliendo de la calculadora. ¡Hasta luego!")
            break
        if opcion in ['1','2','3','4']:
            num1= float(input("introduce el primer número:" ))
            num1= float(input("introduce el segundo número:" ))
        if opcion == '1':
            resultado = sumar(num1, num2)
            print(f"el resultado de {num1} +  {num2} es: {resultado}")
        elif opcion == '2':
            resultado = restar(num1, num2)
            print(f"El resultado de {num1} - {num2} es: {resultado}")
        elif opcion == '3':
            resultado = multiplicar (num1, num2)
            print(f"El resultado de {num1} - {num2} es: {resultado}")
        elif opcion == '4':
            resultado = dividir (num1,) 
            print(f"El resultado de {num1} - {num2} es: {resultado}")
else:
    print ("Opcion no valido. Por favor, selecciona una opcion del 1 AL 5 ")
if__name__"__mine__":
calculadora()