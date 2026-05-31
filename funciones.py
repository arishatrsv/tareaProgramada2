#Elaborado por: Arina Tarasova, Hilary Aguilar
#Fecha de creación: 12/05/2026 01:30 pm
#Última modificación:
#Versión: 3.14.3

#Importación de librerias
import pickle
import os #Para crear la carpeta de los reportes
import re
from datetime import datetime
import random
from faker import Faker #permite generar datos aleatorios
fake = Faker("es_MX") #español de Mexico

def mostrarTiposSangre():
    """
    Funcionamiento: Retorna los tipos de sangre disponibles.
    Entrada: Ninguna.
    Salida: tupla con los tipos de sangre válidos.
    """
    tipos = ("O+","O-","A+","A-","B+","B-","AB+","AB-")
    return tipos

def mostrarProvincias():
    """
    Funcionamiento: Retorna el diccionario de provincias.
    Entrada: Ninguna.
    Salida: dict con código de provincia y nombre.
    """
    provincias= {
    1: "San José",
    2: "Alajuela",
    3: "Cartago",
    4: "Heredia",
    5: "Guanacaste",
    6: "Puntarenas",
    7: "Limon",
    8: "Naturalizado"}
    return provincias

def crearDiccionarioLugares():
    """
    Funcionamiento: Retorna el diccionario de centros de donación por provincia.
    Entrada: Ninguna.
    Salida: dict con listas de lugares de donación por provincia.
    """
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
        "Hospital de Guápiles"],
    8:["Banco Nacional de Sangre", 
        "Hospital México",
        "Hospital San Juan de Dios"]}
    return diccionarioLugares

def guardarArchivo(pmatrizD):
    """
    Funcionamiento: Guarda la matriz de donadores en el archivo donadores.txt.
    Entrada: pmatrizD (list) con la matriz de donadores.
    Salida: None.
    """
    archivo=open("donadores.txt","wb")
    pickle.dump(pmatrizD,archivo)
    archivo.close()
    return 

def cargarArchivo():
    """
    Funcionamiento: Carga la matriz de donadores desde el archivo donadores.txt.
    Entrada: Ninguna.
    Salida: Lista de donadores o lista vacía si no existe el archivo.
    """
    try:
        archivo=open("donadores.txt","rb")
        matriz=pickle.load(archivo)
        archivo.close()
        return matriz
    except:
        return []

def buscarCedula(pmatrizD,pcedula):
    """
    Funcionamiento: Busca un donador por cédula en la matriz.
    Entrada: pmatrizD (list), pcedula (str).
    Salida: Índice del donador o -1 si no existe.
    """
    for i in range(len(pmatrizD)):
        if pmatrizD[i][1]==pcedula:
            return i
    return -1
    
def obtenerProvincias(pcedula):
    """
    Funcionamiento: Extrae el código de provincia de la cédula.
    Entrada: pcedula (str) con formato #-####-####.
    Salida: int con el código de provincia.
    """
    provincia = int(pcedula[0])
    return provincia

def insertarDonador(pmatrizD,pdatos):
    """
    Funcionamiento: Inserta un donador si la cédula no existe en la matriz.
    Entrada: pmatrizD (list), pdatos (list) con datos del donador.
    Salida: bool, True si se inserta, False si ya existe.
    """
    cedula = pdatos[1]
    existe = buscarCedula(pmatrizD,cedula)
    if existe != -1:
        return False
    pmatrizD.append(pdatos)
    return True

def validarCedula(pcedula):
    """
    Funcionamiento: Valida que la cédula siga el formato correcto.
    Entrada: pcedula (str) con formato #-####-####.
    Salida: bool, True si la cédula es válida.
    Expresión regular: ^[1-8]-\d{4}-\d{4}$
    """
    if re.match(r"^[1-8]-\d{4}-\d{4}$",pcedula): #Valida que el formato de cedula sea #-####-#### 
        return True
    return False

def validarExpediente(pexpediente):
    """
    Funcionamiento: Valida que el formato del expediente sea correcto (3 letras mayúsculas, # y 4 números).
    Entrada:pexpediente (str): Número de expediente a validar.
    Salida:bool: True si el formato es válido, False en caso contrario.
    Expresión regular:
        ^[A-Z]{3}#[0-9]{4}$
        - [A-Z]{3} : tres letras mayúsculas
        - # : carácter 
        - [0-9]{4} : cuatro dígitos numéricos
    """
    if re.match(r"^[A-Z]{3}#[0-9]{4}$", pexpediente):
        return True
    return False

