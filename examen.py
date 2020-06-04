import tkinter
from tkinter import *

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
txt3 = tkinter.Entry(miFrame)
txt4 = tkinter.Entry(miFrame)
txt5 = tkinter.Entry(miFrame)

def funcion_2 ():
    txtdia = txt3.get()
    txtmes = txt4.get()
    txtaño = txt5.get()
    labelres["text"] = 'Usted nació el ' + txtdia + '/' + txtmes + '/' + txtaño


btn1 = tkinter.Button(miFrame, text = "Función 1")
btn2 = tkinter.Button(miFrame, text = "Función 2", command = funcion_1)
btn3 = tkinter.Button(miFrame, text = "Función 3")
btn4 = tkinter.Button(miFrame, text = "Función 4")
btn5 = tkinter.Button(miFrame, text = "Función 5")

welcomelbl.grid(row = 0, column = 0, columnspan = 6)
label1.grid(row = 1, column = 1, columnspan = 2)
label2.grid(row = 2, column = 1, columnspan = 2)
label3.grid(row = 3, column = 1, columnspan = 2)
label4.grid(row = 4, column = 1, columnspan = 2)
label5.grid(row = 5, column = 1, columnspan = 2)
labelres.grid(row = 7, column = 0, columnspan = 6)

txt1.grid(row = 1, column = 3, columnspan = 4, sticky = W+E)
txt2.grid(row = 2, column = 3, columnspan = 4, sticky = W+E)
txt3.grid(row = 3, column = 3, columnspan = 4, sticky = W+E)
txt4.grid(row = 4, column = 3, columnspan = 4, sticky = W+E)
txt5.grid(row = 5, column = 3, columnspan = 4, sticky = W+E)

btn1.grid(row = 6, column = 1)
btn2.grid(row = 6, column = 2)
btn3.grid(row = 6, column = 3)
btn4.grid(row = 6, column = 4)
btn5.grid(row = 6, column = 5)

window.mainloop()