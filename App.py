import os,sys
os.system("cls")

## INPUT
n_personas = int(input("Ingrese el número de personas en el domicilio: "))
n_enfermos = 0
lista_nombres = []
lista_edades = []
lista_generos = []
lista_edades2=[]
i = 0



##PROCESO
while (i<n_personas):
<<<<<<< HEAD
    nombre = input("ingrese el nombre de la persona: ")
    edad = int(input("ingrese edad de la persona: "))
    while(True):
        if edad>0 and edad<18:
            edad2="menor de edad"
            break
        elif edad>=18 and edad<65:
            edad2="mayor de edad"
            break
        elif edad>=65:
            edad2="tercera edad"
            break
        else:
            print("ERROR")

    genero = input("ingrese si es hombre o mujer :")

=======
    nombre = input("Ingrese el nombre de la persona: ")
    edad = input("Ingrese edad de la persona: ")
    genero = input("Ingrese si es hombre o mujer :")
    enfermo = input("esta enfermo? (si/no)")

    if (enfermo == "si"):
        n_enfermos += 1 

    else :
        print("que bueno que estes sano(a) "+ nombre) 
    
    
>>>>>>> 9187f0f2a13d77ddb5711667bfcfc726e43d5e27
    lista_nombres.append(nombre.title())
    lista_edades.append(edad)
    lista_edades2.append(edad2)
    lista_generos.append(genero)
    

    i += 1

 ##SALIDA
print(lista_nombres)
print(lista_edades)
print(lista_generos)

for i in range (n_personas):
    print("---------------------")
    print("Persona #",i+1)
    print( "Nombre: ", lista_nombres[i] )
    print( "Edad: ", lista_edades[i] )
    print( "Género: ", lista_generos[i] )
    print("---------------------")
    
    
