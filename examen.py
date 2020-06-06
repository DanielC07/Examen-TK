#Importacion de librerias TK
import tkinter
from tkinter import *
#Importacion de librerias para fechas
from datetime import date
import datetime

#Creacion de Tk
window = tkinter.Tk()

#Se colocó título al Tk
window.title("Examen Final")

#Se le dieron las dimensiones al tk
window.geometry("400x200")

#Se creó Frame
miFrame = Frame(window)
miFrame.pack()

#Creacion de Labels que irán dentro del Frame
welcomelbl = tkinter.Label(miFrame, text = "BIENVENIDO", font = ("arial", 15))
label1 = tkinter.Label(miFrame, text = "Nombre")
label2 = tkinter.Label(miFrame, text = "Apellido")
label3 = tkinter.Label(miFrame, text = "Día")
label4 = tkinter.Label(miFrame, text = "Mes")
label5 = tkinter.Label(miFrame, text = "Año")
labelres = tkinter.Label(miFrame, text = "Acá se verá el resultado de las funciones")

#Creacion de Entrys que irán dentro del Frame
txt1 = tkinter.Entry(miFrame)
txt2 = tkinter.Entry(miFrame)
vardia = Entry(miFrame)
varmes = Entry(miFrame)
varaño = Entry(miFrame)

#Creacion de primera funcion
def funcion_1():
    #Condicion para validar campos
    if txt1.get().strip() == "" or txt2.get().strip() == "" or vardia.get().strip() == "" or varmes.get().strip() == "" or varaño.get().strip() == "":
        
        labelres["text"]= "Todos los campos son requeridos"
    else:
        #Se guarda el texto recibido y se convierte a entero
        dia1 = int(vardia.get())
        mes1 = int(varmes.get())
        año1 = int(varaño.get())

        #Se obtiene tiempo actual
        hoy = datetime.datetime.now()

        #Se obtienen dia, mes y año actual
        a = hoy.year
        m = hoy.month
        d = hoy.day

        #Se obtiene fecha actual
        actu = date(a, m, d)

        #Contador de días máximos que se pueden ingresar en la fecha
        limidia = 0

        #Se comprueba que la fecha ingresada sea válida
        if dia1==0 or mes1 == 0 or año1==0:
            labelres["text"]= "No puede ingresar fechas '0'"
        else:
            if año1 <= 0:
                labelres["text"]= "El año no puede ser menor a 0, ingreselo nuevamente"
            if mes1 <= 0 or mes1 >12:
                labelres["text"]= "El mes solo puede variar de 1 a 12, ingreselo nuevamente"
            else:
                if año1 % 4 == 0:
                    if mes1 == 2:
                        limidia = 29
                    else:
                        if mes1 == 1 or mes1 == 3 or mes1 == 5 or mes1 == 7 or mes1 == 8 or mes1 == 10 or mes1 == 12:
                            limidia = 31
                        else:
                            limidia = 30
                else:
                    if mes1 == 2:
                        limidia = 28
                    else:
                        if mes1 == 1 or mes1 == 3 or mes1 == 5 or mes1 == 7 or mes1 == 8 or mes1 == 10 or mes1 == 12:
                            limidia = 31
                        else:
                            limidia = 30
                if dia1 <= 0 or dia1 > limidia:
                    labelres["text"]= "El mes ingresado solo tiene " + str(limidia) + " días"
                else:
                    naci = date(año1, mes1, dia1)
                    if naci>actu:
                        labelres["text"]= "La fecha no puede ser mayor a la actual"
                    else:
                        #Una vez ya validadas las fechas se almacenan nuevamente para poder mostrar la fecha correcta
                        dia = int(vardia.get())
                        mes = int(varmes.get())
                        año = int(varaño.get())

                        #Creacion de Strings para almacenar los binarios
                        binadia = ''
                        binames = ''
                        binaño = ''

                        #Creacion de ciclo while que recorra el dia ingresado y le vaya restando 1 mientras sea distinto de 0
                        while dia1-1 !=0:

                            #Condicion para extraer el residuo para poder obtener los binarios
                            if dia1 % 2 == 0:
                                binadia += '0'
                                dia1 /= 2
                            else:
                                binadia += '1'
                                dia1 = int(dia1 / 2)
                        binadia += '1'
                        binadia = binadia[::-1]

                        #Creacion de ciclo while que recorra el mes ingresado y le vaya restando 1 mientras sea distinto de 0
                        while mes1-1 !=0:

                            #Condicion para extraer el residuo para poder obtener los binarios
                            if mes1 % 2 == 0:
                                binames += '0'
                                mes1 /= 2
                            else:
                                binames += '1'
                                mes1 = int(mes1 / 2)
                        binames += '1'
                        binames = binames[::-1]

                        #Creacion de ciclo while que recorra el año ingresado y le vaya restando 1 mientras sea distinto de 0
                        while año1-1 !=0:

                            #Condicion para extraer el residuo para poder obtener los binarios
                            if año1 % 2 == 0:
                                binaño += '0'
                                año1 /= 2
                            else:
                                binaño += '1'
                                año1 = int(año1 / 2)
                        binaño += '1'
                        binaño = binaño[::-1]

                        #Condicion para que agregue un "0" al número del mes si es menor a 10
                        if mes1<10:

                            #Impresion por label del resultado
                            labelres["text"] = str(dia) + '/0' + str(mes) + '/' + str(año) + ' = ' + binadia + '/' + binames + '/' + binaño
                        
                        else:
                            #Impresion por label del resultado
                            labelres["text"] = str(dia) + '/' + str(mes) + '/' + str(año) + ' = ' + binadia + '/' + binames + '/' + binaño

