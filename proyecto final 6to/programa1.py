from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


def fun_menu():
    global menu
    menu = Tk()
    menu.title("Bienvenidos")
    menu.state('zoomed')
    menu.resizable(0, 0)
 #ancho, alto
    
    img_net1 = Image.open("Imagenes/inicial.png")

    resized = img_net1.resize((1500,800))
    img_net1 = ImageTk.PhotoImage(resized)

    label_imagen = Label(menu, image = img_net1, bg='black')
    label_imagen.pack()
    label_imagen.place(x=20, y=20)
    
    img_net2 = Image.open("Imagenes/uno.png")

    resized = img_net2.resize((180,700))
    img_net2 = ImageTk.PhotoImage(resized)

    label_imagen = Label(menu, image = img_net2, bg='#000000')
    label_imagen.pack()
    label_imagen.place(x=10, y=60)
    
    img_net3 = Image.open("Imagenes/a.png")

    resized = img_net3.resize((70,70))
    img_net3 = ImageTk.PhotoImage(resized)
    
    label_imagen = Label(menu, image = img_net3, bg='black')
    label_imagen.pack()
    label_imagen.place(x=54, y=140)
    
    img_net4 = Image.open("Imagenes/b.png")

    resized = img_net4.resize((70,70))
    img_net4 = ImageTk.PhotoImage(resized)
    
    label_imagen = Label(menu, image = img_net4, bg='black')
    label_imagen.pack()
    label_imagen.place(x=54, y=223)
    
    img_net5 = Image.open("Imagenes/c.png")

    resized = img_net5.resize((70,70))
    img_net5 = ImageTk.PhotoImage(resized)
    
    label_imagen = Label(menu, image = img_net5, bg='black')
    label_imagen.pack()
    label_imagen.place(x=54, y=323)
    

    img_net6 = Image.open("Imagenes/d.png")

    resized = img_net6.resize((70,70))
    img_net6 = ImageTk.PhotoImage(resized)
    
    label_imagen = Label(menu, image = img_net6, bg='black')
    label_imagen.pack()
    label_imagen.place(x=54, y=610)
    
    menu.configure(bg='black')

    
    mainloop()


def ir_l_m():
    menu.destroy()
    import login


def fun_secion():
    menu.destroy()
    import secion

def fun_login():
    menu.destroy()
    import login



fun_menu()
