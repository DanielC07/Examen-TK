import tkinter
from tkinter import *
from datetime import date
import datetime

window = tkinter.Tk()
window.title("Examen Final")
window.geometry("400x200")

miFrame = Frame(window)
miFrame.pack()

welcomelbl = tkinter.Label(miFrame, text = "BIENVENIDO", font = ("arial", 15))
label1 = tkinter.Label(miFrame, text = "Nombre")
label2 = tkinter.Label(miFrame, text = "Apellido")
label3 = tkinter.Label(miFrame, text = "Día")
label4 = tkinter.Label(miFrame, text = "Mes")
label5 = tkinter.Label(miFrame, text = "Año")
labelres = tkinter.Label(miFrame, text = "Acá se verá el resultado de las funciones")

txt1 = tkinter.Entry(miFrame)
txt2 = tkinter.Entry(miFrame)
vardia = Entry(miFrame)
varmes = Entry(miFrame)
varaño = Entry(miFrame)

def funcion_1():
    if txt1.get().strip() == "" or txt2.get().strip() == "" or vardia.get().strip() == "" or varmes.get().strip() == "" or varaño.get().strip() == "":
        labelres["text"]= "Todos los campos son requeridos"
    else:
        dia1 = int(vardia.get())
        mes1 = int(varmes.get())
        año1 = int(varaño.get())
        hoy = datetime.datetime.now()
        a = hoy.year
        m = hoy.month
        d = hoy.day
        actu = date(a, m, d)
        if dia1==0 or mes1 == 0 or año1==0:
            labelres["text"]= "No puede ingresar fechas '0'"
        elif dia1>d and mes1>m and año1>=a:
            labelres["text"]= "Las fechas no puede ser mayor a la actual"
        elif dia1>d and mes1>=m and año1>=a:
            labelres["text"]= "Aún no hemos llegado a ese día"
        elif mes1>m and año1>=a:
            labelres["text"]= "Aún no hemos llegado a ese mes"
        elif dia1<= d and mes1<=m and año1>a:
            labelres["text"]= "Aún no hemos llegado a ese año"
        elif dia1 == 29 and mes1 == 2 and año1 % 4 !=0:
            labelres["text"]= "Ese año no es bisiesto, el mes solo tiene un máximo de 28 días"
        elif dia1>29 and mes1 == 2:
            labelres["text"]= "Recuerde que febrero solo puede tener un max de 29 días"
        elif mes1 == 1 or mes1 == 3 or mes1 == 5 or mes1 == 7 or mes1 == 8 or mes1 == 10 or mes1 == 12 and dia1>31:
            labelres["text"]= "El mes ingresado solo tiene un máximo de 31 días"
        elif mes1 == 4 or mes1 == 6 or mes1 == 9 or mes1 == 11 and dia1>30:
            labelres["text"]= "El mes ingresado solo tiene un máximo de 30 días"
        else:
        
            naci = date(año1, mes1, dia1)
        
            if naci>actu:
                labelres["text"]= "Las fechas no puede ser mayor a la actual"
            else:
                dia = vardia.get()
                mes = varmes.get()
                año = varaño.get()
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
        elif dia>d and mes>m and año>=a:
            labelres["text"]= "Las fechas no puede ser mayor a la actual"
        elif dia>d and mes>=m and año>=a:
            labelres["text"]= "Aún no hemos llegado a ese día"
        elif mes>m and año>=a:
            labelres["text"]= "Aún no hemos llegado a ese mes"
        elif dia<= d and mes<=m and año>a:
            labelres["text"]= "Aún no hemos llegado a ese año"
        elif dia == 29 and mes == 2 and año % 4 !=0:
            labelres["text"]= "Ese año no es bisiesto, el mes solo tiene un máximo de 28 días"
        elif dia>29 and mes == 2:
            labelres["text"]= "Recuerde que febrero solo puede tener un max de 29 días"
        elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12 and dia>31:
            labelres["text"]= "El mes ingresado solo tiene un máximo de 31 días"
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11 and dia>30:
            labelres["text"]= "El mes ingresado solo tiene un máximo de 30 días"
        else:

            naci = date(año, mes, dia)
            if naci>actu:
                labelres["text"]= "Las fechas no puede ser mayor a la actual"
            else:      
                diasvivid = actu-naci
                labelres["text"]= "Usted nació el " + str(dia) + "/" + str(mes) + "/" + str(año) + " y ha vivido " + str(diasvivid.days) + " días"

def funcion_3():
    if txt1.get().strip() == "" or txt2.get().strip() == "" or vardia.get().strip() == "" or varmes.get().strip() == "" or varaño.get().strip() == "":
        labelres["text"]= "Todos los campos son requeridos"
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