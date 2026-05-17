#Elaborado por: Arina Tarasova, Hilary Aguilar
#Fecha de creación: 12/05/2026 01:30 pm
#Última modificación:
#Versión: 3.14.3

#Importación de librerias
from funciones import *

tiposSangre=mostrarTiposSangre()
provincias=mostrarProvincias()
lugaresDonar=crearDiccionarioLugares()
matrizDonadores=cargarArchivo()

def analizarEdadDonarAux(pfecha):
    resultado = analizarEdadDonar(pfecha)
    if resultado == True:
        return "Dado su fecha de nacimiento usted ya puede ser donador"
    else:
        return "Dado su fecha de nacimiento usted aún no puede ser donador"

def ingresarAnalizarEdad():
    fecha =input("Ingrese su fecha de nacimiento: ")
    print(analizarEdadDonarAux(fecha))

def lugarNacimiento(pcedula):
    provincia= mostrarProvincias()
    lugares= crearDiccionarioLugares()
    codProvincia = obtenerProvincias(pcedula)
    nomProvincia= provincia[codProvincia]
    listaLugares = lugares[codProvincia]
    mensaje= ("Dado que usted nació en la provincia de",nomProvincia,", usted podría donar en:\n")
    for lugar in listaLugares:
        mensaje += f"-{lugar}\n"
    return mensaje

def validarPesoAux(ppeso):
    if validarPeso(ppeso):
        return("Usted posee un peso adecuado, correcto para ser donador de sangre.")
    elif ppeso <= 50:
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
                "Particularidades de la sangre tipo A:"
                "Responde diferente al estrés según la ciencia.")
    return ""

def insertarDonadorAux(pmatrizD,pdatos):
    inserto= insertarDonador(pmatrizD,pdatos)
    if inserto == False:
        return False
    guardarArchivo(pmatrizD)
    return True

def opcionInsertarDonador(pmatrizD):
    #Se hace con while True separados, para que en el momento que si ingresa un dato incorrecto
    #lo detenga hasta que lo ingrese de manera correcta.
    while True:
        cedula= input("Ingrese su cédula: ")
        if validarCedula(cedula) == False:
            print("Debe ingresar una cédula válida")
        break
    while True:
        nombre= input("Ingrese su nombre completo: ")
        if nombre != "":
            print("Debe ingresar un nombre Completo")
        break
    while True:
        fecha= input("Ingrese su fecha de nacimiento: ")
        if validarFecha(fecha):
            print("Debe de ingresar una fecha de nacimiento válida")
        break
    while True:
        sangre= input("Ingrese su tipo de sangre: ").upper()
        if sangre in mostrarTiposSangre():
            print("El tipo de sangre debe ser O+, O-, A+, A-, B+, B-, AB+ o AB-.")
        break
    while True:
        sexo= input("Ingrese su sexo: ").upper()
        if sexo != "M" or sexo != "F":
            print("Debe ingresar M o F")
        break
    while True:
        peso= input("Ingrese su peso en Kg: ")
        if not validarPeso(peso):
            print("Debe ingresar un peso válido")
        break
    while True:
        telefono= input("Ingrese su número de teléfono: ")
        if validarTelefono(telefono):
            print("Debe ingresar un número de teléfono con el formato válido")
        break
    while True:
        correo= input("Ingrese su correo: ")
        if validarCorreo(correo):
            print("Debe ingresar un correo con el formato válido")
        break
    datos =[cedula,nombre,fecha,sangre,sexo,peso,telefono,correo]
    inserto = insertarDonadorAux(pmatrizD,datos)
    if inserto:
        print("Donador registrado correctamente")
    else:
        print("La cédula ya existe")

        
        



def actualizarDonadorAux(pnombre,ptelefono,pfecha,psangre,ppeso):
    while True:
        if pnombre==False:
            print("El nombre debe contener al menos 2 caracteres.")
            return False
        if validarTelefono(ptelefono)==False:
            print("El teléfono debe tener el formato ####-#### y comenzar con 2,4,6,7,8 o 9.")
            return False
        if validarFecha(pfecha)==False:
            print("La fecha debe tener el formato dd/mm/yyyy y ser válida.")
            return False
        if psangre==False:
            print("El tipo de sangre debe ser O+, O-, A+, A-, B+, B-, AB+ o AB-.")
            return False
        try:
            ppeso=float(ppeso)
            if validarPeso(ppeso)==False:
                print("El peso mínimo para donar es de 50 kg")
                return False
        except:
            print("El peso debe ser un valor numérico.")
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