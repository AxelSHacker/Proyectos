from tkinter import *

#iniciar tkinter
gestor = Tk()

#tamanio ventana
gestor.wm_geometry("1020x630+0+0")

#titulo de la ventana
gestor.title("Venta Manolo")

#color de fondo de la ventana
gestor.config(bg="black")


def codigo_para_el_menu():

#panel del menu
    panel_menu = Frame(gestor, bd=1, relief=FLAT)
#esto es para llamar al cuadrado
    panel_menu.pack(side=LEFT)

#panel de las diferentes comidas
    panel_comidas = LabelFrame(panel_menu, text="Comida", font=("Dosis", 19, "bold"),
                               bd=1, relief=FLAT, fg="azure4")
#ubicacion del labelframe dentro del Frame
    panel_comidas.pack(side=LEFT)

#panel para las diferentes bebidas
    panel_bebidas = LabelFrame(panel_menu, text="Bebidas", font=("Dosis", 19, "bold"),
                               bd=1, relief=FLAT, fg="azure4")
#ubicacion del labelframe dentro del Frame
    panel_bebidas.pack(side=LEFT)

#panel de los diferentes postres
    panel_postres = LabelFrame(panel_menu, text="Postres", font=("Dosis", 19, "bold"),
                               bd=1, relief=FLAT, fg="azure4")
#ubicacion del labelframe dentro del Frame
    panel_postres.pack(side=LEFT)

#menus
    menu_de_comida = ["Hamburguesa de tofu", "Hummus", "Sushi"]
    menu_de_bebidas = ["Cerveza", "Coca-Cola", "Vino"]
    menu_de_postres = ["Tiramisu", "Helado", "Cafe"]
    variables_comida = []
    cuadros_comida = []
    texto_comida = []
    contador = 0
#loop para crear check buton y funcion del menu
    for comida in menu_de_comida:
        #crear los creck button
        variables_comida.append("")
        variables_comida[contador] = IntVar()
        comida = Checkbutton(panel_comidas,
                             text=comida.title(),
                             font=("Dosis", 19, "bold"),
                             onvalue=1,
                             offvalue=0,
                             variable=variables_comida[contador],
                             command=revisar_check)
        comida.grid(row=contador, column=0, sticky=W)
        #crear cuadros de entrada
        cuadros_comida.append("")
        texto_comida.append("")
        texto_comida[contador] = StringVar()
        texto_comida[contador].set("0")
        cuadros_comida[contador]= Entry(panel_comidas,
                                        font=("Dosis", 18, "bold"),
                                        bd=1,
                                        width=6,
                                        state=DISABLED,
                                        textvariable=texto_comida[contador])
        cuadros_comida[contador].grid(row=contador,
                                      column=1)

        contador += 1

    variables_bebidas = []
    cuadros_bebida = []
    texto_bebida = []
    contador = 0
    for bebidas in menu_de_bebidas:
        variables_bebidas.append("")
        variables_bebidas[contador] = IntVar()
        bebidas = Checkbutton(panel_bebidas,
                              text=bebidas.title(),
                              font=("Dosis", 19, "bold"),
                              onvalue=1,
                              offvalue=0,
                              variable=variables_bebidas[contador],
                              command=revisar_check)
        bebidas.grid(row=contador, column=0, sticky=W)
        cuadros_bebida.append("")
        texto_bebida.append("")
        texto_bebida[contador] = StringVar()
        texto_bebida[contador].set("0")
        cuadros_bebida[contador] = Entry(panel_bebidas,
                                         font=("Dosis", 18, "bold"),
                                         bd=1,
                                         width=6,
                                         state=DISABLED,
                                         textvariable=texto_bebida[contador])
        cuadros_bebida[contador].grid(row=contador,
                                      column=1)
        contador += 1

    variables_postres = []
    cuadros_postres = []
    texto_postres = []
    contador = 0
    for postres in menu_de_postres:
        variables_postres.append("")
        variables_postres[contador] = IntVar()
        postres = Checkbutton(panel_postres,
                              text=postres.title(),
                              font=("Dosis", 19, "bold"),
                              onvalue=1,
                              offvalue=0,
                              variable=variables_postres[contador],
                              command=revisar_check)
        postres.grid(row=contador, column=0, sticky=W)
        cuadros_postres.append("")
        texto_postres.append("")
        texto_postres[contador] = StringVar()
        texto_postres[contador].set("0")
        cuadros_postres[contador] = Entry(panel_postres,
                                         font=("Dosis", 18, "bold"),
                                         bd=1,
                                         width=6,
                                         state=DISABLED,
                                         textvariable=texto_postres[contador])
        cuadros_postres[contador].grid(row=contador,
                                      column=1)
        contador += 1

    #revisar check button

    def revisar_check():
        x = 0
        for c in cuadros_comida:
            if variables_comida[x].get() == 1:
                cuadros_comida[x].config(state=NORMAL)


    mesa_1 ["state"] = DISABLED




#botones
mesa_1 = Button(gestor, text="Mesa 1", bg="red", command=codigo_para_el_menu)
mesa_1.place(width=50, height=50)










#Evitar que se cierre la aplicacion
gestor.mainloop()