def funcion_2 ():
    #Validacion de campos
    if txt1.get().strip() == "" or txt2.get().strip() == "" or vardia.get().strip() == "" or varmes.get().strip() == "" or varaño.get().strip() == "":
        
        labelres["text"]= "Todos los campos son requeridos"
    else:
        #Se obtiene fecha actual
        hoy = datetime.datetime.now()

        #Se almacenan el año, mes y dia actual en distintas variables
        a = hoy.year
        m = hoy.month
        d = hoy.day

        #Se almacena la fecha actual
        actu = date(a, m, d)

        #Contador de días máximos que se pueden ingresar en la fecha
        limidia = 0

        #Se obtienen los datos de los entry
        dia = int(vardia.get())
        mes = int(varmes.get())
        año = int(varaño.get())

        #Condicion para que el usuario no ingrese fechas "0"
        if dia==0 or mes == 0 or año==0:

            labelres["text"]= "No puede ingresar fechas '0'"
        else:
            #Condicion para validar fechas ingresadas
            if año <= 0:

                labelres["text"]= "El año no puede ser menor a 0, ingreselo nuevamente"
            if mes <= 0 or mes >12:
                labelres["text"]= "El mes solo puede variar de 1 a 12, ingreselo nuevamente"
            else:
                if año % 4 == 0:
                    if mes == 2:
                        limidia = 29
                    else:
                        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                            limidia = 31
                        else:
                            limidia = 30
                else:
                    if mes == 2:
                        limidia = 28
                    else:
                        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                            limidia = 31
                        else:
                            limidia = 30
                if dia <= 0 or dia > limidia:
                    labelres["text"]= "El mes ingresado solo tiene " + str(limidia) + " días"
                else:

                    #Se almacena la fecha ingresada una vez que se valida
                    naci = date(año, mes, dia)

                    #Condicion para que el usuario no ingrese fechas mayores a la actual
                    if naci>actu:

                        labelres["text"]= "La fecha no puede ser mayor a la actual"
                    else:      
                        #Resta entre la fecha actual menos la fecha de nacimiento para obtener los días vividos
                        diasvivid = actu-naci

                        #Condicion para mostrar un "0" junto al número del mes si es menor a 10
                        if mes<10:

                            #Mostrar el resultado final en el label
                            labelres["text"]= "Usted nació el " + str(dia) + "/0" + str(mes) + "/" + str(año) + " y ha vivido " + str(diasvivid.days) + " días"
                        
                        else:
                            #Mostrar el resultado final en el label
                            labelres["text"]= "Usted nació el " + str(dia) + "/" + str(mes) + "/" + str(año) + " y ha vivido " + str(diasvivid.days) + " días"
    
