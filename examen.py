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
                        dia = int(vardia.get())
                        mes = int(varmes.get())
                        año = int(varaño.get())
                        binadia = ''
                        binames = ''
                        binaño = ''
                        while dia1-1 !=0:
                            if dia1 % 2 == 0:
                                binadia += '0'
                                dia1 /= 2
                            else:
                                binadia += '1'
                                dia1 = int(dia1 / 2)
                        binadia += '1'
                        binadia = binadia[::-1]

                        while mes1-1 !=0:
                            if mes1 % 2 == 0:
                                binames += '0'
                                mes1 /= 2
                            else:
                                binames += '1'
                                mes1 = int(mes1 / 2)
                        binames += '1'
                        binames = binames[::-1]

                        while año1-1 !=0:
                            if año1 % 2 == 0:
                                binaño += '0'
                                año1 /= 2
                            else:
                                binaño += '1'
                                año1 = int(año1 / 2)
                        binaño += '1'
                        binaño = binaño[::-1]

                        if mes1<10:
                            labelres["text"] = str(dia) + '/0' + str(mes) + '/' + str(año) + ' = ' + binadia + '/' + binames + '/' + binaño
                        else:
                            labelres["text"] = str(dia) + '/' + str(mes) + '/' + str(año) + ' = ' + binadia + '/' + binames + '/' + binaño

def funcion_2 ():
    if txt1.get().strip() == "" or txt2.get().strip() == "" or vardia.get().strip() == "" or varmes.get().strip() == "" or varaño.get().strip() == "":
        labelres["text"]= "Todos los campos son requeridos"
    else:
        hoy = datetime.datetime.now()
        a = hoy.year
        m = hoy.month
        d = hoy.day
        actu = date(a, m, d)
        limidia = 0
        dia = int(vardia.get())
        mes = int(varmes.get())
        año = int(varaño.get())

        if dia==0 or mes == 0 or año==0:
            labelres["text"]= "No puede ingresar fechas '0'"
        else:
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
                    naci = date(año, mes, dia)
                    if naci>actu:
                        labelres["text"]= "La fecha no puede ser mayor a la actual"
                    else:      
                        diasvivid = actu-naci
                        if mes<10:
                            labelres["text"]= "Usted nació el " + str(dia) + "/0" + str(mes) + "/" + str(año) + " y ha vivido " + str(diasvivid.days) + " días"
                        else:
                            labelres["text"]= "Usted nació el " + str(dia) + "/" + str(mes) + "/" + str(año) + " y ha vivido " + str(diasvivid.days) + " días"
    
def funcion_3():
    if txt1.get().strip() == "" or txt2.get().strip() == "" or vardia.get().strip() == "" or varmes.get().strip() == "" or varaño.get().strip() == "":
        labelres["text"]= "Todos los campos son requeridos"
    else:
        hoy = datetime.datetime.now()
        a = hoy.year
        m = hoy.month
        d = hoy.day
        actu = date(a, m, d)
        limidia = 0
        dia = int(vardia.get())
        mes = int(varmes.get())
        año = int(varaño.get())

        if dia==0 or mes == 0 or año==0:
            labelres["text"]= "No puede ingresar fechas '0'"
        else:
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
                    naci = date(año, mes, dia)
                    if naci>actu:
                        labelres["text"]= "La fecha no puede ser mayor a la actual"
                    else:
                        nom = txt1.get()
                        ape = txt2.get()
                        tamnom = len(nom)
                        tamape = len(ape)
                        parnom = ''
                        parape = ''
                        if tamnom % 2 == 0:
                            parnom = 'su nombre es par'
                        else:
                            parnom = 'su nombre es impar'
                        if tamape % 2 == 0:
                            parape = 'su apellido es par'
                        else:
                            parape = 'su apellido es impar'
                        labelres["text"]= nom + " " + ape + " " + parnom + " y " + parape

