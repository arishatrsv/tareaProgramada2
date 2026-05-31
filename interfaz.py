#Elaborado por: Arina Tarasova, Hilary Aguilar
#Fecha de creación: 12/05/2026 01:30 pm
#Última modificación:
#Versión: 3.14.3

from tkinter import *
from tkinter import ttk #Para combobox desplegable
from tkinter import messagebox #Permite mostrar ventanas emergentes(validaciones)
from funciones import *
from tareaP2 import*

#label: texto visual
#Toplevel: crea ventana secundaria
#font: tipo letra,tamaño
#.pack(): coloca el elemento en la ventana
#.grid(): para ordenar tipo tabla
#.get() obtiene lo que el usuario escribe
#command=, va sin paréntesis Ejecuta funciones cuando se presiona un botón:
#Entry: caja texto
#row: fila, column: columna
#padx: espacio horizontal
#pady: espacio vertical
#values: definir lista de opciones
#Combobox: para lista desplegable
#StringVar: guarda el valor seleccionado
#sticky="w": Alinea a la izquierda
#destroy: cierra una ventana
    
def ventanaInsertar(listaBotones):
    """
    Funcionamiento: Crea y muestra la ventana para insertar un nuevo donador.
    Entrada: listaBotones (list) lista de botones del menú principal para habilitarlos luego.
        Salida: Ventana con campos de entrada y botones: 'Registrar', 'Limpiar' y 'Regresar'.
    """
    ventanaInsertar= Toplevel()
    ventanaInsertar.title("Insertar Donador")
    ventanaInsertar.geometry("600x500")
    Label(ventanaInsertar,text="Cédula").grid(row=0,column=0,padx=15,pady=10,sticky="e")
    cedula= Entry(ventanaInsertar)
    cedula.grid(row=0,column=1)
    Label(ventanaInsertar,text="Nombre Completo").grid(row=1,column=0,padx=10,pady=10)
    nombre= Entry(ventanaInsertar)
    nombre.grid(row=1,column=1)
    Label(ventanaInsertar,text="Fecha Nacimiento").grid(row=2,column=0,padx=10,pady=10)
    fecha= Entry(ventanaInsertar)
    fecha.grid(row=2,column=1)
    Label(ventanaInsertar,text="Tipo de sangre").grid(row=3,column=0,padx=10,pady=10)
    sangre= ttk.Combobox(ventanaInsertar,values=mostrarTiposSangre(),state="readonly") #state: evita que escriban cualquier cosa
    sangre.grid(row=3,column=1)
    Label(ventanaInsertar,text="Sexo").grid(row=4,column=0,padx=10,pady=10)
    sexo= StringVar(value="M") #masculino aparece como default
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
    Button(ventanaInsertar,text="Registrar", #crea un boton en la ventana insertar
        command=lambda: registrarDonador(   #dice que funcion ejecutar cuando hagan click
        ventanaInsertar,cedula,nombre,fecha,sangre,sexo,peso,telefono,
        correo,listaBotones)).grid(row=9,column=1,pady=20) #coloca el boton.
    Button(ventanaInsertar,text="Limpiar", #crea un boton en la ventana insertar
        command=lambda: limpiarDonador(   #dice que funcion ejecutar cuando hagan click
        cedula,nombre,fecha,sangre,sexo,peso,telefono,
        correo)).grid(row=9,column=2,pady=20,padx=10) 
    Button(ventanaInsertar,text="Regresar", #crea un boton en la ventana insertar
        command=ventanaInsertar.destroy).grid(row=9,column=3,pady=20,padx=10)

def registrarDonador(ventanaInsertar,cedula,nombre,fecha,sangre,sexo,peso,telefono,correo,listaBotones):
    """
    Funcionamiento: Lee los datos del formulario de inserción y registra el donador.
    Entrada: objetos Entry/Combobox/StringVar del formulario y listaBotones (list).
        Salida: Muestra mensajes de error/éxito, abre la ventana de información del donador, habilita botones del menú y cierra la ventana de inserción.
    """
    datosCedula=cedula.get() # .get() obtiene lo escrito por el usuario
    datosNombre=nombre.get()
    datosFecha=fecha.get()
    datosSangre=sangre.get()
    datosSexo=sexo.get()
    datosPeso=peso.get()
    datosTelefono=telefono.get()
    datosCorreo=correo.get()
    matriz = cargarArchivo()
    resultado = insertarDonadorMostrar(matriz,datosCedula,datosNombre,datosFecha,datosSangre,
                                        datosSexo,datosPeso,datosTelefono,datosCorreo)
    if type(resultado)==str:
        messagebox.showerror("Error",resultado,parent=ventanaInsertar)
        return
    messagebox.showinfo("Éxito","Donador registrado correctamente",parent=ventanaInsertar)
    mostrarInformacionDonador(datosCedula,datosFecha,datosPeso,datosSangre)
    for boton in listaBotones:
        boton.config(state="normal")
    ventanaInsertar.destroy() #Cierra ventana

