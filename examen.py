import tkinter

window = tkinter.Tk()
window.title("Examen Final")

welcomelbl = tkinter.Label(window, text = "BIENVENIDO", font = ("arial", 18))
label1 = tkinter.Label(window, text = "Nombre")
label2 = tkinter.Label(window, text = "Apellido")
label3 = tkinter.Label(window, text = "Día")
label4 = tkinter.Label(window, text = "Mes")
label5 = tkinter.Label(window, text = "Año")
labelres = tkinter.Label(window, text = "Acá se verá el resultado de las funciones")

txt1 = tkinter.Entry(window)
txt2 = tkinter.Entry(window)
txt3 = tkinter.Entry(window)
txt4 = tkinter.Entry(window)
txt5 = tkinter.Entry(window)

btn1 = tkinter.Button(window, text = "Función 1")
btn2 = tkinter.Button(window, text = "Función 2")
btn3 = tkinter.Button(window, text = "Función 3")
btn4 = tkinter.Button(window, text = "Función 4")
btn5 = tkinter.Button(window, text = "Función 5")

welcomelbl.grid(row = 0, column = 0, columnspan = 6)
label1.grid(row = 1, column = 1, columnspan = 2)
label2.grid(row = 2, column = 1, columnspan = 2)
label3.grid(row = 3, column = 1, columnspan = 2)
label4.grid(row = 4, column = 1, columnspan = 2)
label5.grid(row = 5, column = 1, columnspan = 2)
labelres.grid(row = 7, column = 0, columnspan = 6)

txt1.grid(row = 1, column = 2, columnspan = 4)
txt2.grid(row = 2, column = 2, columnspan = 4)
txt3.grid(row = 3, column = 2, columnspan = 4)
txt4.grid(row = 4, column = 2, columnspan = 4)
txt5.grid(row = 5, column = 2, columnspan = 4)

btn1.grid(row = 6, column = 1)
btn2.grid(row = 6, column = 2)
btn3.grid(row = 6, column = 3)
btn4.grid(row = 6, column = 4)
btn5.grid(row = 6, column = 5)

window.mainloop()