def funcion_3():
    #Condicion de validacion de datos
    if txt1.get().strip() == "" or txt2.get().strip() == "" or vardia.get().strip() == "" or varmes.get().strip() == "" or varaño.get().strip() == "":
        
        labelres["text"]= "Todos los campos son requeridos"
    else:
        #Se almacena fecha actual
        hoy = datetime.datetime.now()

        #Se almacena año, mes y dias actual en diferentes variables
        a = hoy.year
        m = hoy.month
        d = hoy.day

        #Se almacena fecha actual
        actu = date(a, m, d)

        #Contador de días máximos que se pueden ingresar en la fecha
        limidia = 0

        #Se obtienen los datos de las fechas y se convierten interos
        dia = int(vardia.get())
        mes = int(varmes.get())
        año = int(varaño.get())

        #Condicion para validar que las fechas no sean "0"
        if dia==0 or mes == 0 or año==0:
            
            labelres["text"]= "No puede ingresar fechas '0'"
        else:
            #Condicion para que fecha se validada
            if año <= 0:
                
                labelres["text"]= "El año no puede ser menor a 0, ingreselo nuevamente"
            if mes <= 0 or mes >12:
                labelres["text"]= "El mes solo puede variar de 1 a 12, ingreselo nuevamente"
            else:
                if año % 4 == 0:
                    if mes == 2:
                        limidia = 29
                    else:
                        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                            limidia = 31
                        else:
                            limidia = 30
                else:
                    if mes == 2:
                        limidia = 28
                    else:
                        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                            limidia = 31
                        else:
                            limidia = 30
                if dia <= 0 or dia > limidia:
                    labelres["text"]= "El mes ingresado solo tiene " + str(limidia) + " días"
                else:
                    #Se almacena la fecha ingresada una vez ya esté validada
                    naci = date(año, mes, dia)

                    #Condicion para que el usuario no ingrese una fecha mayor a la actual
                    if naci>actu:
                        labelres["text"]= "La fecha no puede ser mayor a la actual"
                    else:
                        #Se obtiene el nombre y apellido del usuario
                        nom = txt1.get()
                        ape = txt2.get()

                        #Se hace uso del atributo len de los strings para saber cuantos caracteres tiene la palabra y se almacena la cantidad
                        tamnom = len(nom)
                        tamape = len(ape)

                        #Se crean variables que almacenaran si el nombre y apellido tiene cantidad de letras pares o no
                        parnom = ''
                        parape = ''

                        #Condicion para validar si el nombre tiene cantidad de caracteres pares
                        if tamnom % 2 == 0:
                            
                            parnom = 'su nombre es par'
                        else:
                            parnom = 'su nombre es impar'

                        #Condicion para validar si el nombre tiene cantidad de caracteres pares 
                        if tamape % 2 == 0:
                            
                            parape = 'su apellido es par'
                        else:
                            parape = 'su apellido es impar'

                        #Se muestra el resultado en el label
                        labelres["text"]= nom + " " + ape + " " + parnom + " y " + parape