def validarFecha(pfecha):
    """
    Funcionamiento: Valida la fecha en formato dd/mm/YYYY y retorna objeto datetime.
    Entrada: pfecha (str).
    Salida: datetime si es válida, False si no lo es.
    """
    try:
        fecha=datetime.strptime(pfecha,"%d/%m/%Y") #Verifica que el str es una fecha con el formato correcto
        return fecha
    except:
        return False

def validarCorreo(pcorreo):
    """
    Funcionamiento: Valida el correo electrónico contra dominios permitidos.
    Entrada: pcorreo (str).
    Salida: bool, True si es válido.
    """
    #Valida que solo se puedan los correos con dominio permitido
    if re.match(r"^[\w.%+-]+@(gmail\.com|costarricense\.cr|racsa\.go\.cr|ccss\.sa\.cr)$",pcorreo):
        return True
    return False

def validarTelefono(ptelefono):
    """
    Funcionamiento: Valida el teléfono con formato ####-#### y prefijo permitido.
    Entrada: ptelefono (str).
    Salida: bool, True si es válido.
    """
    #Valida el teléfono cumpla el formato ####-####
    if re.match(r"^[246789]{1}\d{3}-\d{4}$",ptelefono):
        return True
    else:
        return False
    
def validarPeso(ppeso):
    """
    Funcionamiento: Valida que el peso sea numérico y esté en el rango permitido.
    Entrada: ppeso (str).
    Salida: bool, True si el peso es válido.
    """
    if ppeso.isdigit()==False:
        return False
    peso = int(ppeso) 
    if peso > 50 and peso < 120:
        return True
    return False

def analizarEdadDonar(pfecha):
    """
    Funcionamiento: Calcula la edad y verifica si puede donar por edad.
    Entrada: pfecha (str) con fecha de nacimiento.
    Salida: int edad o False si la fecha es inválida.
    """
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
    return edad    

def calcularEdad(pfecha):
    """
    Funcionamiento: Calcula la edad actual en años completos.
    Entrada: pfecha (str) con fecha de nacimiento.
    Salida: int edad.
    """
    fechaNacimiento= validarFecha(pfecha)
    anno= fechaNacimiento.year
    mes= fechaNacimiento.month
    dia= fechaNacimiento.day
    hoy= datetime.now()
    edad= hoy.year-anno
    if(hoy.month,hoy.day)<(mes,dia):
        edad -= 1
    return edad

def mostrarCompatibilidad():
    """
    Funcionamiento: Retorna las opciones de donación posibles para cada tipo de sangre.
    Entrada: Ninguna.
    Salida: dict con compatibilidad de donación.
    """
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

def mostrarRecibeDe():
    """
    Funcionamiento: Retorna la compatibilidad de recepción de sangre.
    Entrada: Ninguna.
    Salida: dict con tipos de sangre de los que se puede recibir.
    """
    recibe = {
        "O-":["O-"],
        "O+":["O-","O+"],
        "A-":["O-","A-"],
        "A+":["O-","O+","A-","A+"],
        "B-":["O-","B-"],
        "B+":["O-","O+","B-","B+"],
        "AB-":["O-","A-","B-","AB-"],
        "AB+":["O-","O+","A-","A+","B-","B+","AB-","AB+"]}
    return recibe

def mostrarInfoSangre():
    """
    Funcionamiento: Retorna recomendaciones según el tipo de sangre.
    Entrada: Ninguna.
    Salida: dict con mensajes de recomendación.
    """
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
    """
    Funcionamiento: Actualiza los datos de un donador en la matriz.
    Entrada: pmatrizD (list), pposicion (int), pdatos (list).
    Salida: pmatrizD actualizado.
    """
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

def eliminarDonador(pmatrizD,pcedula,pjustificacion):
    """
    Funcionamiento: Marca un donador como inactivo y registra la justificación.
    Entrada: pmatrizD (list), pcedula (str), pjustificacion (int).
    Salida: bool, True si se actualiza, False si no existe.
    """
    posicion = buscarCedula(pmatrizD,pcedula)
    if posicion == -1: #Si no existe
        return False
    pmatrizD[posicion][8]=0 #Si existe, cambia el estado
    pmatrizD[posicion][9]= pjustificacion
    return True

