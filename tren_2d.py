from tkinter import *

#-----------------------
# variables globales
#-----------------------

BASE = 460
ALTURA = 220

#-----------------------
# ventana principal
#-----------------------
ventana_principal = Tk()
ventana_principal.title("Tren 2D")
ventana_principal.resizable(False, False)
ventana_principal.geometry(f"500x500")
ventana_principal.config(bg="black")

#-----------------------
# frame de graficación
#-----------------------
frame_graficacion = Frame(ventana_principal, width=480, height=240)
frame_graficacion.config(bg="light slate blue", width=480, height=240)
frame_graficacion.place(x=10, y=10)

# creación canvas
c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="mistyrose2")
c.place(x=10, y=10)

#lineas divisorias
#linea1 = c.create_line(BASE/2,0, BASE/2, ALTURA, fill="red")
#linea2 = c.create_line(0,ALTURA/2, BASE, ALTURA/2, fill="red")

#cuadro 1

cuadro1 = c.create_polygon(BASE/2+10,ALTURA/2-40, BASE/2+10,ALTURA/2+10,BASE/2+60,ALTURA/2+10,BASE/2+60,ALTURA/2-40, outline="black",fill="gray")

#cuadro 2

cuadro2 = c.create_polygon(BASE/2+20,ALTURA/2-30, BASE/2+20,ALTURA/2+0,BASE/2+50,ALTURA/2+0,BASE/2+50,ALTURA/2-30,fill="gray65")

#rectangulo 1

rectangulo1 = c.create_polygon(BASE/2-40,ALTURA/2+10,BASE/2-40,ALTURA/2+60,BASE/2+70,ALTURA/2+60,BASE/2+70,ALTURA/2+10, outline="black",fill="gray")
rectangulo2 = c.create_polygon(BASE/2,ALTURA/2-50,BASE/2,ALTURA/2-40,BASE/2+70,ALTURA/2-40,BASE/2+70,ALTURA/2-50, outline="black",fill="gray32")
rectangulo3 = c.create_polygon(BASE/2+10,ALTURA/2-60,BASE/2+10,ALTURA/2-50,BASE/2+60,ALTURA/2-50,BASE/2+60,ALTURA/2-60, outline="black",fill="gray32")
rectangulo4 = c.create_polygon(BASE/2-30,ALTURA/2+10,BASE/2-10,ALTURA/2+10,BASE/2-10,ALTURA/2-30,BASE/2-30,ALTURA/2-30, outline="black",fill="gray32")
rectangulo5 = c.create_polygon(BASE/2-40,ALTURA/2-40,BASE/2-40,ALTURA/2-30,BASE/2,ALTURA/2-30,BASE/2,ALTURA/2-40, outline="black",fill="gray32")
frente1 = c.create_polygon(BASE/2-40,ALTURA/2+20,BASE/2-40,ALTURA/2+50,BASE/2-45,ALTURA/2+50,BASE/2-45,ALTURA/2+60,BASE/2-60,ALTURA/2+60,BASE/2-60,ALTURA/2+10,BASE/2-45,ALTURA/2+10,BASE/2-45,ALTURA/2+20, outline="black",fill="gray32")

#semi circulo 1

semi_circulo1 = c.create_arc(BASE/2-80,ALTURA/2+50,BASE/2-40,ALTURA/2+20, start=90, extent=180, outline="black",fill="gray32")

#ruedas

rueda1 = c.create_oval(BASE/2-40,ALTURA/2+50,BASE/2-10,ALTURA/2+80, outline="black",fill="gray32")

rueda2 = c.create_oval(BASE/2,ALTURA/2+50,BASE/2+30,ALTURA/2+80, outline="black",fill="gray32")

rueda3 = c.create_oval(BASE/2+70,ALTURA/2+50,BASE/2+40,ALTURA/2+80, outline="black",fill="gray32")

#cadena

cadena1 = c.create_polygon(BASE/2-10,ALTURA/2+60,BASE/2-10,ALTURA/2+70,BASE/2,ALTURA/2+70,BASE/2,ALTURA/2+60, fill="black")
cadena2 = c.create_polygon(BASE/2+30,ALTURA/2+60,BASE/2+30,ALTURA/2+70,BASE/2+40,ALTURA/2+70,BASE/2+40,ALTURA/2+60, fill="black")

#circulo cara

cara = c.create_oval(BASE/2+20,ALTURA/2-30,BASE/2+50,ALTURA/2, outline="black",fill="khaki1")

#ojos cara

ojo1 = c.create_oval(BASE/2+25,ALTURA/2-20,BASE/2+30,ALTURA/2-15, outline="white",fill="black")
ojo2 = c.create_oval(BASE/2+40,ALTURA/2-20,BASE/2+45,ALTURA/2-15, outline="white",fill="black")

#cejas cara

ceja1 = c.create_line(BASE/2+25,ALTURA/2-25,BASE/2+32,ALTURA/2-20, fill="black")
ceja2 = c.create_line(BASE/2+39,ALTURA/2-20,BASE/2+47,ALTURA/2-25, fill="black")

#boca cara

boca = c.create_oval(BASE/2+30,ALTURA/2-15,BASE/2+40,ALTURA/2-5, outline="white",fill="black")

#nombre tren

nombre = c.create_text(BASE/2+15,ALTURA/2+35, text="Adrián Forero", fill="black", font=("times new roman", 10))

#-----------------------
# frame controles
#-----------------------

frame_controles = Frame(ventana_principal, width=480, height=240)
frame_controles.config(bg="light slate blue", width=480, height=230)
frame_controles.place(x=10, y=260)

#boton salir
boton_salir = Button(frame_controles, text="Salir", command=ventana_principal.destroy)
boton_salir.place(x=220, y=110)









# desplegar ventana
ventana_principal.mainloop()