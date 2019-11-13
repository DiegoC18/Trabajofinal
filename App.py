import os,sys
os.system("cls")

print("********** Ministerio de desarrollo e inclusión social ***********")
print(" ")
print("---------- Bienvenido al sistema de registro de familias ----------")
print(" ")

## INPUT
n_personas = int(input("Ingrese el número de personas en el domicilio: "))
n_enfermos = 0
genero = ""
calorias=""
respuesta_medicamento=""
lista_nombres = []
lista_edades = []
lista_generos = []
lista_enfermos=[]
lista_etapas=[]
lista_calorias=[]
medicamentos={"Pecho":"aspirina","Cabeza":"Ibuprofeno","Músculos":"Relajante","Estómago":"Desintoxicante","Garganta":"Desinflamatorio","Asma":'Salbutamol'}
lista_medicamentos= []
i = 0
a=0
b=0
c=0
e=0

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
        lista_etapas.append(etapa)
    elif 13<=edad<20:
        adolescentes=adolescentes+1
        etapa = "adolescente"
        lista_etapas.append(etapa)
    elif 20<=edad<60:
        adultos=adultos+1
        etapa = "adulto"
        lista_etapas.append(etapa)
    else:
        adultos_mayores=adultos_mayores+1
        etapa = "adulto mayor"
        lista_etapas.append(etapa)

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

        if (enfermo.lower() == "si" or enfermo.lower() == "sí"):
            n_enfermos += 1
            lista_enfermos.append(enfermo.title())
            enfermedad=str(input("¿Que le duele? "))
            for k in range(0, 1):
                if(enfermedad.title() in medicamentos):
                    e=1
                else:
                    e=0
            if(e==1):
                respuesta_medicamento=medicamentos[enfermedad.title()]
                lista_medicamentos.append(respuesta_medicamento)
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
            
                
    if etapa == "infante":
        calorias="Usted deberia consumir 1400 kilocalorias diariamente"
        lista_calorias.append(calorias)
    elif etapa =="adolescente":
        calorias="Usted deberia consumir 1600 kilocalorias diariamente"
        lista_calorias.append(calorias)
    elif etapa =="adulto" and genero=="Mujer":
        calorias="Usted deberia consumir 2000 kilocalorias diariamente"
        lista_calorias.append(calorias)
    elif etapa =="adulto" and genero=="Hombre":
        calorias="Usted deberia consumir 2250 kilocalorias diariamente"
        lista_calorias.append(calorias)
    elif etapa =="adulto mayor":
        calorias="Usted deberia consumir 2100 kilocalorias diariamente"
        lista_calorias.append(calorias)
    i=i+1

    if etapa =="infante" or etapa=="adolescente":
        a=a+1
    elif etapa=="adulto":
        b=b+1
    elif etapa=="adulto mayor":
        c=c+1


    lista_nombres.append(nombre)
    lista_edades.append(edad)

##SALIDA

for i in range (0,n_personas):
    print("---------------------")
    print("Persona #",i+1)
    print( "Nombre: ", lista_nombres[i] )
    print( "Edad: ", lista_edades[i] )
    print("Etapa: ", lista_etapas[i] )
    print(lista_calorias[i])
    print( "Enfermo: ", lista_enfermos[i] )
    if (lista_enfermos[i] == "Si"): 
        print(respuesta_medicamento)
    if (lista_enfermos[i] == "No"):
        print("La persona está sana")   
    print( "Género: ", lista_generos[i] )
    print("---------------------")
 
print("Se le va a ayudar con un monto de ",a*800+b*400+c*600,"soles" )
print("Número total de enfermos: ", n_enfermos)
