import os,sys
os.system("cls")

print("---------- Bienvenido al sistema de registro de familias ----------")

## INPUT
n_personas = int(input("Ingrese el número de personas en el domicilio: "))
n_enfermos = 0
genero = ""
lista_nombres = []
lista_edades = []
lista_generos = []
lista_enfermos=[]
i = 0

while (i<n_personas):

    nombre = input("Ingrese el nombre de la persona: ")

    edad = int(input("Ingrese edad de la persona: "))  

    while True:

        gen_pregunta = input("Es la persona hombre? (sí o no): ")

        if gen_pregunta.title() == "si":
            genero = "Hombre"
            lista_generos.append(genero)
            break

        if gen_pregunta.lower() == "no":
            genero = "Mujer"
            lista_generos.append(genero)
            break

        else :
            print("Ingrese una respuesta válida (Sí/No).")

    while True:

        enfermo = input("¿Está la persona enferma? (Sí/No): ")

        if (enfermo.lower() == "si"):
            n_enfermos += 1
            lista_enfermos.append("Sí")
            break

        if (enfermo.lower() == "no"):
            print("Qué bueno que estés sano(a) "+ nombre) 
            lista_enfermos.append("No")
            break

        else :
            print("Ingrese una respuesta válida (si/no).")
                
  
    i += 1

    lista_nombres.append(nombre)
    lista_edades.append(edad)

##SALIDA

for i in range (n_personas):
    print("---------------------")
    print("Persona #",i+1)
    print( "Nombre: ", lista_nombres[i] )
    print( "Edad: ", lista_edades[i] )
    print( "Enfermo: ", lista_enfermos[i] )
    print( "Género: ", lista_generos[i] )
    print("---------------------")
 
print("Número total de enfermos: ", n_enfermos)
    
    
