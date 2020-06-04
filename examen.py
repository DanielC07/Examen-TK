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

window.mainloop()