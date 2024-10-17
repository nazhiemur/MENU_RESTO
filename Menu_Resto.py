import tkinter as tk
from tkinter import messagebox, PhotoImage
from lista_comidas import *

# Crea ventana login
ventana_login = tk.Tk()
ventana_login.title("Login")
ventana_login.geometry("400x200")
ventana_login.config(bg="lemon chiffon")


    #crea input y nombre de usuario
nombre = tk.Label(ventana_login, text= "Usuario",bg="lemon chiffon", font=("Arial", 10))
nombre.pack()
ingresa_usuario = tk.Entry(ventana_login, bg="khaki")
ingresa_usuario.pack()

    #crea input y clave
clave = tk.Label(ventana_login, text= "Clave", bg="lemon chiffon", font=("Arial", 10))
clave.pack()
ingresa_clave = tk.Entry(ventana_login,bg="khaki", show="*")
ingresa_clave.pack()


def ingresar():
    usuario_input = ingresa_usuario.get()
    clave_input = ingresa_clave.get()

    acceso = False

    for usuario in lista_usuarios:

        if usuario["nombre"] == usuario_input and usuario["clave"]== clave_input:
            acceso = True

    if acceso:
        ventana = tk.Tk()
        ventana.title("COMILANDIA")
        # ventana.iconbitmap("comil.ico")
        ventana.geometry("650x450")
        ventana.config(bg="LightGreen")
        tk.Label(ventana,text= "BIENVENIDOS MENU RESTO🍕🍔", font='skia 20 bold').grid(padx=95 , pady= 175)
        
        # VENTANAS DE LOS MENUS--- COLORES DISEÑO
        def items_lista(ventana, lista_comida):

            for item in lista_comida:
                tk.Label(ventana,text= f'{item["nombre"]} --- {item["tipo"]} --- $ {item["precio"]}', font='skia 10 bold').grid(padx=50 , pady= 10)


        def entrada():
            ventanita = tk.Tk()
            ventanita.title("Entradas")
            ventanita.geometry("400x450")
            ventanita.config(bg="LightGreen")
            items_lista(ventanita, menu_entrada)
            ventanita.pack()


        def plato():
            ventanita = tk.Tk()
            ventanita.title("PlatoPrincipal")
            ventanita.geometry("650x400")
            ventanita.config(bg="LightGreen")
            items_lista(ventanita, menu_comida)
            ventanita.pack()


        def bebidas():
            ventanita = tk.Tk()
            ventanita.title("Bebidas")
            ventanita.geometry("650x275")
            ventanita.config(bg="LightGreen")
            items_lista(ventanita, menu_bebida)
            ventanita.pack()

        def postre():
            ventanita = tk.Tk()
            ventanita.title("Postre")
            ventanita.geometry("350x300")
            ventanita.config(bg="LightGreen")
            items_lista(ventanita, menu_postre)
            ventanita.pack()




        menu = tk.Menu(ventana)
        ventana.config(menu=menu)

        # menu_entrada = tk.Menu(menu)
        # menu_plato = tk.Menu(menu)
        # menu_bebidas = tk.Menu(menu)
        # menu_postre = tk.Menu(menu)


        #CASCADA BEBIDA / ENTRADA / PLATO PRINCIPAL / POSTRE

        menu.add_cascade(label ='Entradas', font=("Arial", 8), command=entrada)
        menu.add_cascade(label ='Plato Principal', font=("Arial", 8), command=plato)
        menu.add_cascade(label ='Bebidas', font=("Arial", 8), command=bebidas)
        menu.add_cascade(label ='Postre', font=("Arial", 8), command=postre)  #menu=menu_postre
        # menu.add_cascade(label ='Reservas', font=("Arial", 8), menu=reserva)

        # menu_bebidas.add_command(label = "Con Alcohol", font=("Times", 8), command=bebidas)
        # menu_bebidas.add_command(label = "Sin Alcohol", font=("Times", 8), command=bebidas)

        # menu_entrada.add_command(label = "Menu Niños", font=("Arial", 8), command=entrada)
        # menu_entrada.add_command(label = "Todo", font=("Arial", 8), command=entrada)

        # menu_plato.add_command(label = "Platos Tradicionales", font=("Arial", 8), command=plato)
        # menu_plato.add_command(label = "Platos Gourmet", font=("Arial", 8), command=plato)
        # menu_plato.add_command(label = "Platos Veganos", font=("Arial", 8), command=plato)

        # menu_postre.add_command(label = "Postres Frios", font=("Arial", 8), command=postre)
        # menu_postre.add_command(label = "Postres Calientes", font=("Arial", 8), command=postre)

    else:
        messagebox.showerror("Error", "Tenes que registrarte!")

    ventana.mainloop()


