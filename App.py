import os,sys
os.system("cls")

print("---------- Bienvenido al sistema de registro de familias ----------")

## INPUT
n_personas = int(input("Ingrese el número de personas en el domicilio: "))
n_enfermos = 0
lista_nombres = []
lista_edades = []
lista_generos = []
lista_edades2=[]
medicamentos={"Pecho":"aspirina","Cabeza":"ibuprofeno","Musculos":"Relajante","Estomago":"Desintoxicante","Garganta":"Desinflamatorio","Asma":"Salbutamol"}
i = 0



##INPUT
while (i<n_personas):

    nombre = input("ingrese el nombre de la persona: ")
    lista_nombres.append(nombre)
    edad = int(input("ingrese edad de la persona: "))
    lista_edades.append(edad)
    genero = input("Es la persona hombre?(sí o no):")
    if genero.title() == "Si" or "Sí":
        genero = "Hombre"
    elif genero.title() == "No":
        genero = "Mujer"
    lista_generos.append(genero)
    enfermo = input("¿esta enfermo? (si/no)")

    if (enfermo == "si"):
        n_enfermos += 1
        enf_bool = "Si"
        enfermedad=str(input("Que le molesta?"))
        for k in range(medicamentos):
            if medicamentos[enfermedad]=True:
                print(medicamentos) 


    else :
        print("que bueno que estes sano(a) "+ nombre) 
        enf_bool ="No"
    
    i += 1

 ##SALIDA

for i in range (n_personas):
    print("---------------------")
    print("Persona #",i+1)
    print( "Nombre: ", lista_nombres[i] )
    print( "Edad: ", lista_edades[i] )
    print( "Enfermo: ", enf_bool )
    print( "Género: ", lista_generos[i] )
    print("---------------------")
    
    
