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
        if pmatrizD[i][0]==pcedula:
            return i
    return -1
    
def obtenerProvincias(pcedula):
    provincia = int(pcedula[0])
    return provincia

def insertarDonador(pmatrizD,pdatos):
    cedula = pdatos[0]
    existe = buscarCedula(pmatrizD,cedula)
    if existe != -1:
        return False
    pmatrizD.append(pdatos)
    return True

def actualizarPeso(pmatrizD,pcedula,pnuevoPeso):
    posicion=buscarCedula(pmatrizD,pcedula)
    if not posicion == -1:
        pmatrizD[posicion][5]=pnuevoPeso
        return pmatrizD
    return []
    
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
    if peso >= 50 and peso <= 120:
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
        "AB-":"Se le recomienda donar plaquetas y plasma."
        "AB-":"Se le recomienda donar plaquetas y plasma."}
    return informacion

def actualizarDonador(pmatrizD,pposicion,pdatos):
    pmatrizD[pposicion][1]=pdatos[0]
    pmatrizD[pposicion][6]=pdatos[1]
    pmatrizD[pposicion][2]=pdatos[2]
    pmatrizD[pposicion][3]=pdatos[3]
    pmatrizD[pposicion][5]=pdatos[4]
    return pmatrizD

def generarCedulaRandom():
    provincia=str(random.randint(1,8)) #Genera un número de provincia entre 1 y 8
    tomo=random.randint(1000,9999) #Genera 4 números aleatorios para el tomo
    asiento=random.randint(1000,9999) #Genera 4 números aleatorios para el asiento
    cedula=f"{provincia}-{tomo}-{asiento}" #Construye la cédula con formato #-####-####
    return cedula

def generarNombreRandom():
    nombres=["Ana","Hilary","Víctor","Kaleb","María","Luis","Carlos","María","Elena","Sofía","Daniel","Andrés"]
    apellidos=["Ramírez","Gómez","Vargas","Solano","Rojas","Castro"] #listas de nombres y apellidos para usar en la generacion
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
    telefono=primerNumero+resto[:3]+"-"+resto[3:] #Genera un número de teléfono con formato #-###-####
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
    return 0

"""def mostrarJustificacion(pnumero):
    justificaciones={
        0:"Apto para donar",
        1:"Menor de edad",
        2:"Peso menor a 50 kg",
        3:"Peso mayor a 120 kg"}
    return justificaciones[pnumero]"""

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
    return [cedula,nombre,fecha,sangre,sexo,peso,telefono,correo,justificacion]

def crearInicioHtml(ptitulo):
    fecha=datetime.now()
    html="<html>" #Comienza el documento HTML
    html+="<head>"
    html+="<title>"+ptitulo+"</title>" #Coloca el título de la página,aparece en la pestaña del navegador
    html+="</head>" 
    html+="<body>" #Todo lo visible va dentro del body
    html+="<h1>"+ptitulo+"</h1>" #Agrega un título grande visible en la página
    html+="<p>"+str(fecha)+"</p>" #Agrega la fecha y hora del sistema
    return html #Retorna el html creado hasta el momento

def cerrarHtml():
    return "</body></html>" #cierra el body y el html, para no repetirlo en cada funcion

def reporteLugaresDonacion(pmatrizD):
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
        cantidad=0
        for donador in pmatrizD:
            if obtenerProvincias(donador[0])==provincia:
                cantidad+=1
        textoLugares=""
        for lugar in lugares[provincia]:
            textoLugares+=lugar+"<br>" #<br> para salto de linea en html
        html+="<tr>"
        html+="<td>"+provincias[provincia]+"</td>"
        html+="<td>"+str(cantidad)+"</td>"
        html+="<td>"+textoLugares+"</td>"
        html+="</tr>"
    html+="</table>"
    html+=cerrarHtml()
    archivo=open("reporteLugares.html","w")
    archivo.write(html)
    archivo.close()
    return True