def mostrarInformacionDonador(datosCedula,datosFecha,datosPeso,datosSangre):
    """
    Funcionamiento: Muestra una ventana con información adicional del donador recién registrado.
    Entrada: datosCedula (str), datosFecha (str), datosPeso (str), datosSangre (str).
        Salida: Ventana con información textual y botón 'Regresar'.
    """
    ventanaInfo = Toplevel()
    ventanaInfo.title("Información del Donador")
    ventanaInfo.geometry("500x500")
    ventanaInfo.configure(bg="#FFF5F5")
    mensaje = ""
    mensaje += analizarEdadDonarAux(datosFecha)
    mensaje += "\n\n"
    #Lugar de donación
    mensaje += imprimirLugarNacimiento(datosCedula)
    mensaje += "\n"
    #Peso
    mensaje += validarPesoAux(datosPeso)
    mensaje += "\n\n"
    #Compatibilidad sangre
    mensaje += donarSangre(datosSangre)
    mensaje += "\n\n"
    #Video recomendado
    mensaje += recomendarVideo(datosSangre)
    Label(ventanaInfo,text=mensaje,justify="left",wraplength=650).pack(padx=20,pady=20)
    Button(ventanaInfo,text="Regresar",command=ventanaInfo.destroy).pack(pady=20)

def limpiarDonador(cedula,nombre,fecha,sangre,sexo,peso,telefono,correo):
    """
    Funcionamiento: Limpia los campos del formulario de inserción/actualización.
    Entrada: objetos Entry/Combobox/StringVar correspondientes a los campos del formulario.
        Salida: Los campos quedan vacíos y `sexo` se restablece a 'M'.
    """
    cedula.delete(0,END) #Borra todos los entry(0-> inicio y end -> final)
    nombre.delete(0,END)
    fecha.delete(0,END)
    sangre.set("")
    sexo.set("M")
    peso.delete(0,END)
    telefono.delete(0,END)
    correo.delete(0,END)
    
def ventanaGenerar(listaBotones):
    """
    Funcionamiento: Crea la ventana para especificar la cantidad de donadores a generar aleatoriamente.
    Entrada: listaBotones (list) lista de botones del menú principal para habilitarlos luego.
        Salida: Ventana con campo `Entry` para cantidad y botón 'Generar'.
    """
    ventanaGenerar = Toplevel()
    ventanaGenerar.title("Generar Donadores")
    ventanaGenerar.geometry("400x200")
    Label(ventanaGenerar,text="Cantidad de donadores:").pack(pady=15)
    cantidad = Entry(ventanaGenerar)
    cantidad.pack(pady=10)
    Button(ventanaGenerar,text="Generar",width=20,command=lambda:generarDonadores(ventanaGenerar,cantidad,listaBotones)).pack(pady=20)

def generarDonadores(ventanaGenerar,cantidad,listaBotones):
    """
    Funcionamiento: Valida la cantidad ingresada y genera donadores aleatorios.
    Entrada: ventanaGenerar (Tk window), cantidad (Entry), listaBotones (list).
    Salida: Muestra mensaje de resultado, habilita botones del menú y cierra la ventana al completar.
    """
    datosCantidad = cantidad.get()
    if datosCantidad.isdigit() == False:
        messagebox.showerror("Error","Debe ingresar únicamente números enteros positivos",parent=ventanaGenerar)
        return
    datosCantidad = int(datosCantidad)
    if datosCantidad <= 0:
        messagebox.showerror("Error","La cantidad debe ser mayor a 0",parent=ventanaGenerar)
        return
    matriz = cargarArchivo()
    mensaje = generarDonadoresAux(matriz,datosCantidad)
    messagebox.showinfo("Éxito",mensaje,parent=ventanaGenerar)
    for boton in listaBotones:
        boton.config(state="normal")
    ventanaGenerar.destroy()

