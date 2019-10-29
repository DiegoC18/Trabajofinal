## INPUT
n_personas = int(input("ingrese el numero de personas en el domicilio: "))
lista_nombres = []
lista_edades = []
lista_generos = []
i = 0



##PROCESO
while (i<n_personas):
    nombre = input("ingrese el nombre de la persona: ")
    edad = input("ingrese edad de la persona: ")
    genero = input("ingrese si es hombre o mujer :")
    lista_nombres.append(nombre.title())
    lista_edades.append(edad)
    lista_generos.append(genero)
    

    i += 1


print(lista_nombres)
print(lista_edades)
print(lista_generos)

    
    