def insertarLugar(pdiccionario,pprovincia,plugar):
    """
    Funcionamiento: Inserta un lugar nuevo para donación en una provincia.
    Entrada: pdiccionario (dict), pprovincia (int), plugar (str).
    Salida: bool, False si ya existe, True si se agrega.
    """
    listaLugares = pdiccionario[pprovincia]
    if plugar in listaLugares:
        return False
    listaLugares.append(plugar)
    return True

def generarCedulaRandom():
    """
    Funcionamiento: Genera una cédula costarricense aleatoria con formato #-####-####.
    Entrada: Ninguna.
    Salida: str con la cédula generada.
    """
    provincia=str(random.randint(1,8)) #Genera un número de provincia entre 1 y 8
    tomo=random.randint(1000,9999) #Genera 4 números aleatorios para el tomo
    asiento=random.randint(1000,9999) #Genera 4 números aleatorios para el asiento
    cedula=f"{provincia}-{tomo}-{asiento}" #Construye la cédula con formato #-####-####
    return cedula

def generarNombreSexoRandom():
    """
    Funcionamiento: Genera un nombre completo aleatorio y asigna un sexo.
    Entrada: Ninguna.
    Salida: tuple (nombreCompleto, sexo).
    """
    sexo=random.choice(["M","F"]) #Selecciona aleatoriamente el sexo del donador
    if sexo=="M":
        nombre=fake.first_name_male()
    else:
        nombre=fake.first_name_female()
    apellido1=fake.last_name()
    apellido2=fake.last_name()
    nombreCompleto=nombre+" "+apellido1+" "+apellido2
    return nombreCompleto,sexo

def generarTipoSangreRandom():
    """
    Funcionamiento: Selecciona aleatoriamente un tipo de sangre válido.
    Entrada: Ninguna.
    Salida: str con el tipo de sangre.
    """
    tipos=mostrarTiposSangre()
    return random.choice(tipos) #Selecciona uno aleatoriamente

def generarPesoRandom():
    """
    Funcionamiento: Genera un peso aleatorio para un donador.
    Entrada: Ninguna.
    Salida: str con un peso entre 30 y 150 kg.
    """
    return str(random.randint(30,150))

def generarTelefonoRandom():
    """
    Funcionamiento: Genera un número telefónico aleatorio con formato ####-####.
    Entrada: Ninguna.
    Salida: str con el teléfono generado.
    """
    primerNumero=random.choice(["2","4","6","7","8","9"])
    resto=str(random.randint(1000000,9999999)) #str para poder separarlo despues
    telefono=primerNumero+resto[:3]+"-"+resto[3:] #Genera un número de teléfono con formato ####-####
    return telefono

def generarCorreoRandom(pnombre):
    """
    Funcionamiento: Genera un correo electrónico aleatorio a partir del nombre.
    Entrada: pnombre (str), nombre completo del donador.
    Salida: str con el correo generado.
    """
    usuario=pnombre.lower().replace(" ","") #quita espacios y lo pone en minuscula
    terminaciones=["@costarricense.cr","@racsa.go.cr","@ccss.sa.cr","@gmail.com"]
    terminacion=random.choice(terminaciones) #elige la terminacion al azar
    numero=random.randint(1,99) #agrega un numero para evitar correos repetidos
    correo=usuario+str(numero)+terminacion 
    return correo

def generarFechaRandom():
    """
    Funcionamiento: Genera una fecha de nacimiento aleatoria.
    Entrada: Ninguna.
    Salida: str con la fecha en formato dd/mm/YYYY.
    """
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
    """
    Funcionamiento: Genera una justificación de estado para el donador según edad, peso o causas aleatorias.
    Entrada:
        pfecha (str): fecha de nacimiento.
        ppeso (str): peso del donador.
    Salida:
        int con el código de justificación.
    """
    if analizarEdadDonar(pfecha)<18: #menor de edad
        return 1
    if int(ppeso)<50: #Peso menor al mínimo permitido
        return 2
    if int(ppeso)>120: #Peso mayor al máximo permitido
        return 3
    otrasJustificaciones=[0,4,5,6,7,8,0,0,0] #puse 0 para que sea mas probable que sea apto
    return random.choice(otrasJustificaciones)