def formularioActualizar(matriz,posicion):
    """
    Funcionamiento: Abre un formulario con los datos actuales de un donador para actualizar.
    Entrada: matriz (list) matriz de donadores, posicion (int) índice del donador en la matriz.
        Salida: Ventana con campos precargados y botones 'Actualizar' y 'Regresar'.
    """
    ventana = Toplevel()
    ventana.title("Actualizar Donador")
    ventana.geometry("600x500")
    #DATOS ACTUALES
    datos = matriz[posicion]
    Label(ventana,text="Cédula").grid(row=0,column=0,padx=15,pady=10)
    cedula = Entry(ventana,state="normal")
    cedula.grid(row=0,column=1)
    cedula.insert(0,datos[1])
    #bloquear cédula
    cedula.config(state="readonly")
    Label(ventana,text="Nombre").grid(row=1,column=0,padx=15,pady=10)
    nombre = Entry(ventana)
    nombre.grid(row=1,column=1)
    nombre.insert(0,datos[0])
    Label(ventana,text="Fecha").grid(row=2,column=0,padx=15,pady=10)
    fecha = Entry(ventana)
    fecha.grid(row=2,column=1)
    fecha.insert(0,datos[4])
    Label(ventana,text="Tipo Sangre").grid(row=3,column=0,padx=15,pady=10)
    sangre = ttk.Combobox(
        ventana,
        values=mostrarTiposSangre(),
        state="readonly")
    sangre.grid(row=3,column=1)
    sangre.set(datos[2])
    Label(ventana,text="Peso").grid(row=4,column=0,padx=15,pady=10)
    peso = Entry(ventana)
    peso.grid(row=4,column=1)
    peso.insert(0,datos[5])
    Label(ventana,text="Teléfono").grid(row=5,column=0,padx=15,pady=10)
    telefono = Entry(ventana)
    telefono.grid(row=5,column=1)
    telefono.insert(0,datos[7])
    Button(
        ventana,
        text="Actualizar",
        command=lambda: actualizarInterfaz(
            ventana,
            cedula,
            nombre,
            telefono,
            fecha,
            sangre,
            peso)
    ).grid(row=6,column=1,pady=20)
    Button(
        ventana,
        text="Regresar",
        command=ventana.destroy).grid(row=6,column=2,pady=20)

def ventanaActualizar():
    """
    Funcionamiento: Abre la ventana para solicitar cédula y buscar un donador a actualizar.
    Entrada: Ninguna.
        Salida: Ventana con campo cédula y botones 'Buscar' y 'Regresar'.
    """
    ventanaActualizar = Toplevel()
    ventanaActualizar.title("Actualizar Donador")
    ventanaActualizar.geometry("400x200")
    Label(ventanaActualizar,text="Digite la cédula:").pack(pady=15)
    cedula = Entry(ventanaActualizar,width=25)
    cedula.pack(pady=10)
    Button(
        ventanaActualizar,
        text="Buscar",
        command=lambda: buscarDonadorCedula(ventanaActualizar,cedula)
    ).pack(pady=20)
    Button(
        ventanaActualizar,
        text="Regresar",
        command=ventanaActualizar.destroy).pack()
    
def buscarDonadorCedula(pventana,pcedula):
    """
    Funcionamiento: Valida cédula, busca el donador en la matriz y abre el formulario de actualización.
    Entrada: pventana (Tk window) ventana actual, pcedula (Entry) con la cédula a buscar.
    Salida: Ninguna; muestra mensajes de error o abre `formularioActualizar`.
    """
    cedula = pcedula.get()
    if validarCedula(cedula)==False:
        messagebox.showerror("Error","Debe ingresar una cédula válida",parent=pventana)
        return
    matriz = cargarArchivo()
    posicion = buscarCedula(matriz,cedula)
    if posicion == -1:
        messagebox.showerror("Error","La persona con el número de cédula: "+ cedula +" no está registrado en la base de datos del Banco de Sangre aún.",
                            parent=pventana )
        return
    pventana.destroy()
    formularioActualizar(matriz,posicion)

def actualizarInterfaz(ventanaActualizar,
    cedula,
    nombre,
    telefono,
    fecha,
    sangre,
    peso):
    """
    Funcionamiento: Lee los campos del formulario de actualización y solicita guardar los cambios.
    Entrada: ventanaActualizar (Tk window), cedula,nombre,telefono,fecha,sangre,peso (Entry/Combobox).
    Salida: Ninguna; muestra mensaje de éxito o error y cierra la ventana si se actualiza.
    """
    matriz=cargarArchivo()
    resultado=actualizarDonadorMostrar(matriz,cedula.get(),nombre.get(),telefono.get(),fecha.get(),sangre.get(),peso.get())
    if resultado==True:
        messagebox.showinfo("Éxito","Datos actualizados correctamente",parent=ventanaActualizar)
        ventanaActualizar.destroy()
    else:
        messagebox.showerror("Error","Datos no actualizados",parent=ventanaActualizar)

