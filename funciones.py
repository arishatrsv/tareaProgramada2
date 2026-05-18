#Elaborado por: Arina Tarasova, Hilary Aguilar
#Fecha de creación: 12/05/2026 01:30 pm
#Última modificación:
#Versión: 3.14.3

#Importación de librerias
import pickle
import re
from datetime import datetime
import random

def mostrarTiposSangre():
    tipos = ("O+","O-","A+","A-","B+","B-","AB+","AB-")
    return tipos

def mostrarProvincias():
    provincias= {
    1: "San José",
    2: "Alajuela",
    3: "Cartago",
    4: "Heredia",
    5: "Guanacaste",
    6: "Puntarenas",
    7: "Limon"}
    return provincias

def crearDiccionarioLugares():
    diccionarioLugares = {
    1:["Banco Nacional de Sangre",
        "Hospital México",
        "Hospital San Juan de Dios"],
    2:["Hospital San Rafael de Alajuela",
        "Hospital de San Ramón",
        "Hospital del Cantón Norteño"],
    3:["Hospital Max Peralta"],
    4:["Hospital San Vicente de Paúl"],
    5:["Hospital La Anexión en Nicoya",
        "Hospital Enrique Baltodano de Liberia"],
    6:["Hospital Monseñor Sanabria"],
    7:["Hospital Tony Facio",
        "Hospital de Guápiles"]}
    return diccionarioLugares

def guardarArchivo(pmatrizD):
    archivo=open("donadores.txt","wb")
    pickle.dump(pmatrizD,archivo)
    archivo.close()
    return 

def cargarArchivo():
    try:
        archivo=open("donadores.txt","rb")
        matriz=pickle.load(archivo)
        archivo.close()
        return matriz
    except:
        return []

def buscarCedula(pmatrizD,pcedula):
    for i in range(len(pmatrizD)):
        if pmatrizD[i][1]==pcedula:
            return i
    return -1
    
def obtenerProvincias(pcedula):
    provincia = int(pcedula[0])
    return provincia

def insertarDonador(pmatrizD,pdatos):
    cedula = pdatos[1]
    existe = buscarCedula(pmatrizD,cedula)
    if existe != -1:
        return False
    pmatrizD.append(pdatos)
    return True

def validarCedula(pcedula):
    if re.match(r"^[1-8]-\d{4}-\d{4}$",pcedula): #Valida que el formato de cedula sea #-####-#### 
        return True
    return False

def validarFecha(pfecha):
    try:
        fecha=datetime.strptime(pfecha,"%d/%m/%Y") #Verifica que el str es una fecha con el formato correcto
        return fecha
    except:
        return False

def validarCorreo(pcorreo):
    #Verifica que el correo cumpla con alguno de los formatos permitidos
    if re.match(r"^[\w.%+-]+@(gmail\.com|costarricense\.cr|racsa\.go\.cr|ccss\.sa\.cr)$",pcorreo):
        return True
    return False

def validarTelefono(ptelefono):
    if re.match(r"^[246789]{1}\d{3}-\d{4}$",ptelefono):
        return True
    else:
        return False
    
def validarPeso(ppeso):
    if ppeso.isdigit()==False:
        return False
    peso = int(ppeso) 
    if peso > 50 and peso < 120:
        return True
    return False

def analizarEdadDonar(pfecha):
    fechaNacimiento = validarFecha(pfecha)
    if fechaNacimiento==False:
        return False
    anno= fechaNacimiento.year
    mes= fechaNacimiento.month
    dia= fechaNacimiento.day
    hoy= datetime.now()
    annoAct= hoy.year
    mesAct= hoy.month
    diaAct= hoy.day
    edad= annoAct - anno
    if((mesAct,diaAct)<(mes,dia)):
        edad -= 1
    return edad >= 18

def mostrarCompatibilidad():
    compatibilidad = {
        "O-":[
            "O-","O+",
            "A-","A+",
            "B-","B+",
            "AB-","AB+"],
        "O+":[
            "O+","A+",
            "B+","AB+"],
        "A-":[
            "A-","A+",
            "AB-","AB+"],
        "A+":[
            "A+","AB+"],
        "B-":[
            "B-","B+",
            "AB-","AB+"],
        "B+":[
            "B+","AB+"],
        "AB-":[
            "AB-","AB+"],
        "AB+":["AB+"]}
    return compatibilidad

def mostrarInfoSangre():
    informacion={
        "A+": "Se le recomienda que done sangre entera y plaquetas.",
        "A-": "Se le recomienda que done sangre entera y glóbulos rojos dobles.",
        "B+": "Se le recomienda que done sangre entera y glóbulos rojos dobles.",
        "B-": "Se le recomienda que done sangre entera o plaquetas.",
        "O+": "Se le recomienda que done sangre entera y glóbulos rojos dobles.",
        "O-": "Se le recomienda que done sangre entera y glóbulos rojos dobles.",
        "AB+":"Se le recomienda donar plaquetas y plasma.",
        "AB-":"Se le recomienda donar plaquetas y plasma."}
    return informacion

