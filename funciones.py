#Elaborado por: Arina Tarasova, Hilary Aguilar
#Fecha de creación: 12/05/2026 01:30 pm
#Última modificación:
#Versión: 3.14.3

#Importación de librerias
import pickle
import re
from datetime import datetime
import random
from faker import Faker #permite generar datos aleatorios
fake = Faker("es_MX") #español de Mexico

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
    return edad    

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

def mostrarRecibeDe():
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

def eliminarDonador(pmatrizD,pcedula,pjustificacion):
    posicion = buscarCedula(pmatrizD,pcedula)
    if posicion == -1: #Si no existe
        return False
    pmatrizD[posicion][8]=0 #Si existe, cambia el estado
    pmatrizD[posicion][9]= pjustificacion
    return True

def insertarLugar(pdiccionario,pprovincia,plugar):
    listaLugares = pdiccionario[pprovincia]
    if plugar in listaLugares:
        return False
    listaLugares.append(plugar)
    return True

def generarCedulaRandom():
    provincia=str(random.randint(1,8)) #Genera un número de provincia entre 1 y 8
    tomo=random.randint(1000,9999) #Genera 4 números aleatorios para el tomo
    asiento=random.randint(1000,9999) #Genera 4 números aleatorios para el asiento
    cedula=f"{provincia}-{tomo}-{asiento}" #Construye la cédula con formato #-####-####
    return cedula

def generarNombreSexoRandom():
    sexo=random.choice(["M","F"])
    if sexo=="M":
        nombre=fake.first_name_male()
    else:
        nombre=fake.first_name_female()
    apellido1=fake.last_name()
    apellido2=fake.last_name()
    nombreCompleto=nombre+" "+apellido1+" "+apellido2
    return nombreCompleto,sexo

def generarTipoSangreRandom():
    tipos=mostrarTiposSangre()
    return random.choice(tipos)

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
    if analizarEdadDonar(pfecha)<18:
        return 1
    if int(ppeso)<50:
        return 2
    if int(ppeso)>120:
        return 3
    otrasJustificaciones=[0,4,5,6,7,0,0,0] #puse 0 para que sea mas probable que sea apto
    return random.choice(otrasJustificaciones)

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

def generarEstadoDonador(pjustificacion):
    if pjustificacion == 0:
        return "Apto"
    return "No apto"

def generarDonadorRandom():
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
    return "</body></html>" #cierra el body y el html, para no repetirlo en cada funcion

def guardarHtml(pnombreArchivo,phtml):
    archivo=open(pnombreArchivo,"w",encoding="utf-8") #utf-8 es algo que encontre para caracteres especiales. 
    archivo.write(phtml) #Escribe todo el html dentro del archivo
    archivo.close()
    return True

def generarReporteDonadoresProvincia(pmatrizD,pprovincia):
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
    return guardarHtml("reporteDonadoresProvincia.html",html)

def generarReportePuedeDonar(pmatrizD,ptipo):
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
    return guardarHtml("reporteAquienPuedeDonar.html",html)  
            
def generarReporteLugaresDonacion(pmatrizD):
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
    return guardarHtml("reporteLugares.html",html)

def generarReporteRecibeDe(pmatrizD,ptipo):
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
    return guardarHtml("reporteDeQuienPuedeRecibir.html",html) 

def generarReporteMujeresDonantes(pmatrizD):
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
    return guardarHtml("reporteMujeresDonantes.html",html)
