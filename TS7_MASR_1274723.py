#trabajo supervisado introduccion a la programación
#21/09/2023
#Marcos Anibal Sanchez Rios 
#objetivo 
#entradas
codigo = True

while codigo: 
    print("Marcos Anibal Sanchez Rios")
    numero = int((input("ingrese un numero del 1-10: ")))

#Procesos principales
    if numero < 1 or numero > 10:
        print("El numero no está en el rango indicado")
        continue
    for i in range (1,11):
        resultado = numero * i 
        print(numero, "*", i,  "=", resultado)
    opcion = input ("¿desea generar otra tabla? (si - no)")
    if opcion == "no":
        print("hasta luego")
        codigo=False
    elif opcion == "si":
        codigo = True
        
    

    