def actualizarDonador(pmatrizD,pposicion,pdatos):
    pmatrizD[pposicion][0]=pdatos[0] #nombre
    pmatrizD[pposicion][7]=pdatos[1] #telefono
    pmatrizD[pposicion][4]=pdatos[2] #fecha
    pmatrizD[pposicion][2]=pdatos[3] #sangre
    pmatrizD[pposicion][5]=pdatos[4] #peso
    justificacion=generarJustificacionRandom(pdatos[2],pdatos[4])
    estado=generarEstadoDonador(justificacion)
    pmatrizD[pposicion][8]=estado
    pmatrizD[pposicion][9]=justificacion
    return pmatrizD

def generarCedulaRandom():
    provincia=str(random.randint(1,8)) #Genera un número de provincia entre 1 y 8
    tomo=random.randint(1000,9999) #Genera 4 números aleatorios para el tomo
    asiento=random.randint(1000,9999) #Genera 4 números aleatorios para el asiento
    cedula=f"{provincia}-{tomo}-{asiento}" #Construye la cédula con formato #-####-####
    return cedula

def generarNombreRandom():
    nombres=["Víctor","Augusto","Ana","Hilary","Kaleb","María","Luis","Carlos","María","Elena","Sofía","Daniel","Andrés"]
    apellidos=["Torrealba","Porras","Ramírez","Gómez","Vargas","Solano","Rojas","Castro"] #listas de nombres y apellidos para usar en la generacion
    nombre=random.choice(nombres) #.choice elige un elemento al azar de la lista
    apellido=random.choice(apellidos)
    return nombre+" "+apellido #construye el nombre completo

def generarTipoSangreRandom():
    tipos=mostrarTiposSangre()
    return random.choice(tipos)

def generarSexoRandom():
    sexos=["M","F"]
    return random.choice(sexos)

def generarPesoRandom():
    return str(random.randint(30,150))

def generarTelefonoRandom():
    primerNumero=random.choice(["2","4","6","7","8","9"])
    resto=str(random.randint(1000000,9999999)) #str para poder separarlo despues
    telefono=primerNumero+resto[:3]+"-"+resto[3:] #Genera un número de teléfono con formato ####-####
    return telefono

def generarCorreoRandom(pnombre):
    usuario=pnombre.lower().replace(" ","") #quita espacios y lo pone en minuscula
    terminaciones=["@costarricense.cr","@racsa.go.cr","@ccss.sa.cr","@gmail.com"]
    terminacion=random.choice(terminaciones) #elige la terminacion al azar
    numero=random.randint(1,99) #agrega un numero para evitar correos repetidos
    correo=usuario+str(numero)+terminacion 
    return correo

def generarFechaRandom():
    anno=random.randint(1926,2015) #genera un año entre 1926 y 2015
    mes=random.randint(1,12)
    if mes==2: #febrero, max dias=28
        dia=random.randint(1,28)
    elif mes in [4,6,9,11]: #tienen 30 dias
        dia=random.randint(1,30)
    else: #31 dias
        dia=random.randint(1,31)
    fecha=f"{dia:02d}/{mes:02d}/{anno}"
    #:02d: formato de fecha
        #d-numero entero digit
        #02-que ocupe 2 espacios, y si falta un espacio lo rellene con 0
    return fecha

def generarJustificacionRandom(pfecha,ppeso):
    if analizarEdadDonar(pfecha)==False:
        return 1
    if int(ppeso)<50:
        return 2
    if int(ppeso)>120:
        return 3
    otrasJustificaciones=[0,4,5,6,7]
    return random.choice(otrasJustificaciones)

def generarEstadoDonador(pjustificacion):
    if pjustificacion == 0:
        return "Apto"
    return "No apto"

def mostrarJustificacion(pnumero):
    justificaciones={
        0:"Apto para donar",
        1:"Menor de edad",
        2:"Peso menor a 50 kg",
        3:"Peso mayor a 120 kg",
        4:"Enfermedad infecciosa o crónica",
        5:"Uso de medicamentos no permitidos",
        6:"Procedimiento médico reciente",
        7:"Viaje o conducta de riesgo"}
    return justificaciones[pnumero]

def generarDonadorRandom():
    cedula=generarCedulaRandom()
    nombre=generarNombreRandom()
    fecha=generarFechaRandom()
    sangre=generarTipoSangreRandom()
    sexo=generarSexoRandom()
    peso=generarPesoRandom()
    telefono=generarTelefonoRandom()
    correo=generarCorreoRandom(nombre)
    justificacion=generarJustificacionRandom(fecha,peso)
    estado=generarEstadoDonador(justificacion)
    return [nombre,cedula,sangre,sexo,fecha,peso,correo,telefono,estado,justificacion]