def funcion_4():
    #Se validan los datos
    if txt1.get().strip() == "" or txt2.get().strip() == "" or vardia.get().strip() == "" or varmes.get().strip() == "" or varaño.get().strip() == "":
        
        labelres["text"]= "Todos los campos son requeridos"
    else:
        #Se obtiene nombre y apellido del usuario
        nom = txt1.get()
        ape = txt2.get()

        #Se utiliza atributo de los strings para convertir todo el texto a mayusculas y se almacena en diferente variable
        nom1 = nom.upper()
        ape1 = ape.upper()

        #Se crean variables que llevaran el conteo de las vocales y consonantes
        contvocal = 0
        contconso = 0

        #Se obtiene la fecha actual
        hoy = datetime.datetime.now()

        #Se almacena el año, mes y dia actual
        a = hoy.year
        m = hoy.month
        d = hoy.day

        #Se almacena fecha actual
        actu = date(a, m, d)

        #Contador de días máximos que se pueden ingresar en la fecha
        limidia = 0

        #Se obtienen la fecha ingresada por el usuario
        dia = int(vardia.get())
        mes = int(varmes.get())
        año = int(varaño.get())

        #Condicion para que las fechas ingresadas no sean 0
        if dia==0 or mes == 0 or año==0:
            
            labelres["text"]= "No puede ingresar fechas '0'"
        else:
            #Condicion para validacion de fecha ingresada
            if año <= 0:
                labelres["text"]= "El año no puede ser menor a 0, ingreselo nuevamente"
            if mes <= 0 or mes >12:
                labelres["text"]= "El mes solo puede variar de 1 a 12, ingreselo nuevamente"
            else:
                if año % 4 == 0:
                    if mes == 2:
                        limidia = 29
                    else:
                        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                            limidia = 31
                        else:
                            limidia = 30
                else:
                    if mes == 2:
                        limidia = 28
                    else:
                        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                            limidia = 31
                        else:
                            limidia = 30
                if dia <= 0 or dia > limidia:
                    labelres["text"]= "El mes ingresado solo tiene " + str(limidia) + " días"
                else:

                    #Se almacena fecha actual una vez se haya confirmado que es verídica
                    naci = date(año, mes, dia)

                    #Condicion para que el usuario no ingrese fecha mayor a la actual
                    if naci>actu:
                        labelres["text"]= "La fecha no puede ser mayor a la actual"
                    else:
                        #Ciclo for para recorrer cada caracter del nombre obtenido en mayusculas
                        for i in nom1:

                            #Condiciones para encontrar vocales en ek nombre tanto letra tónica como átona
                            if i == "A" or i == "Á":

                                #Aumenta el contador de vocales en 1
                                contvocal += 1

                            elif i == "E" or i == "É":
                                #Aumenta el contador de vocales en 1
                                contvocal += 1

                            elif i == "I" or i == "Í":
                                #Aumenta el contador de vocales en 1
                                contvocal += 1

                            elif i == "O" or i == "Ó":
                                #Aumenta el contador de vocales en 1
                                contvocal += 1

                            elif i == "U" or i == "Ú":
                                #Aumenta el contador de vocales en 1
                                contvocal += 1

                            else:
                                #Aumenta el contador de consonantes en 1
                                contconso += 1

                        #Ciclo for para recorrer cada caracter del nombre obtenido en mayusculas
                        for i in ape1:

                            #Condiciones para encontrar vocales en ek apellido tanto letra tónica como átona
                            if i == "A" or i == "Á":

                                #Aumenta el contador de vocales en 1
                                contvocal += 1

                            elif i == "E" or i == "É":
                                #Aumenta el contador de vocales en 1
                                contvocal += 1

                            elif i == "I" or i == "Í":
                                #Aumenta el contador de vocales en 1
                                contvocal += 1

                            elif i == "O" or i == "Ó":
                                #Aumenta el contador de vocales en 1
                                contvocal += 1

                            elif i == "U" or i == "Ú":
                                #Aumenta el contador de vocales en 1
                                contvocal += 1

                            else:
                                #Aumenta el contador de consonantes en 1
                                contconso += 1

                        #Se muestra el resultado
                        labelres["text"]= nom + " " + ape + " tiene " + str(contvocal) + " vocales y " + str(contconso) + " consonantes" 

