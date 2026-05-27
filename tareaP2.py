#Elaborado por: Arina Tarasova, Hilary Aguilar
#Fecha de creación: 12/05/2026 01:30 pm
#Última modificación:
#Versión: 3.14.3

#Importación de funciones.py
from funciones import *

tiposSangre=mostrarTiposSangre()
provincias=mostrarProvincias()
lugaresDonar=crearDiccionarioLugares()
matrizDonadores=cargarArchivo()

def analizarEdadDonarAux(pfecha):
    resultado = analizarEdadDonar(pfecha)
    if resultado == False:
        return "Fecha inválida"
    elif resultado >=18:
        return "Dado su fecha de nacimiento usted ya puede ser donador"
    else:
        return "Dado su fecha de nacimiento usted aún no puede ser donador"

def ingresarAnalizarEdad():
    fecha =input("Ingrese su fecha de nacimiento: ")
    print(analizarEdadDonarAux(fecha))

def imprimirLugarNacimiento(pcedula):
    provincia= mostrarProvincias()
    lugares= crearDiccionarioLugares()
    codProvincia = obtenerProvincias(pcedula)
    nomProvincia= provincia[codProvincia]
    listaLugares = lugares[codProvincia]
    mensaje="Dado que usted nació en la provincia de "+nomProvincia+", usted podría donar en:\n"    
    for lugar in listaLugares:
        mensaje += f"-{lugar}\n"
    return mensaje

def validarPesoAux(ppeso):
    try:
        peso=int(ppeso)
    except:
        return "Peso inválido. Debe ingresar solo números."
    if validarPeso(ppeso):
        return("Usted posee un peso adecuado, correcto para ser donador de sangre.")
    elif peso < 50:
        return("Usted debe pesar más de 50 kgms para poder ser donador.")
    else:
        return("Dado su sobre peso, no es posible donar sangre.")

def donarSangre(ptipo):
    compatibilidad = mostrarCompatibilidad()
    informacion = mostrarInfoSangre()
    listaCompatibles = compatibilidad[ptipo]
    info = informacion[ptipo]
    mensaje = ("Dado su tipo de sangre y RH usted puede donar a:\n")
    for sangre in listaCompatibles:
        mensaje += f"-{sangre}\n"
    mensaje += "\n"
    mensaje += info
    return mensaje

def recomendarVideo(ptipo):
    if ptipo == "A+" or ptipo == "A-":
        return ("Le recomendamos ver el video de:\n"
                "Particularidades de la sangre tipo A: "
                "Responde diferente al estrés según la ciencia.")
    return ""

def insertarDonadorAux(pmatrizD,pdatos):
    inserto= insertarDonador(pmatrizD,pdatos)
    if inserto == False:
        return False
    guardarArchivo(pmatrizD)
    return True

def insertarDonadorMostrar(pmatrizD,pcedula,pnombre,pfecha,psangre,psexo,ppeso,ptelefono,pcorreo):
    if validarCedula(pcedula)==False:
        return "Cédula inválida. Debe tener el formato #-####-####"
    if pnombre.replace(" ","").isalpha()== False:
        return "Debe ingresar un nombre Completo"
    if validarFecha(pfecha)==False:
        return "Fecha inválida. Debe ser en formato dd/mm/aaaa"
    if psangre not in mostrarTiposSangre():
        return "Tipo de sangre inválido"
    if validarPeso(ppeso)== False:
     return validarPesoAux(ppeso)
    if validarTelefono(ptelefono)==False:
        return "Teléfono inválido. Debe ser en formato ####-#### y comenzar con 2,4,6,7,8 o 9."
    if validarCorreo(pcorreo)==False:
        return "Correo inválido. Debe contener un @ y un dominio"
    justificacion = generarJustificacionRandom(pfecha,ppeso)
    estado=generarEstadoDonador(justificacion)
    datos =[pnombre,pcedula,psangre,psexo,pfecha,ppeso,pcorreo,ptelefono,estado,justificacion]
    inserto = insertarDonadorAux(pmatrizD,datos)
    if inserto:
        return datos
    return "La cédula ya existe"
        
