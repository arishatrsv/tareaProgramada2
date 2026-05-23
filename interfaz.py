#Elaborado por: Arina Tarasova, Hilary Aguilar
#Fecha de creación: 12/05/2026 01:30 pm
#Última modificación:
#Versión: 3.14.3

from tkinter import *
from tkinter import ttk #Para combobox desplegable
from tkinter import messagebox #Permite mostrar ventanas emergentes
from funciones import *

#label: texto visual
#Toplevel: crea ventana secundaria
#font: tipo letra,tamaño
#.pack(): coloca el elemento en la ventana
#.grid(): para ordenar tipo tabla
#pady: agrega espacio vertical
#.get() obtiene lo que el usuario escribe
#command=, va sin paréntesis Ejecuta funciones cuando se presiona un botón:
#Entry: caja texto
#row: fila, column: columna
#padx: espacio horizontal, pady: espacio vertical
#values: definir lista de opciones
#Combobox: para lista desplegable
#StringVar: guarda el valor seleccionado
#sticky="w": Alinea a la izquierda

ventana = Tk() #Crea la ventana principal
ventana.title("Banco de Sangre") #Titulo de la ventana
ventana.geometry("800x600") #tamaño
titulo= Label(ventana,
            text="MENÚ PRINCIPAL",
            font=("Arial",20))
titulo.pack(pady=20) #Coloca el elemento en la ventana

def guardarDonador(ventanaInsertar,cedula,nombre,fecha,sangre,sexo,peso,telefono,correo):
    datosCedula=cedula.get() # .get() obtiene lo escrito por el usuario
    datosNombre=nombre.get()
    datosFecha=fecha.get()
    datosSangre=sangre.get()
    datosSexo=sexo.get()
    datosPeso=peso.get()
    datosTelefono=telefono.get()
    datosCorreo=correo.get()
    if validarCedula(datosCedula)==False:
        messagebox.showerror("Error","Cédula inválida")
        return
    # Valida fecha
    if validarFecha(datosFecha)==False:
        messagebox.showerror("Error","Fecha inválida")
        return
    # Valida peso
    if validarPeso(datosPeso)==False:
        messagebox.showerror("Error","Peso inválido")
        return
    # Valida teléfono
    if validarTelefono(datosTelefono)==False:
        messagebox.showerror("Error","Teléfono inválido")
        return
    # Valida correo
    if validarCorreo(datosCorreo)==False:
        messagebox.showerror("Error","Correo inválido")
        return
    justificacion = generarJustificacionRandom(datosFecha,datosPeso)
    estado = generarEstadoDonador(justificacion)
    datos = [
        datosNombre,
        datosCedula,
        datosSangre,
        datosSexo,
        datosFecha,
        datosPeso,
        datosCorreo,
        datosTelefono,
        estado,
        justificacion]
    matriz = cargarArchivo()
    inserto = insertarDonador(matriz,datos)
    if inserto:
        guardarArchivo(matriz)
        messagebox.showinfo("Éxito","Donador registrado correctamente")
        ventanaInsertar.destroy() #Cierra ventana
    else:
        messagebox.showerror("Error","La cédula ya existe")
    
def ventanaInsertar():
    ventanaInsertar= Toplevel()
    ventanaInsertar.title("Insertar Donador")
    ventanaInsertar.geometry("600x500")
    Label(ventanaInsertar,text="Cédula").grid(row=0,column=0,padx=10,pady=10)
    cedula= Entry(ventanaInsertar)
    cedula.grid(row=0,column=1)
    Label(ventanaInsertar,text="Nombre Completo").grid(row=1,column=0,padx=10,pady=10)
    nombre= Entry(ventanaInsertar)
    nombre.grid(row=1,column=1)
    Label(ventanaInsertar,text="Fecha Nacimiento").grid(row=2,column=0,padx=10,pady=10)
    fecha= Entry(ventanaInsertar)
    fecha.grid(row=2,column=1)
    Label(ventanaInsertar,text="Tipo de sangre").grid(row=3,column=0,padx=10,pady=10)
    sangre= ttk.Combobox(ventanaInsertar,values=mostrarTiposSangre())
    sangre.grid(row=3,column=1)
    Label(ventanaInsertar,text="Sexo").grid(row=4,column=0,padx=10,pady=10)
    sexo= StringVar()
    Radiobutton(ventanaInsertar,text="Masculino",variable=sexo,value="M").grid(
        row=4,column=1,sticky="w")
    Radiobutton(ventanaInsertar,text="Femenino",variable=sexo,value="F").grid(
        row=5,column=1,sticky="w")
    Label(ventanaInsertar,text="Peso").grid(row=6,column=0,padx=10,pady=10)
    peso= Entry(ventanaInsertar)
    peso.grid(row=6,column=1)
    Label(ventanaInsertar,text="Teléfono").grid(row=7,column=0,padx=10,pady=10)
    telefono= Entry(ventanaInsertar)
    telefono.grid(row=7,column=1)
    Label(ventanaInsertar,text="Correo").grid(row=8,column=0,padx=10,pady=10)
    correo= Entry(ventanaInsertar)
    correo.grid(row=8,column=1)
    Button(ventanaInsertar,text="Guardar", #crea un boton en la ventana incertar
        command=lambda: guardarDonador(   #dice que funcion ejecutar cuando hagan click
        ventanaInsertar,
        cedula,
        nombre,
        fecha,
        sangre,
        sexo,
        peso,
        telefono,
        correo)).grid(row=9,column=1,pady=20) #coloca el boton.
botonInsertar= Button(ventana,
                    text="Ingresar",
                    command=ventanaInsertar)
botonInsertar.pack()
ventana.mainloop() #Mantiene abierta la ventana