def ventanaEliminar():
    """
    Funcionamiento: Crea la ventana para eliminar (marcar inactivo) un donador aportando una justificación.
    Entrada: Ninguna.
        Salida: Ventana con campo cédula, combobox de justificaciones y botones 'Eliminar' y 'Regresar'.
    """
    ventanaEliminar= Toplevel()
    ventanaEliminar.title("Eliminar Donador")
    ventanaEliminar.geometry("500x400")
    Label(ventanaEliminar,text="Cédula").pack(pady=10)
    cedula=Entry(ventanaEliminar,width=30)
    cedula.pack()
    Label(ventanaEliminar,text="Justificación").pack(pady=10)
    justificacion= StringVar()
    opciones=mostrarJustificacion()
    justificaciones= ttk.Combobox(ventanaEliminar,textvariable=justificacion,width=40,
                                state="readonly",values=list(opciones.values()))
    justificaciones.pack(pady=10)
    botones= Frame(ventanaEliminar) #Para poner los botones al lado uno del otro.
    botones.pack(pady=20)
    Button(botones,text="Eliminar",
        command=lambda:eliminarDonadores(ventanaEliminar,cedula,justificacion)).pack(side=LEFT,padx=10)
    Button(botones,text="Regresar",
        command=ventanaEliminar.destroy).pack(side=LEFT,padx=10)

def eliminarDonadores(pventanaEliminar,pcedula,pjustificacion):
    """
    Funcionamiento: Procesa la eliminación (marcar inactivo) de un donador tras confirmación.
    Entrada: pventanaEliminar (Tk window), pcedula (Entry), pjustificacion (StringVar/Combobox).
        Salida: Muestra mensajes de resultado, habilita botones del menú y cierra la ventana si se elimina.
    """
    matriz= cargarArchivo()
    cedula= pcedula.get()
    justificacionEliminar= pjustificacion.get()
    opciones= mostrarJustificacion()
    codigoJustificacion=""
    for codigo in opciones:
        if opciones[codigo] == justificacionEliminar:
            codigoJustificacion= codigo
    confirmar= messagebox.askyesno(
        "Confirmar eliminación", "¿Desea eliminar el donador?",parent=pventanaEliminar) #muestra ventana con dos botones Si y No
    resultado= eliminarDonadorMostrar(matriz,cedula,codigoJustificacion,confirmar)
    if resultado == "Donador eliminado satisfactoriamente.":
        messagebox.showinfo("Éxito",resultado,parent=pventanaEliminar)
        pventanaEliminar.destroy()
    else:
        messagebox.showerror("Resultado",resultado,parent=pventanaEliminar)

def ventanaInsertarLugar(lugaresDonar):
    """
    Funcionamiento: Muestra la ventana para insertar un nuevo lugar de donación en una provincia.
    Entrada: lugaresDonar (dict) diccionario global de lugares por provincia.
        Salida: Ventana con combobox de provincias, campo de texto para el lugar y botones 'Insertar' y 'Salir'.
    """
    ventanaLugar= Toplevel()
    ventanaLugar.title("Insertar Lugar de Donación")
    ventanaLugar.geometry("500x300")
    Label(ventanaLugar,text="Provincia").pack(pady=10)
    provincias=mostrarProvincias()
    provinciaElegida= StringVar()
    provincia= ttk.Combobox(ventanaLugar,textvariable=provinciaElegida,
                            state="readonly",width=35,values=list(provincias.values()))
    provincia.pack()
    Label(ventanaLugar,text="Nuevo Lugar").pack(pady=10)
    lugar= Text(ventanaLugar,width=40,height=3)
    lugar.pack()
    botones= Frame(ventanaLugar)
    botones.pack(pady=20)
    Button(botones,text="Insertar",
            command=lambda: insertarLugares(ventanaLugar,provinciaElegida,lugar)).pack(side=LEFT,padx=10)
    Button(botones,text="Salir",
            command=ventanaLugar.destroy).pack(side=LEFT,padx=10)

def insertarLugares(pventanaLugar,pprovincia,plugar):
    """
    Funcionamiento: Inserta un nuevo lugar en el diccionario de lugares según la provincia seleccionada.
    Entrada: pventanaLugar (Tk window), pprovincia (StringVar/Combobox), plugar (Text).
        Salida: Muestra mensaje de éxito o error mediante `messagebox`.
    """
    nomProvincia= pprovincia.get()
    lugar= plugar.get("1.0",END).strip()
    provincias= mostrarProvincias()
    codProvincia = ""
    for codigo in provincias:
        if provincias[codigo]== nomProvincia:
            codProvincia= codigo
    resultado= insertarLugarAux(lugaresDonar,codProvincia,lugar)
    if resultado== "Lugar agregado correctamente.":
        messagebox.showinfo("Éxito",resultado,parent=pventanaLugar)
        pventanaLugar.destroy()
    else:
        messagebox.showerror("Error",resultado,parent=pventanaLugar)