def actualizarDonadorAux(pnombre,ptelefono,pfecha,psangre,ppeso):
    if pnombre=="":
        print("Debe ingresar un nombre valido.")
        return False
    if validarTelefono(ptelefono)==False:
        print("El teléfono debe tener el formato ####-#### y comenzar con 2,4,6,7,8 o 9.")
        return False
    if validarFecha(pfecha)==False:
        print("La fecha debe tener el formato dd/mm/yyyy y ser válida.")
        return False
    if psangre not in mostrarTiposSangre():
        print("El tipo de sangre debe ser O+, O-, A+, A-, B+, B-, AB+ o AB-.")
        return False
    if validarPeso(ppeso)==False:
        print("El peso debe ser mayor o igual a 50 kg y menor o igual a 120 kg.")
        return False
    return [pnombre,ptelefono,pfecha,psangre,ppeso]

def opcionActualizarDonador(pposicion):
    print("Número de cédula:",matrizDonadores[pposicion][1])
    nombre=input("Digite el nombre completo: ")
    telefono=input("Digite el teléfono: ")
    fecha=input("Digite la fecha de nacimiento (dd/mm/yyyy): ")
    sangre=input("Digite el tipo de sangre: ").upper()
    peso=input("Digite el peso: ")
    datos=actualizarDonadorAux(nombre,telefono,fecha,sangre,peso)
    if not datos==False:
        return datos
        
def menuActualizarDonador(pposicion):
    datos=opcionActualizarDonador(pposicion)
    while True:
        print("-----ACTUALIZAR DONADOR-----")
        print("\n1. Confirmar actualización")
        print("\n2. Cancelar actualización")
        print("\n3. Regresar")
        opcion=input("Digite una opción: ")
        if opcion=="1":
            actualizarDonador(matrizDonadores,pposicion,datos)
            guardarArchivo(matrizDonadores)
            return "Datos actualizados correctamente."
        elif opcion=="2":
            print("Datos No actualizados.")
        elif opcion=="3":
            return
        else:
            print("La opción seleccionada no existe. Ingrese una opción 1-3")

def eliminarDonadorAux(matrizDonadores,pcedula,pjustificacion):
    if validarCedula(pcedula)==False:
        return "Debe ingresar una cédula válida"
    posicion = buscarCedula(matrizDonadores,pcedula)
    if posicion == -1:
        return "La persona con el número de cédula: "+pcedula+" no está registrado en la base de datos del Banco de Sangre aún."
    if pjustificacion=="":
        return "Debe ingresar una justificación"
    return True

#No sirve
"""
def opcionEliminarDonador():
    cedula = input("Digite el número de cédula: ")
    print("1- Menor de edad")
    print("2- Peso menor a 50 kg")
    print("3- Peso mayor a 120 kg")
    print("4- Enfermedad infecciosa o crónica")
    print("5- Uso de medicamentos no permitidos")
    print("6- Procedimiento médico reciente")
    print("7- Viaje o conducta de riesgo")
    try:
        justificacion= int(input("Digite la justificación de eliminación: "))
    except:
        print("Debe ingresar un número válido.")
        return False
    if justificacion not in [1,2,3,4,5,6,7]:
        print("Debe seleccionar una opción válida.")
        return False
    eliminado=eliminarDonadorAux(matrizDonadores,cedula,justificacion)
    if not eliminado==False:
        return eliminado
"""
def eliminarDonadorMostrar(matrizDonadores,pcedula,pjustificacion,pconfirmar):
    validacion= eliminarDonadorAux(matrizDonadores,pcedula,pjustificacion)
    if validacion != True:
        return validacion
    if pconfirmar == True:
        eliminarDonador(matrizDonadores,pcedula,int(pjustificacion))
        guardarArchivo(matrizDonadores)
        return "Donador eliminado satisfactoriamente."
    else:
        return "Donador NO eliminado"

