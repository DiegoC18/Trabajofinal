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
medicamentos={"Pecho":"aspirina","Cabeza":"Ibuprofeno","Músculos":"Relajante","Estómago":"Desintoxicante","Garganta":"Desinflamatorio","Asma":"Salbutamol"}
i = 0

while (i<n_personas):

    print(" ")
    print("PERSONA #",i+1)

    nombre = input("Ingrese el nombre de la persona: ")

    edad = int(input("Ingrese edad de la persona: "))  

    infantes = 0
    adolescentes = 0
    adultos = 0
    adultos_mayores = 0
    
    if 0<=edad<13:
        infantes=infantes+1
        etapa = "infante"
    elif 13<=edad<20:
        adolescentes=adolescentes+1
        etapa = "adolescente"
    elif 20<=edad<60:
        adultos=adultos+1
        etapa = "adulto"
    else:
        adultos_mayores=adultos_mayores+1
        etapa = "adulto mayor"

    while True:

        gen_pregunta = input("sexo? (H/M): ")

        if gen_pregunta.lower() == "h":
            genero = "Hombre"
            lista_generos.append(genero)
            break

        if gen_pregunta.lower() == "m":
            genero = "Mujer"
            lista_generos.append(genero)
            break

        else :
            print("Ingrese una respuesta válida (H/M).")

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
            print("Ingrese una respuesta válida (Sí/No).")
                
  
    i += 1

    lista_nombres.append(nombre)
    lista_edades.append(edad)

##SALIDA

for i in range (n_personas):
    print("---------------------")
    print("Persona #",i+1)
    print( "Nombre: ", lista_nombres[i] )
    print( "Edad: ", lista_edades[i] )
    print("Etapa: ", etapa )
    print( "Enfermo: ", lista_enfermos[i] )
    print( "Género: ", lista_generos[i] )
    print("---------------------")
 
print("Número total de enfermos: ", n_enfermos)

    