def reporteProvinciaInterfaz(pprovincia,pventana):
    """
    Funcionamiento: Llama la función que genera el reporte por provincia y muestra el resultado.
    Entrada: pprovincia (str) nombre de la provincia seleccionada.
    Salida: Muestra mensaje de éxito o error mediante `messagebox`.
    """
    resultado=opcionReporteProvincia(pprovincia)
    if resultado!=False:
        messagebox.showinfo("Éxito",resultado,parent=pventana)
        pventana.destroy()
    else:
        messagebox.showerror("Error","Reporte no creado.",parent=pventana)
    
def ventanaReporteProvincia():
    """
    Funcionamiento: Crea la ventana para seleccionar una provincia y generar su reporte.
    Entrada: Ninguna.
    Salida: Ventana con combobox de provincias y botones 'Generar Reporte' y 'Regresar'.
    """
    ventana = Toplevel()
    ventana.title("Reporte Donadores por Provincia")
    ventana.geometry("400x300")
    Label(ventana,text="Seleccione la provincia:").pack(pady=15)
    provincias = mostrarProvincias()
    comboProvincia = ttk.Combobox(
        ventana,
        values=list(provincias.values()),
        state="readonly",width=30)
    comboProvincia.pack(pady=10)
    Button(
        ventana,text="Generar Reporte",
        command=lambda: reporteProvinciaInterfaz(comboProvincia.get(),ventana)).pack(pady=15)
    Button(
        ventana,
        text="Regresar",
        command=ventana.destroy).pack(pady=10)

def reporteEdadInterfaz(pinicial,pfinal,pventana):
    """
    Funcionamiento: Solicita la generación de un reporte por rango de edad usando los valores de entrada.
    Entrada: pinicial (Entry), pfinal (Entry).
    Salida: Muestra mensaje de éxito o error mediante `messagebox`.
    """
    resultado = reporteRangoEdad(pinicial.get(),pfinal.get())
    if not resultado==False:
        messagebox.showinfo("Éxito",resultado,parent=pventana)
        pventana.destroy()
    else:
        messagebox.showerror("Error","Reporte no creado",parent=pventana)

def activarEdadFinal(pinicial,pfinal,pventana):
    """
    Funcionamiento: Valida la edad inicial y habilita el campo de edad final si es correcta.
    Entrada: pinicial (Entry) edad inicial, pfinal (Entry) campo a habilitar.
    Salida: bool True si habilita correctamente, False en caso de error.
    """
    try:
        edad = int(pinicial.get())
    except:
        messagebox.showerror("Error","Debe ingresar una edad válida",parent=pventana)
        return False
    if edad < 18 or edad > 65:
        messagebox.showerror(
            "Error","La edad inicial debe estar entre 18 y 65 años",parent=pventana)
        return False
    pfinal.config(state="normal")
    return True

def ventanaReporteEdad():
    """
    Funcionamiento: Crea la ventana para ingresar rango de edad y generar el reporte correspondiente.
    Entrada: Ninguna.
    Salida: Ventana con campos 'Edad inicial' y 'Edad final' y botones 'Validar edad inicial', 'Generar Reporte' y 'Regresar'.
    """
    ventana = Toplevel()
    ventana.title("Reporte por Rango de Edad")
    ventana.geometry("400x300")
    Label(ventana,text="Edad inicial:").pack(pady=10)
    entradaInicial = Entry(ventana)
    entradaInicial.pack()
    Label(ventana,text="Edad final:").pack(pady=10)
    entradaFinal = Entry(ventana,state="disabled")
    entradaFinal.pack()
    Button(ventana,text="Validar edad inicial",
    command=lambda: activarEdadFinal(entradaInicial,entradaFinal,ventana)).pack(pady=10)
    Button(ventana,text="Generar Reporte",command=lambda: reporteEdadInterfaz(
            entradaInicial,entradaFinal,ventana),).pack(pady=20)
    Button(ventana,text="Regresar",command=ventana.destroy).pack()