def funcion_5():
    #Validacion de campos
    if txt1.get().strip() == "" or txt2.get().strip() == "" or vardia.get().strip() == "" or varmes.get().strip() == "" or varaño.get().strip() == "":
        
        labelres["text"]= "Todos los campos son requeridos"
    else:
        #Se obtiene el nombre y apellido del usuario
        nom = txt1.get()
        ape = txt2.get()

        #Se invierte las posiciones de los caracteres y se almacenan en otras variables
        revnom = nom[::-1]
        revape = ape[::-1]

        #Se obtiene fecha actual
        hoy = datetime.datetime.now()

        #Se almacena el ano, mes y dia actuales
        a = hoy.year
        m = hoy.month
        d = hoy.day

        #Se almacena fecha actual
        actu = date(a, m, d)

        #Contador de días máximos que se pueden ingresar en la fecha
        limidia = 0

        #Se obtiene fecha ingresada por el usuario
        dia = int(vardia.get())
        mes = int(varmes.get())
        año = int(varaño.get())

        #Condicion para que el usuario no im¿ngrese fechas con cantidades 0
        if dia==0 or mes == 0 or año==0:
           
            labelres["text"]= "No puede ingresar fechas '0'"
        else:
            #Validacion de fecha ingresada
            if año <= 0:

                labelres["text"]= "El año no puede ser menor a 0, ingreselo nuevamente"
            if mes <= 0 or mes >12:
                labelres["text"]= "El mes solo puede variar de 1 a 12, ingreselo nuevamente"
            else:
                if año % 4 == 0:
                    if mes == 2:
                        limidia = 29
                    else:
                        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                            limidia = 31
                        else:
                            limidia = 30
                else:
                    if mes == 2:
                        limidia = 28
                    else:
                        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                            limidia = 31
                        else:
                            limidia = 30
                if dia <= 0 or dia > limidia:
                    labelres["text"]= "El mes ingresado solo tiene " + str(limidia) + " días"
                else:
                    #Se almacena la fecha ingresada una vez se haya validado
                    naci = date(año, mes, dia)

                    #Condicion para comparar fechas para que no ingresen fechas mayores a la actual
                    if naci>actu:

                        labelres["text"]= "La fecha no puede ser mayor a la actual"
                    else:
                        #Se muestra el resultado
                        labelres["text"]= nom + " " + ape +" al revés es " + revape + " " + revnom

#Se les da una variable a los botones y se les asigna una funcion específica
btn1 = tkinter.Button(miFrame, text = "Función 1", command = funcion_1)
btn2 = tkinter.Button(miFrame, text = "Función 2", command = funcion_2)
btn3 = tkinter.Button(miFrame, text = "Función 3", command = funcion_3)
btn4 = tkinter.Button(miFrame, text = "Función 4", command = funcion_4)
btn5 = tkinter.Button(miFrame, text = "Función 5", command = funcion_5)

#Se colocan los labels en las posiciones requeridas y se combinan las celdas de los que lo requieran
welcomelbl.grid(row = 0, column = 0, columnspan = 6)
label1.grid(row = 1, column = 1, columnspan = 2)
label2.grid(row = 2, column = 1, columnspan = 2)
label3.grid(row = 3, column = 1, columnspan = 2)
label4.grid(row = 4, column = 1, columnspan = 2)
label5.grid(row = 5, column = 1, columnspan = 2)
labelres.grid(row = 7, column = 0, columnspan = 6)

#Se colocan los labels en las posiciones requeridas y se combinan las celdas de los que lo requieran
txt1.grid(row = 1, column = 3, columnspan = 4, sticky = W + E)
txt2.grid(row = 2, column = 3, columnspan = 4, sticky = W + E)
vardia.grid(row = 3, column = 3, columnspan = 4, sticky = W + E)
varmes.grid(row = 4, column = 3, columnspan = 4, sticky = W + E)
varaño.grid(row = 5, column = 3, columnspan = 4, sticky = W + E)

#Se colocan los botones en las posiciones que se requieren
btn1.grid(row = 6, column = 1)
btn2.grid(row = 6, column = 2)
btn3.grid(row = 6, column = 3)
btn4.grid(row = 6, column = 4)
btn5.grid(row = 6, column = 5)

#Se crea el maniloop para poder visualizar la ventana del Tkinter
window.mainloop()