def funcion_4():
    if txt1.get().strip() == "" or txt2.get().strip() == "" or vardia.get().strip() == "" or varmes.get().strip() == "" or varaño.get().strip() == "":
        labelres["text"]= "Todos los campos son requeridos"
    else:
        nom = txt1.get()
        ape = txt2.get()
        nom1 = nom.upper()
        ape1 = ape.upper()
        contvocal = 0
        contconso = 0
        hoy = datetime.datetime.now()
        a = hoy.year
        m = hoy.month
        d = hoy.day
        actu = date(a, m, d)
        limidia = 0
        dia = int(vardia.get())
        mes = int(varmes.get())
        año = int(varaño.get())

        if dia==0 or mes == 0 or año==0:
            labelres["text"]= "No puede ingresar fechas '0'"
        else:
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
                    naci = date(año, mes, dia)
                    if naci>actu:
                        labelres["text"]= "La fecha no puede ser mayor a la actual"
                    else:
                        for i in nom1:
                            if i == "A" or i == "Á":
                                contvocal += 1
                            elif i == "E" or i == "É":
                                contvocal += 1
                            elif i == "I" or i == "Í":
                                contvocal += 1
                            elif i == "O" or i == "Ó":
                                contvocal += 1
                            elif i == "U" or i == "Ú":
                                contvocal += 1
                            else:
                                contconso += 1

                        for i in ape1:
                            if i == "A" or i == "Á":
                                contvocal += 1
                            elif i == "E" or i == "É":
                                contvocal += 1
                            elif i == "I" or i == "Í":
                                contvocal += 1
                            elif i == "O" or i == "Ó":
                                contvocal += 1
                            elif i == "U" or i == "Ú":
                                contvocal += 1
                            else:
                                contconso += 1
    
                        labelres["text"]= nom + " " + ape + " tiene " + str(contvocal) + " vocales y " + str(contconso) + " consonantes" 

def funcion_5():
    if txt1.get().strip() == "" or txt2.get().strip() == "" or vardia.get().strip() == "" or varmes.get().strip() == "" or varaño.get().strip() == "":
        labelres["text"]= "Todos los campos son requeridos"
    else:
        nom = txt1.get()
        ape = txt2.get()
        revnom = nom[::-1]
        revape = ape[::-1]
        hoy = datetime.datetime.now()
        a = hoy.year
        m = hoy.month
        d = hoy.day
        actu = date(a, m, d)
        limidia = 0
        dia = int(vardia.get())
        mes = int(varmes.get())
        año = int(varaño.get())
        if dia==0 or mes == 0 or año==0:
            labelres["text"]= "No puede ingresar fechas '0'"
        else:
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

                    naci = date(año, mes, dia)
                    if naci>actu:
                        labelres["text"]= "La fecha no puede ser mayor a la actual"
                    else:
                        labelres["text"]= nom + " " + ape +" al revés es " + revape + " " + revnom


btn1 = tkinter.Button(miFrame, text = "Función 1", command = funcion_1)
btn2 = tkinter.Button(miFrame, text = "Función 2", command = funcion_2)
btn3 = tkinter.Button(miFrame, text = "Función 3", command = funcion_3)
btn4 = tkinter.Button(miFrame, text = "Función 4", command = funcion_4)
btn5 = tkinter.Button(miFrame, text = "Función 5", command = funcion_5)

welcomelbl.grid(row = 0, column = 0, columnspan = 6)
label1.grid(row = 1, column = 1, columnspan = 2)
label2.grid(row = 2, column = 1, columnspan = 2)
label3.grid(row = 3, column = 1, columnspan = 2)
label4.grid(row = 4, column = 1, columnspan = 2)
label5.grid(row = 5, column = 1, columnspan = 2)
labelres.grid(row = 7, column = 0, columnspan = 6)

txt1.grid(row = 1, column = 3, columnspan = 4, sticky = W + E)
txt2.grid(row = 2, column = 3, columnspan = 4, sticky = W + E)
vardia.grid(row = 3, column = 3, columnspan = 4, sticky = W + E)
varmes.grid(row = 4, column = 3, columnspan = 4, sticky = W + E)
varaño.grid(row = 5, column = 3, columnspan = 4, sticky = W + E)

btn1.grid(row = 6, column = 1)
btn2.grid(row = 6, column = 2)
btn3.grid(row = 6, column = 3)
btn4.grid(row = 6, column = 4)
btn5.grid(row = 6, column = 5)

window.mainloop()