def ventanaListaCompleta():
    """
    Funcionamiento: Pide la generación del reporte de lista completa de donadores y muestra resultado.
    Entrada: Ninguna.
    Salida: Muestra mensaje de éxito o error mediante `messagebox`.
    """
    resultado= reporteListaDonadores()
    if resultado == "Reporte creado satisfactoriamente":
        messagebox.showinfo("Éxito",resultado)
    else:
        messagebox.showerror("Error",resultado)

def reporteTipoProvinciaInterfaz(psangre,pprovincia,pventana):
    """
    Funcionamiento: Solicita la generación del reporte por tipo de sangre y provincia.
    Entrada: psangre (str) tipo de sangre, pprovincia (int o str) provincia seleccionada.
    Salida: Muestra mensaje de éxito o error mediante `messagebox`.
    """
    resultado=reporteTipoProvincia(psangre,pprovincia)
    if resultado!=False:
        messagebox.showinfo("Éxito",resultado,parent=pventana)
        pventana.destroy()
    else:
        messagebox.showerror("Error","Reporte no creado.",parent=pventana)

def ventanaReporteSangreProvincia():
    """
    Funcionamiento: Muestra la ventana para seleccionar tipo de sangre y provincia y generar reporte.
    Entrada: Ninguna.
    Salida: Ventana con combobox para tipo de sangre y provincia y botones 'Generar Reporte' y 'Regresar'.
    """
    ventana=Toplevel()
    ventana.title("Tipo Sangre y Provincia")
    ventana.geometry("400x350")
    Label(ventana,text="Seleccione el tipo de sangre:").pack(pady=10)
    comboSangre=ttk.Combobox(ventana,values=mostrarTiposSangre(),state="readonly",width=30)
    comboSangre.pack(pady=10)
    Label(ventana,text="Seleccione la provincia:").pack(pady=10)
    provincias=mostrarProvincias()
    comboProvincia=ttk.Combobox(ventana,values=list(provincias.values()),state="readonly",width=30)
    comboProvincia.pack(pady=10)
    Button(ventana,text="Generar Reporte",command=lambda:
        reporteTipoProvinciaInterfaz(comboSangre.get(),comboProvincia.get(),ventana)).pack(pady=20)
    Button(ventana,text="Regresar",command=ventana.destroy).pack()

def reporteMujeresOInterfaz(pventana):
    """
    Funcionamiento: Llama la función que genera el reporte de mujeres O- y muestra el resultado.
    Entrada: Ninguna.
    Salida: Muestra mensaje de éxito o error mediante `messagebox`.
    """
    resultado=reporteMujeresO()
    if resultado!=False:
        messagebox.showinfo("Éxito",resultado,parent=pventana)
        pventana.destroy()
    else:
        messagebox.showerror("Error","Reporte no creado.",parent=pventana)

def ventanaMujeresO():
    """
    Funcionamiento: Crea la ventana para generar el reporte de mujeres O-.
    Entrada: Ninguna.
    Salida: Ventana con botones 'Generar Reporte' y 'Regresar'.
    """
    ventana=Toplevel()
    ventana.title("Reporte Mujeres O-")
    ventana.geometry("400x250")
    Label(ventana,
        text="Reporte Mujeres Donantes O-").pack(pady=20)
    Button(ventana,text="Generar Reporte",
        command=lambda:reporteMujeresOInterfaz(ventana)).pack(pady=20)
    Button(ventana,text="Regresar",
            command=ventana.destroy).pack(pady=10)

def reportePuedeDonar(psangre,pventana):
    """
    Funcionamiento: Genera el reporte de a quién puede donar el tipo de sangre seleccionado.
    Entrada: psangre (Combobox/Entry), pventana (Tk window) ventana que llamó la acción.
    Salida: Ninguna; muestra mensaje de éxito o error y cierra la ventana de selección.
    """
    tipo= psangre.get()
    resultado = reporteDonar(tipo)
    if resultado=="Reporte creado satisfactoriamente.":
        messagebox.showinfo("Éxito",resultado,parent=pventana)
        pventana.destroy()
    else:
        messagebox.showerror("Error",resultado,parent=pventana)

def ventanaPuedeDonar():
    """
    Funcionamiento: Muestra la ventana para seleccionar un tipo de sangre y generar el reporte correspondiente.
    Entrada: Ninguna.
    Salida: Ventana con combobox para tipo de sangre y botones 'Generar Reporte' y 'Regresar'.
    """
    ventana=Toplevel()
    ventana.title("¿A quién puede donar?")
    ventana.geometry("400x250")
    Label(ventana,text="Seleccione el tipo de sangre").pack(pady=20)
    sangre= ttk.Combobox(ventana,values=mostrarTiposSangre(),state="readonly")
    sangre.pack()
    Button(ventana,text="Generar Reporte",
            command=lambda: reportePuedeDonar(sangre,ventana)).pack(pady=20)
    Button(ventana,text="Regresar",
            command=ventana.destroy).pack()