lista_usuarios = [{"nombre": "a", "clave": "a"}]

def registro():
    ventana_registro = tk.Tk()
    ventana_registro.title("Nuevo Registro")
    ventana_registro.geometry("400x300")
    ventana_registro.config(bg="lemon chiffon")


    #INGRESA NOMBRE
    nombre = tk.Label(ventana_registro, bg="lemon chiffon", text= "Nombre ", font=("Arial", 10))
    nombre.pack()
    ingresa_nombre = tk.Entry(ventana_registro, bg="khaki")
    ingresa_nombre.pack()

    # INGRESA TELEFONO
    telefono = tk.Label(ventana_registro,bg="lemon chiffon", text= "Telefono ", font=("Arial", 10))
    telefono.pack()
    ingresa_telefono = tk.Entry(ventana_registro, bg="khaki")
    ingresa_telefono.pack()

    # INGRESA DIRECCION
    direccion = tk.Label(ventana_registro,bg="lemon chiffon", text= "Dirección ", font=("Arial", 10))
    direccion.pack()
    ingresa_direccion = tk.Entry(ventana_registro, bg="khaki")
    ingresa_direccion.pack()

    # INGRESA CLAVE
    clave = tk.Label(ventana_registro,bg="lemon chiffon", text= "Clave Nueva ", font=("Arial", 10))
    clave.pack()
    #clave = str()
    ingresa_clave = tk.Entry(ventana_registro, bg="khaki", show="*")
    ingresa_clave.pack()

    # REPETIR CLAVE
    rep_clave = tk.Label(ventana_registro, bg="lemon chiffon", text= "Repetir Clave ", font=("Arial", 10))
    rep_clave.pack()
    repetir_clave = tk.Entry(ventana_registro, bg="khaki", show="*")
    repetir_clave.pack()


    def guardar():
       nombre = ingresa_nombre.get()
       telefono = ingresa_telefono.get()
       direccion = ingresa_direccion.get()
       clave = ingresa_clave.get()
       rep_clave =  repetir_clave.get()

       if nombre and telefono and direccion and clave and rep_clave:
            datos_registro = {"nombre": nombre,
                     "telefono": telefono,
                     "direccion": direccion,
                     "clave": clave,
                     "repetir_clave": rep_clave}

            print(datos_registro)
            
            if clave == rep_clave:
                lista_usuarios.append(datos_registro)

                messagebox.showinfo("Gracias!", "Los datos fueron guardados correctamente")
                ventana_registro.destroy()
            else:
                messagebox.showerror("Error", "La clave no coincide")
       else:
            messagebox.showerror("Error", "Ingrese todos los campos")



    boton_guardar = tk.Button(ventana_registro, bg="lemon chiffon", text='Guardar', command=guardar)
    boton_guardar.pack()



boton_ingresar = tk.Button(ventana_login, bg="lemon chiffon", text='Ingresar', command=ingresar)
boton_ingresar.pack()


boton_registro = tk.Button(ventana_login, bg="lemon chiffon", text='Registrate', command=registro)
boton_registro.pack()

ventana_login.mainloop()