def insertarLugarAux(plugaresDonar,pprovincia,plugar):
    if pprovincia not in mostrarProvincias():
        return "Debe seleccionar una provincia válida"
    if plugar.strip()=="":
        return "Debe ingresar un lugar válido"
    insertar= insertarLugar(plugaresDonar,pprovincia,plugar)
    if insertar == False:
        return "El lugar ya está registrado en esa provincia."
    return "Lugar agregado correctamente."

def generarDonadoresAux(pmatrizD,pcantidad):
    #en caso de que se repite la cedula no se guarda el donador
    # para eso se hace un ciclo while hasta que se genera la cantidad deseada
    generados=0  
    while generados<pcantidad:
        datos=generarDonadorRandom()
        inserto=insertarDonador(pmatrizD,datos)
        if inserto: #True si no se repite la cedula
            generados+=1 #solo aumenta si incerte correctamente
    guardarArchivo(pmatrizD)
    return f"{pcantidad} donadores generados correctamente."

def opcionGenerarDonadores():
    while True:
        cantidad=input("Digite la cantidad de donadores a generar: ")
        if cantidad.isdigit()==False:
            print("Debe ingresar únicamente números.")
            continue #vuelve a pedir la cantidad reiniciando el ciclo
        cantidad=int(cantidad)
        if cantidad<=0:
            print("La cantidad debe ser mayor a 0.")
            continue
        break
    return generarDonadoresAux(matrizDonadores,cantidad)

def opcionReporteProvincia():
    print(mostrarProvincias())
    provincia=int(input("Digite el número de provincia: "))
    if provincia not in mostrarProvincias():
        return "Provincia inválida."
    reporte=generarReporteDonadoresProvincia(matrizDonadores,provincia)
    if reporte:
        return "Reporte creado satisfactoriamente"
    else:
        return "Reporte no creado"

def opcionReporteRangoEdad():
    edadInicial=int(input("Ingrese la edad inicial: "))
    if edadInicial < 18 or edadInicial > 65:
        return "La edad inicial debe estar entre 18 y 65 años."
    while True:
        try:
            edadFinal=int(input("Ingrese la edad final: "))
        except:
            print("Debe ingresar un número válido.")
            continue
        if edadFinal < 18 or edadFinal > 65:
            return "La edad final debe estar entre 18 y 65 años."
        if edadFinal < edadInicial:
            return "La edad final no puede ser menor que la inicial."
        reporte=generarReporteRangoEdad(matrizDonadores,edadInicial,edadFinal)
        if reporte:
            return "Reporte creado satisfactoriamente"
        else:
            return "Reporte no creado"

def opcionReporteListaDonadores():
    opcion=input("Digite una opción: ")
    if opcion=="1": #Genera reporte
        reporte=generarReporteListaDonadores(matrizDonadores)
        if reporte:
            return "Reporte creado satisfactoriamente"
        else:
            return "Reporte no creado."
        return
    elif opcion=="2": #Regresa al menú reportes
        return
    else:
        print("Debe seleccionar una opción válida.")

def opcionReporteDonar():
    for tipo in tiposSangre:
        print("-",tipo)
    print("9 - Regresar")
    tipo= input("Seleccione el tipo de sangre: ").upper()
    if tipo=="9": #Regresa al menú reportes
        return
    if tipo not in tiposSangre:
        print("Debe ingresar un tipo de sangre válido.")
    reporte=generarReportePuedeDonar(matrizDonadores,tipo)
    if reporte:
        print("Reporte creado satisfactoriamente.")
    else:
        print("Reporte no creado.")
    return

def opcionReporteRecibeDe():
    for tipo in tiposSangre:
        print("-",tipo)
    print("9 - Regresar")
    tipo = input("Seleccione el tipo de sangre: ").upper()
    if tipo=="9":
        return
    if tipo not in tiposSangre:
        return "Debe ingresar un tipo de sangre válido."
    reporte=generarReporteRecibeDe(matrizDonadores,tipo)
    if reporte:
        return "Reporte creado satisfactoriamente."
    else:
        return "Reporte no creado."