def reporteRecibeInterfaz(psangre,pventana):
    """
    Funcionamiento: Genera el reporte de de quién puede recibir sangre el tipo indicado.
    Entrada: psangre (str) tipo de sangre.
    Salida: Muestra mensaje de éxito o error mediante `messagebox`.
    """
    resultado = reporteRecibeDe(psangre)
    if resultado != False:
        messagebox.showinfo("Éxito",resultado,parent=pventana)
        pventana.destroy()
    else:
        messagebox.showerror("Error","Reporte no creado.",parent=pventana)

def ventanaPuedeRecibir():
    """
    Funcionamiento: Crea la ventana para seleccionar tipo de sangre y generar el reporte de recepción.
    Entrada: Ninguna.
    Salida: Ventana con combobox para tipo de sangre and buttons 'Generar Reporte' and 'Regresar'.
    """
    ventana = Toplevel()
    ventana.title("¿De quién puede recibir?")
    ventana.geometry("400x300")
    Label(ventana,text="Seleccione el tipo de sangre:").pack(pady=15)
    comboSangre = ttk.Combobox(ventana,
        values=mostrarTiposSangre(),state="readonly",width=30)
    comboSangre.pack(pady=10)
    Button(ventana,text="Generar Reporte",
        command=lambda:reporteRecibeInterfaz(comboSangre.get(),ventana)).pack(pady=20)
    Button(ventana,text="Regresar",command=ventana.destroy).pack()

def reporteNoActivoInterfaz(pventana):
    """
    Funcionamiento: Solicita la generación del reporte de donadores no activos y muestra el resultado.
    Entrada: pventana (Tk window) ventana que llamó la acción.
    Salida: Muestra mensaje de éxito o error mediante `messagebox`; puede cerrar la ventana que llamó la acción.
    """
    resultado= reporteNoActivo()
    if resultado == "Reporte creado satisfactoriamente":
        messagebox.showinfo("Éxito",resultado,parent=pventana)
        pventana.destroy()
    else:
        messagebox.showerror("Error",resultado,parent=pventana)

def ventanaNoActivos():
    """
    Funcionamiento: Muestra la ventana para generar el reporte de donadores no activos.
    Entrada: Ninguna.
    Salida: Ventana con botones 'Generar Reporte' and 'Regresar'.
    """
    ventana = Toplevel()
    ventana.title("Donadores No Activos")
    ventana.geometry("400x300")
    Label(ventana,text="Generar reporte de donadores NO activos").pack(pady=30)
    Button(ventana,text="Generar Reporte",
            command=lambda:reporteNoActivoInterfaz(ventana)).pack(pady=20)
    Button(ventana,text="Regresar",
            command=ventana.destroy).pack()

def reporteLugaresInterfaz(pventana):
    """
    Funcionamiento: Llama la función que genera el reporte de lugares de donación y muestra el resultado.
    Entrada: pventana (Tk window) ventana que llamó la acción.
    Salida: Muestra mensaje de éxito o error mediante `messagebox`; cierra la ventana que llamó la acción si procede.
    """
    resultado=reporteLugares()
    if resultado == "Reporte creado satisfactoriamente.":
        messagebox.showinfo("Éxito",resultado,parent=pventana)
        pventana.destroy()
    else:
        messagebox.showerror("Error",resultado,parent=pventana)
        
def ventanaLugaresDonacion():
    """
    Funcionamiento: Crea la ventana para generar el reporte de lugares de donación.
    Entrada: Ninguna.
    Salida: Ventana con botones 'Generar Reporte' and 'Regresar'.
    """
    ventana = Toplevel()
    ventana.title("Lugares de Donación")
    ventana.geometry("400x300")
    Label(ventana,text="Generar reporte de lugares de donación").pack(pady=30)
    Button(ventana,text="Generar Reporte",
            command=lambda:reporteLugaresInterfaz(ventana)).pack(pady=20)
    Button(ventana,text="Regresar",
            command=ventana.destroy).pack()
    