def mostrarJustificacion():
    """
    Funcionamiento: Retorna el diccionario de justificaciones para el estado del donador.
    Entrada: Ninguna.
    Salida: dict con código y descripción de la justificación.
    """
    justificaciones={
        0:"Apto para donar",
        1:"Menor de edad",
        2:"Peso menor a 50 kg",
        3:"Peso mayor a 120 kg",
        4:"Enfermedad infecciosa o crónica",
        5:"Uso de medicamentos no permitidos",
        6:"Procedimiento médico reciente",
        7:"Conducta de riesgo",
        8:"Viaje reciente a zona de riesgo"}
    return justificaciones

def generarEstadoDonador(pjustificacion):
    """
    Funcionamiento: Determina el estado del donador según la justificación.
    Entrada: pjustificacion (int).
    Salida: 1 si está activo, 0 si está inactivo.
    """
    if pjustificacion == 0:
        return 1 #Activo
    return 0 #Inactivo

def generarDonadorRandom():
    """
    Funcionamiento: Genera un donador con datos aleatorios.
    Entrada: Ninguna.
    Salida: list con los datos completos del donador.
    """
    cedula=generarCedulaRandom()
    nombre,sexo=generarNombreSexoRandom()    
    fecha=generarFechaRandom()
    sangre=generarTipoSangreRandom()
    peso=generarPesoRandom()
    telefono=generarTelefonoRandom()
    correo=generarCorreoRandom(nombre)
    justificacion=generarJustificacionRandom(fecha,peso)
    estado=generarEstadoDonador(justificacion)
    return [nombre,cedula,sangre,sexo,fecha,peso,correo,telefono,estado,justificacion]

