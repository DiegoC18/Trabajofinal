## INPUT
n_personas = int(input("ingrese el numero de personas en el domicilio: "))
lista_nombres = []
lista_edades = []
lista_generos = []
lista_edades2=[]
i = 0



##PROCESO
while (i<n_personas):
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

    lista_nombres.append(nombre.title())
    lista_edades.append(edad)
    lista_edades2.append(edad2)
    lista_generos.append(genero)
    

    i += 1

 ##SALIDA
print(lista_nombres)
print(lista_edades)
print(lista_generos)