def ventanaReportes():
    """
    Funcionamiento: Muestra el menú de reportes con botones para cada tipo de informe.
    Entrada: Ninguna.
        Salida: Ventana con botones para cada tipo de reporte y botón 'Regresar'.
    """
    ventana = Toplevel()
    ventana.title("Reportes")
    ventana.geometry("600x600")
    titulo=Label(
        ventana,
        text="REPORTES",
        font=("Arial",20,"bold"),
        fg="#8E1616")
    titulo.pack(pady=10)
    Button(
        ventana,text="Donadores por provincia",width=30, height=2,
        command=lambda: ventanaReporteProvincia()).pack(pady=5)
    Button(
        ventana,text="Por rango de edad",width=30,height=2,
        command=lambda: ventanaReporteEdad()).pack(pady=5)
    Button(
        ventana,text="Por tipo de sangre y provincia",width=30,height=2,
        command=lambda: ventanaReporteSangreProvincia()).pack(pady=5)
    Button(
        ventana,text="Lista completa de donadores",width=30,height=2,
        command=lambda: ventanaListaCompleta()).pack(pady=5)
    Button(
        ventana,text="Mujeres O-",width=30,height=2,
        command=lambda: ventanaMujeresO()).pack(pady=5)
    Button(
        ventana,text="¿A quién puede donar?",width=30,height=2,
        command=lambda: ventanaPuedeDonar()).pack(pady=5)
    Button(
        ventana,text="¿De quién puede recibir?",width=30,height=2,
        command=lambda: ventanaPuedeRecibir()).pack(pady=5)
    Button(
        ventana,text="Donadores no activos",width=30,height=2,
        command=lambda: ventanaNoActivos()).pack(pady=5)
    Button(
        ventana,text="Lugares de donación",width=30,height=2,
        command=lambda: ventanaLugaresDonacion()).pack(pady=5)
    Button(
        ventana,text="Regresar",width=20,height=2,
        command=ventana.destroy).pack(pady=20)

def salirSistema(pventana):
    """
    Funcionamiento: Muestra un mensaje de despedida y cierra la aplicación tras una pausa.
    Entrada: pventana (Tk window) ventana principal que se cerrará.
        Salida: Muestra mensaje de éxito o error; puede cerrar la ventana que llamó la acción.
    """
    ventanaSalir= Toplevel()
    ventanaSalir.title("Salir")
    ventanaSalir.geometry("500x150")
    ventanaSalir.configure(bg="white")
    Label(ventanaSalir, text="Donar Sangre, es donar vida",
        font=("Arial",18,"bold","italic"),fg="red",bg="white").pack(expand=True)
    ventanaSalir.after(2000,lambda:[ventanaSalir.destroy(),pventana.destroy()]) #2000= muestra el mensaje, espera 2 segundos y cierra el programa

def main():
    """
    Funcionamiento: Inicializa la ventana principal del sistema y coloca los botones del menú.
    Entrada: Ninguna.
    Salida: Inicia la interfaz gráfica y entra en el `mainloop` de Tkinter.
    """
    ventana=Tk()
    ventana.title("Banco de Sangre")
    ventana.geometry("800x500")
    titulo=Label(
        ventana,
        text="BANCO DE SANGRE",
        font=("Arial",24,"bold"),
        fg="#8E1616")
    titulo.pack(pady=20)
    botonInsertar = Button(ventana,text="Insertar Donador",width=25,height=2,command=lambda: ventanaInsertar(listaBotones))
    botonGenerar = Button(ventana,text="Generar Donadores",width=25,height=2,command=lambda: ventanaGenerar(listaBotones))
    botonActualizar = Button(ventana,text="Actualizar Donador",width=25,height=2,command=lambda: ventanaActualizar())
    botonEliminar = Button(ventana,text="Eliminar Donador",width=25,height=2,command=lambda: ventanaEliminar())
    botonLugar = Button(ventana,text="Insertar Lugar",width=25,height=2,command=lambda: ventanaInsertarLugar(lugaresDonar))
    botonReportes = Button(ventana,text="Reportes",width=25,height=2,command=lambda: ventanaReportes())
    botonSalir = Button(ventana,text="Salir",width=15,height=1,command=lambda: salirSistema(ventana))
    listaBotones = [botonActualizar,botonEliminar,botonReportes]
    #Coloca los botones en la ventana
    botonInsertar.pack(pady=5)
    botonGenerar.pack(pady=5)
    botonActualizar.pack(pady=5)
    botonEliminar.pack(pady=5)
    botonLugar.pack(pady=5)
    botonReportes.pack(pady=5)
    botonSalir.pack(pady=5)
    matriz = cargarArchivo()
    #Si NO hay donadores guardados
    if matriz == []:
        #Desactiva actualizar
        botonActualizar.config(state="disabled")
        botonEliminar.config(state="disabled")
        botonReportes.config(state="disabled")
    ventana.mainloop() #Mantiene abierta la ventana

main()