def crearInicioHtml(ptitulo):
    """
    Funcionamiento: Crea el inicio del reporte HTML con título y fecha.
    Entrada: ptitulo (str) con el título de la página.
    Salida: str con el contenido HTML inicial.
    """
    fecha=datetime.now()
    html="<html>" #Comienza el documento HTML
    html+="<head>"
    html+="<meta charset='utf-8'>" #formato de caracteres especiales, sin esa linea sale así "TelÃ©fono"
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
    th{background-color:lightgray;}
    </style>""" #cierra la seccion de estilos.
    html+="</head>" 
    html+="<body>" #Todo lo visible va dentro del body
    html+="<h1>"+ptitulo+"</h1>" #Agrega un título grande visible en la página
    html+="<h2>"+str(fecha.strftime("%d/%m/%Y %H:%M"))+"</h2>" #Agrega la fecha y hora del sistema, <p> es un parrafo
    return html #Retorna el html creado hasta el momento

def cerrarHtml():
    """
    Funcionamiento: Retorna las etiquetas de cierre para un documento HTML.
    Entrada: Ninguna.
    Salida: str con las etiquetas de cierre HTML.
    """
    return "</body></html>" #cierra el body y el html, para no repetirlo en cada funcion

def guardarHtml(pnombreArchivo,phtml):
    """
    Funcionamiento: Guarda un contenido HTML en un archivo.
    Entrada: pnombreArchivo (str), phtml (str).
    Salida: bool True si la operación se completa.
    """
    os.makedirs("reportes",exist_ok=True) #Esto verifica si la carpeta reportes existe, si no, la crea
    archivo=open(pnombreArchivo,"w",encoding="utf-8") #utf-8 es algo que encontre para caracteres especiales. 
    archivo.write(phtml) #Escribe todo el html dentro del archivo
    archivo.close()
    return True

def generarReporteDonadoresProvincia(pmatrizD,pprovincia):
    """
    Funcionamiento: Genera un reporte HTML de donadores de una provincia.
    Entrada: pmatrizD (list), pprovincia (int).
    Salida: bool, True si se guarda el archivo correctamente.
    """
    html=crearInicioHtml("Reporte Donadores por Provincia")
    html+="<table>"
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
    return guardarHtml("reportes/reporteDonadoresProvincia.html",html)

def generarReporteRangoEdad(pmatrizD,pedadInicial,pedadFinal):
    """
    Funcionamiento: Genera un reporte HTML de donadores dentro de un rango de edad.
    Entrada: pmatrizD (list), pedadInicial (int), pedadFinal (int).
    Salida: bool, True si se guarda el archivo correctamente.
    """
    html=crearInicioHtml("Reporte por Rango de Edad")
    html+="<table>"
    html+="<tr>" #abre la fila de encabezados
    html+="<th>Cédula</th>" #agrega los titulod de las columnas
    html+="<th>Nombre</th>"
    html+="<th>Fecha Nacimiento</th>"
    html+="<th>Teléfono</th>"
    html+="<th>Correo</th>"
    html+="</tr>"
    for donador in pmatrizD:
        edad=calcularEdad(donador[4])
        if edad >= pedadInicial and edad <= pedadFinal:
            html+="<tr>"#abre una nueva fila para cada donador, tr significa table row
            html+="<td>"+donador[1]+"</td>" #agrega la cedula
            html+="<td>"+donador[0]+"</td>" #nombre
            html+="<td>"+donador[4]+"</td>" #fecha de naciemiento
            html+="<td>"+donador[7]+"</td>" #telefono
            html+="<td>"+donador[6]+"</td>" #correo
            html+="</tr>"
    html+="</table>" #cierra la tabla 
    html+=cerrarHtml() 
    return guardarHtml("reportes/reporteRangoEdad.html",html)  

def generarReporteListaDonadores(pmatrizD):
    """
    Funcionamiento: Genera un reporte HTML de todos los donadores agrupados por provincia.
    Entrada: pmatrizD (list).
    Salida: bool, True si se guarda el archivo correctamente.
    """
    html=crearInicioHtml("Reporte Lista Completa de Donadores")
    html+="<table>"
    html+="<tr>" #abre la fila de encabezados
    html+="<th>Cédula</th>" #Agrega los títulos de las columnas, th significa table header
    html+="<th>Nombre Completo</th>"
    html+="<th>Tipo de sangre</th>"
    html+="<th>Fecha de nacimiento</th>"
    html+="<th>Peso</th>"
    html+="<th>Sexo</th>"
    html+="<th>Teléfono</th>"
    html+="<th>Correo</th>"
    html+="</tr>" #cierra la fila de encabezados
    provincias= mostrarProvincias()
    for provincia in provincias: #Recorre provincias
        html+="<tr><td colspan='8'><h2>"+provincias[provincia]+"</h2></td></tr>" #Encabezado con el nombre de la Provincia
        for donador in pmatrizD: #Recorre donadores
            provinciaDonador= obtenerProvincias(donador[1])
            if provinciaDonador==provincia:
                html+="<tr>"
                html+="<td>"+donador[1]+"</td>" #agrega la cedula
                html+="<td>"+donador[0]+"</td>" #nombre
                html+="<td>"+donador[2]+"</td>" #tipo de sangre
                html+="<td>"+donador[4]+"</td>" #Fecha nacimiento
                html+="<td>"+donador[5]+"</td>" #Peso
                html+="<td>"+donador[3]+"</td>" #Sexo
                html+="<td>"+donador[7]+"</td>" #Teléfono
                html+="<td>"+donador[6]+"</td>" #Correo
                html+="</tr>"
    html+="</table>" #cierra la tabla 
    html+=cerrarHtml() 
    return guardarHtml("reportes/reporteListaDonadores.html",html)  

def generarReportePuedeDonar(pmatrizD,ptipo):
    """
    Funcionamiento: Genera un reporte HTML de donadores compatibles para donar.
    Entrada: pmatrizD (list), ptipo (str).
    Salida: bool, True si se guarda el archivo correctamente.
    """
    compatibilidad= mostrarCompatibilidad()
    listaCompatibles= compatibilidad[ptipo]
    html=crearInicioHtml("Reporte ¿A quién puede donar?")
    html+="<h2>Tipo de sangre seleccionado: "+ptipo+"</h2>"
    html+="<table>" #Crea una tabla con bordes visibles
    html+="<tr>" #Abre la fila de encabezados 
    html+="<th>Cédula</th>" #Agrega los títulos de las columnas, th significa table header
    html+="<th>Nombre Completo</th>"
    html+="<th>Tipo de sangre</th>"
    html+="<th>Teléfono</th>"
    html+="<th>Correo</th>"
    html+="</tr>" #Cierra la fila de encabezados
    provincias= mostrarProvincias()
    for provincia in provincias: #Recorre provincias
        for donador in pmatrizD: #Recorre donadores
            provinciaDonador= obtenerProvincias(donador[1])
            tipoDonador=donador[2]
            if provinciaDonador==provincia:
                if tipoDonador in listaCompatibles:
                    html+="<tr>"
                    html+="<td>"+donador[1]+"</td>" #agrega la cedula
                    html+="<td>"+donador[0]+"</td>" #nombre
                    html+="<td>"+donador[2]+"</td>" #tipo de sangre
                    html+="<td>"+donador[7]+"</td>" #telefono
                    html+="<td>"+donador[6]+"</td>" #correo
                    html+="</tr>"
    html+="</table>" #cierra la tabla 
    html+=cerrarHtml() 
    return guardarHtml("reportes/reporteAquienPuedeDonar.html",html)  
            
def generarReporteRecibeDe(pmatrizD,ptipo):
    """
    Funcionamiento: Genera un reporte HTML de donadores compatibles para recibir.
    Entrada: pmatrizD (list), ptipo (str).
    Salida: bool, True si se guarda el archivo correctamente.
    """
    recibe= mostrarRecibeDe()
    listaCompatibles= recibe[ptipo]
    html=crearInicioHtml("Reporte ¿De quién puede recibir?")
    html+="<h2>Tipo de sangre seleccionado: "+ptipo+"</h2>"
    html+="<table>" #bordes visibles
    html+="<tr>" #fila de encabezados 
    html+="<th>Cédula</th>" #Agrega los títulos de las columnas, th significa table header
    html+="<th>Nombre Completo</th>"
    html+="<th>Tipo de sangre</th>"
    html+="<th>Teléfono</th>"
    html+="<th>Correo</th>"
    html+="</tr>"
    provincias= mostrarProvincias()
    for provincia in range(7,0,-1): #recorre provincias en orden inverso
        for donador in pmatrizD:
            provinciaDonador= obtenerProvincias(donador[1]) #donador[1] es la cedula y de ahi se saca la provincia
            tipoDonador=donador[2]
            if provinciaDonador==provincia and tipoDonador in listaCompatibles:
                html+="<tr>"
                html+="<td>"+donador[1]+"</td>" #agrega la cedula
                html+="<td>"+donador[0]+"</td>" #nombre
                html+="<td>"+donador[2]+"</td>" #tipo de sangre
                html+="<td>"+donador[7]+"</td>" #telefono
                html+="<td>"+donador[6]+"</td>" #correo
                html+="</tr>"
    html+="</table>" #cierra la tabla 
    html+=cerrarHtml() 
    return guardarHtml("reportes/reporteDeQuienPuedeRecibir.html",html) 

def generarReporteNoActivo(pmatrizD):
    """
    Funcionamiento: Genera un reporte HTML de donadores inactivos.
    Entrada: pmatrizD (list).
    Salida: bool, True si se guarda el archivo correctamente.
    """
    html=crearInicioHtml("Reporte Donantes NO Activos")
    html+="<table>" #bordes visibles
    html+="<tr>" #fila de encabezados
    html+="<th>Justificación</th>" 
    html+="<th>Cédula</th>" #Agrega los títulos de las columnas, th significa table header
    html+="<th>Nombre Completo</th>"
    html+="<th>Tipo de sangre</th>"
    html+="<th>Fecha de nacimiento</th>"
    html+="<th>Peso</th>"
    html+="<th>Sexo</th>"
    html+="<th>Teléfono</th>"
    html+="<th>Correo</th>"
    html+="</tr>" #Cierra la fila de encabezados
    for donador in pmatrizD:
        estado=donador[8]
        if estado==0: #Solo NO activos
            justificaciones=mostrarJustificacion()
            justificacion= justificaciones[donador[9]] #donador[9] es el codigo de justificacion, se obtiene el texto con el diccionario
            html+="<tr>"
            html+="<td>"+justificacion+"</td>"
            html+="<td>"+donador[1]+"</td>" #agrega la cedula
            html+="<td>"+donador[0]+"</td>" #nombre
            html+="<td>"+donador[2]+"</td>" #tipo de sangre
            html+="<td>"+donador[4]+"</td>" #Fecha nacimiento
            html+="<td>"+donador[5]+"</td>" #Peso
            html+="<td>"+donador[3]+"</td>" #Sexo
            html+="<td>"+donador[7]+"</td>" #Teléfono
            html+="<td>"+donador[6]+"</td>" #Correo
            html+="</tr>"
    html+="</table>" #cierra la tabla
    html+=cerrarHtml() 
    return guardarHtml("reportes/reporteNoActivos.html",html)

def generarReporteLugaresDonacion(pmatrizD):
    """
    Funcionamiento: Genera un reporte HTML de lugares de donación por provincia.
    Entrada: pmatrizD (list).
    Salida: bool, True si se guarda el archivo correctamente.
    """
    html=crearInicioHtml("Reporte Lugares de Donación")
    html+="<table>" #Crea una tabla con bordes visibles
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
        html+="<td>"+str(cantidad)+"</td>" #Agrega la cantidad de donadores
        html+="<td>"+textoLugares+"</td>" #Agrega los lugares de donacion con saltos de linea
        html+="</tr>" #cierra la fila de provincia
        #aqui se repite el ciclo para cada provincia creando una fila nueva
    html+="</table>" #cierra la tabla
    html+=cerrarHtml() 
    return guardarHtml("reportes/reporteLugares.html",html)

def generarReporteMujeresDonantes(pmatrizD):
    """
    Funcionamiento: Genera un reporte HTML de mujeres donantes O- menores de 45 años.
    Entrada: pmatrizD (list).
    Salida: bool, True si se guarda el archivo correctamente.
    """
    html=crearInicioHtml("Reporte Mujeres Donantes")
    html+="<table>" #bordes visibles
    html+="<tr>" #fila de encabezados 
    html+="<th>Cédula</th>" #Agrega los títulos de las columnas, th significa table header
    html+="<th>Nombre Completo</th>"
    html+="<th>Fecha de Nacimento</th>"
    html+="<th>Teléfono</th>"
    html+="<th>Correo</th>"
    html+="</tr>"
    listaOrdenada=pmatrizD[:]#hace una copia de lista para no modificar el orden original
    listaOrdenada.sort(key=lambda donador: analizarEdadDonar(donador[4]))
    #key-criterio de ordenamiento
    #lambda toma un donador y devuelve su edad, entonces se ordena por edad
    for donador in listaOrdenada:
        sexo=donador[3]
        sangre=donador[2]
        edad=analizarEdadDonar(donador[4])
        if sexo=="F" and sangre=="O-" and edad<45: #mujeres O- menos de 45
            html+="<tr>"
            html+="<td>"+donador[1]+"</td>"
            html+="<td>"+donador[0]+"</td>"
            html+="<td>"+donador[4]+"</td>"
            html+="<td>"+donador[7]+"</td>" #telefono
            html+="<td>"+donador[6]+"</td>"
            html+="</tr>"
    html+="</table>"
    html+=cerrarHtml()
    return guardarHtml("reportes/reporteMujeresDonantes.html",html)

def generarReporteTipoProvincia(pmatrizD,ptipo,pprovincia):
    """
    Funcionamiento: Genera un reporte HTML de donadores por tipo de sangre y provincia.
    Entrada: pmatrizD (list), ptipo (str), pprovincia (int).
    Salida: bool, True si se guarda el archivo correctamente.
    """
    html=crearInicioHtml("Reporte Donadores por Tipo de Sangre y Provincia")
    html+="<h2>Tipo de sangre: "+ptipo+"</h2>"
    html+="<h2>Provincia: "+mostrarProvincias()[pprovincia]+"</h2>"
    html+="<table>"
    html+="<tr>"
    html+="<th>Cédula</th>"
    html+="<th>Nombre Completo</th>"
    html+="<th>Fecha de nacimiento</th>"
    html+="<th>Teléfono</th>"
    html+="<th>Correo</th>"
    html+="</tr>"
    for donador in pmatrizD:
        provincia=obtenerProvincias(donador[1])
        sangre=donador[2]
        estado=donador[8] #1=activo, 0=inactivo
        if provincia==pprovincia and sangre==ptipo and estado==1:
            html+="<tr>"
            html+="<td>"+donador[1]+"</td>"
            html+="<td>"+donador[0]+"</td>"
            html+="<td>"+donador[4]+"</td>"
            html+="<td>"+donador[7]+"</td>"
            html+="<td>"+donador[6]+"</td>"
            html+="</tr>"
    html+="</table>"
    html+=cerrarHtml()
    return guardarHtml("reportes/reporteTipoSangrePorProvincia.html",html)