def crearInicioHtml(ptitulo):
    fecha=datetime.now()
    html="<html>" #Comienza el documento HTML
    html+="<head>"
    html+="<title>"+ptitulo+"</title>" #Coloca el título de la página,aparece en la pestaña del navegador
    #"""style""" abre una seccion de estilos para modificar la apariencia visual
    #collapse une los bordes de la tabla
    #width define el ancho de la tabla
    #1px es el grosor del borde
    #solid significa línea continua
    #padding agrega espacio interno
    #text-align alinea el texto
    #background-color cambia el color del fondo
    html+="""<style> 
    table{border-collapse: collapse;width: 70%;} 
    th, td{border: 1px solid black; padding: 8px; text-align: left;}
    th{background-color: lightgray;}
    </style>""" #cierra la ceccion de estilos.
    html+="</head>" 
    html+="<body>" #Todo lo visible va dentro del body
    html+="<h1>"+ptitulo+"</h1>" #Agrega un título grande visible en la página
    html+="<p>"+str(fecha.strftime("%d/%m/%Y %H:%M"))+"</p>" #Agrega la fecha y hora del sistema, <p> es un parrafo
    return html #Retorna el html creado hasta el momento

def cerrarHtml():
    return "</body></html>" #cierra el body y el html, para no repetirlo en cada funcion

def guardarHtml(pnombreArchivo,phtml):
    archivo=open(pnombreArchivo,"w")
    archivo.write(phtml) #Escribe todo el html dentro del archivo
    archivo.close()
    return True

def generarReporteLugaresDonacion(pmatrizD):
    html=crearInicioHtml("Reporte Lugares de Donación")
    html+="<table border='1'>" #Crea una tabla con bordes visibles
    html+="<tr>" #Abre la fila de encabezados 
    html+="<th>Provincia</th>"  #Agrega los títulos de las columnas, th significa table header
    html+="<th>Cantidad Donadores</th>"
    html+="<th>Recintos</th>"
    html+="</tr>" #Cierra la fila de encabezados
    provincias=mostrarProvincias()
    lugares=crearDiccionarioLugares()
    for provincia in provincias: #Recorre cada provincia
        cantidad=0 #contador de donadores por provincia
        for donador in pmatrizD: #recorre todos los donadores de la matriz
            if obtenerProvincias(donador[1])==provincia: #Obtiene la provincia de la cédula y la compara con la del ciclo
                cantidad+=1 #suma un donador a la provincia
        textoLugares="" #guarda lugares
        for lugar in lugares[provincia]: #recorre los lugares de la provincia
            textoLugares+=lugar+"<br>" #<br> para salto de linea en html(break line)
        html+="<tr>" #abre una nueva fila para cada provincia
        html+="<td>"+provincias[provincia]+"</td>" #Agrega el nombre de la provincia. (tb-table data)
        html+="<td>"+str(cantidad)+"</td>" #Agrefa la cantidad de donadores
        html+="<td>"+textoLugares+"</td>" #Agrega los lugares de donacion con saltos de linea
        html+="</tr>" #cierra la fila de provincia
        #aqui se repite el ciclo para cada provincia creando una fila nueva
    html+="</table>" #cierra la tabla
    html+=cerrarHtml() 
    return guardarHtml("reporteLugares.html",html)

def generarReporteDonadoresProvincia(pmatrizD,pprovincia):
    html=crearInicioHtml("Reporte Donadores por Provincia")
    html+="<table border='1'>"
    html+="<tr>" #abre la fila de encabezados
    html+="<th>Cédula</th>" #agrega los titulod de las columnas
    html+="<th>Nombre</th>"
    html+="<th>Fecha Nacimiento</th>"
    html+="<th>Teléfono</th>"
    html+="<th>Correo</th>"
    html+="</tr>" #cierra la fila de encabezados
    listaOrdenada=pmatrizD[:] #crea una copia indepediente de la matriz sin modificar el orden original
    listaOrdenada.sort(key=lambda donador: donador[0]) #ordena la lista por el nombre del donador. 
    #key es el criterio de ordenamiento
    #lambda es una funcion que toma un donador y devuelve su nombre (donador[0]) entonces se ordena por el nombre
    #sin usar eso se ordenaria por cedula ya que es el primer elemento de cada donador
    for donador in listaOrdenada:
        if obtenerProvincias(donador[1])==pprovincia:
            html+="<tr>"#abre una nueva fila para cada donador, tr significa table row
            html+="<td>"+donador[1]+"</td>" #agrega la cedula
            html+="<td>"+donador[0]+"</td>" #nombre
            html+="<td>"+donador[4]+"</td>" #fecha de naciemiento
            html+="<td>"+donador[7]+"</td>" #telefono
            html+="<td>"+donador[6]+"</td>" #correo
            html+="</tr>"
    html+="</table>" #cierra la tabla
        #se repite el ciclo para cada donador
    html+=cerrarHtml() 
    return guardarHtml("reporteDonadoresProvincia.html",html)