def opcionReporteMujeresO():
    reporte=generarReporteMujeresDonantes(matrizDonadores)
    if reporte:
        return "Reporte creado satisfactoriamente."
    else:
        return "Reporte no creado."
    
def opcionReporteNoActivo():
    opcion=input("Digite una opción: ")
    if opcion=="1": #Genera reporte
        reporte=generarReporteNoActivo(matrizDonadores)
        if reporte:
            print("Reporte creado satisfactoriamente")
        else:
            print("Reporte no creado.")
        return
    elif opcion=="2": #Regresa al menú reportes
        return
    else:
        print("Debe seleccionar una opción válida.")

def opcionReporteLugares():
    reporte=generarReporteLugaresDonacion(matrizDonadores)
    if reporte:
        return "Reporte creado satisfactoriamente."
    else:
        return "Reporte no creado."

def opcionReporteTipoProvincia():
    for tipo in tiposSangre:
        print("-",tipo)
    tipo=input("Digite el tipo de sangre: ").upper()
    if tipo not in tiposSangre:
        return "Debe ingresar un tipo de sangre válido."
    print(mostrarProvincias())
    try:
        provincia=int(input("Digite la provincia: "))
    except:
        return "Debe ingresar un número válido."
    if provincia not in mostrarProvincias():
        return "Provincia inválida. Intente nuevamente."
    reporte=generarReporteTipoProvincia(matrizDonadores,tipo,provincia)
    if reporte:
        return "Reporte creado satisfactoriamente."
    else:
        return "Reporte no creado."

def buscarCedulaActualizar():
    cedula=input("Digite la cédula del donador: ")
    if validarCedula(cedula)==False:
        print("Debe ingresar una cédula válida.")
        return
    posicion=buscarCedula(matrizDonadores,cedula)
    if posicion==-1:
        print("No existe un donador con esa cédula.")
        return
    print(menuActualizarDonador(posicion))
    
def menuReportes():
    while True:
        print("\n----- REPORTES -----")
        print("1. Reporte donadores por provincia")
        print("2. Reporte por rango de edad")
        print("3. Reporte lista completa de donadores")
        print("4. Reporte ¿A quién puede donar?")
        print("5. Reporte ¿De quién puede recibir?")
        print("6. Reporte mujeres donantes O- menores de 45")
        print("7. Reporte donadores NO activos")
        print("8. Reporte lugares de donación")
        print("9. Reporte por tipo de sangre y provincia")
        print("10. Regresar")
        opcion=input("\nDigite una opción: ")
        if opcion=="1":
            print(opcionReporteProvincia())
        elif opcion=="2":
            print(opcionReporteRangoEdad())
        elif opcion=="3":
            print(opcionReporteListaDonadores())
        elif opcion=="4":
            opcionReporteDonar()
        elif opcion=="5":
            print(opcionReporteRecibeDe())
        elif opcion=="6":
            print(opcionReporteMujeresO())
        elif opcion=="7":
            opcionReporteNoActivo()
        elif opcion=="8":
            print(opcionReporteLugares())
        elif opcion=="9":
            print(opcionReporteTipoProvincia())
        elif opcion=="10":
            return
        else:
            print("Debe seleccionar una opción válida.")
    
def menuPrincipal():
    while True:
        print("\n----- BANCO DE SANGRE -----")
        print("1. Insertar donador")
        print("2. Generar donadores")
        print("3. Actualizar datos del donador")
        print("4. Eliminar donador")
        print("5. Insertar lugar de donación según provincia")
        print("6. Reportes")
        print("7. Salir")
        opcion=input("Digite una opción: ")
        if opcion=="1":
            opcionInsertarDonador(matrizDonadores)
        elif opcion=="2":
            print(opcionGenerarDonadores())
        elif opcion=="3":
            buscarCedulaActualizar()
        elif opcion=="4":
            print(menuEliminarDonador())
        elif opcion=="5":
            opcionInsertarLugar()
        elif opcion=="6":
            menuReportes()
        elif opcion=="7":
            print("Donar sangre,es donar vida")
            break
        else:
            print("Debe seleccionar una opción válida.")
#menuPrincipal()
