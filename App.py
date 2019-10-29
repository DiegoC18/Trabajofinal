import os,sys
os.system("cls")

## INPUT
n_personas = int(input("Ingrese el número de personas en el domicilio: "))
lista_nombres = []
lista_edades = []
lista_generos = []
i = 0



##PROCESO
while (i<n_personas):
    nombre = input("Ingrese el nombre de la persona: ")
    edad = input("Ingrese edad de la persona: ")
    def genero():
        hask = input("Es la persona hombre?(sí o no):")
    if genero.title() == "Si" or "Sí":
        return True
        genero = "Hombre"
    if genero.title() == "No":
        return False
        genero = "Mujer"
   
    lista_nombres.append(nombre.title())
    lista_edades.append(edad)
    lista_generos.append(genero)


    

    i += 1


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
    
    
