import os,sys
os.system("cls")

print("---------- Bienvenido al sistema de registro de familias ----------")

## INPUT
n_personas = int(input("Ingrese el número de personas en el domicilio: "))
n_enfermos = 0
genero = ""
calorias=""
respuesta_medicamentos=""
lista_nombres = []
lista_edades = []
lista_generos = []
lista_enfermos=[]
medicamentos={"Pecho":"aspirina","Cabeza":"Ibuprofeno","Músculos":"Relajante","Estómago":"Desintoxicante","Garganta":"Desinflamatorio","Asma":"Salbutamol"}
i = 0

while (i<n_personas):
 ##registro de persona
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
        ## genero de la persona
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
  ## la persona esta enferma??
        enfermo = input("¿Está la persona enferma? (Sí/No): ")

        if (enfermo.lower() == "si"):
            n_enfermos += 1
            lista_enfermos.append(enfermo.title())
            enfermedad=str(input("Que le duele?"))
            
            for k in range(0, len(medicamentos)):
                if(enfermedad.title() in medicamentos):
                    respuesta_medicamento=("Usted deberia tomar", medicamentos[enfermedad.title()])
                    
                else:
                    respuesta_medicamento=("Usted deberia ir al medico")
                    
            break
        elif (enfermo.lower() == "no"):
            print("Qué bueno que estés sano(a) "+ nombre) 
            lista_enfermos.append(enfermo.title())

            break

        else :
            print("Ingrese una respuesta válida (Sí/No).")

      ## numero de kilocalorias persona
            
                
    if etapa== "infante":
        calorias="Usted deberia consumir 1400 kilocalorias"
    elif etapa=="adolescente":
        calorias="Usted deberia consumir 1600 kilocalorias"
    elif etapa=="adulto" and genero=="Mujer":
        calorias="Usted deberia consumir 2000 kilocalorias"
    elif etapa=="adulto" and genero=="Hombre":
        calorias="Usted deberia consumir 2250 kilocalorias"
    elif etapa=="adulto mayor":
        calorias="Usted deberia consumir 2100 kilocalorias"
    i=i+1

lista_nombres.append(nombre)
lista_edades.append(edad)

##SALIDA

for i in range (n_personas):
    print("---------------------")
    print("Persona #",i+1)
    print( "Nombre: ", lista_nombres[i] )
    print( "Edad: ", lista_edades[i] )
    print("Etapa: ", etapa )
    print(calorias)
    print( "Enfermo: ", lista_enfermos[i] )
    print(respuesta_medicamento)
    print( "Género: ", lista_generos[i] )
    print("---------------------")
 
print("Número total de enfermos: ", n_enfermos)

    
