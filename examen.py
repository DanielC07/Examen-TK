import tkinter

window = tkinter.Tk()
window.geometry("800x300")

label1 = tkinter.Label(window, text = "Nombre")
label1 = tkinter.Label(window, text = "Apellido")
label1 = tkinter.Label(window, text = "Día")
label1 = tkinter.Label(window, text = "Mes")
label1 = tkinter.Label(window, text = "Año")

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

window.mainloop()