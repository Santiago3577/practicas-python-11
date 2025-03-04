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
        return "Error: Division por cero" 

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
        opcion = print("selecciona una opcion(1-5): ")   