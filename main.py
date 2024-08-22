import tkinter as tk  # importamos tkinter

# con estas lineas modificaamos la apariencia fisica de la ventana
ventana = tk.Tk()
ventana.geometry("500x250+500+250")
ventana.resizable(False, False)
ventana.title("Entra Y sale Texto")
ventana.iconbitmap("zero_two.ico")

# declaramos una variable con la propiedad de stringvar

Entrada_de_texto = tk.StringVar()

# declaramos la funcion que vamos a utilizar despues


def texto():
    try:  # utilizamos el try ya que con este podemos manejar las expeciones
        # con el .get hacemos que la variable texto adquiera los valores de la otra variable
        texto = float(Entrada_de_texto.get())
        # aunque se usa despues, con esto hacemos que el texto que se vea en label que quiera sea igual al texto
        label.config(text=texto)

    except ValueError:  # excepcion ya que queremos que solo esten numeros
        label.config(text="SOLO NUMEROS!!!!")


# colocamos el recuadro de entrada de datos el cual al escribir se guardara en la variable entrada_texto
Entrada = tk.Entry(ventana, textvariable=Entrada_de_texto)
Entrada.pack()

# colocamos el boton que va ajecutar la funcion que antes declaramos
boton = tk.Button(ventana, text="Presiona", command=texto)
boton.pack()

# con esto creamos el apartado donde se vera el resultado que queremos, le asignamos un valor de 0 que sera modificado por lo puesto dentro de la funcion
label = tk.Label(ventana, text="")
label.pack()


ventana.mainloop()
