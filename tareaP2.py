#Elaborado por: Arina Tarasova, Hilary Aguilar
#Fecha de creación: 12/05/2026 01:30 pm
#Última modificación:
#Versión: 3.14.3

#Importación de funciones.py
from funciones import *

tiposSangre=mostrarTiposSangre()
lugaresDonar=crearDiccionarioLugares()

def analizarEdadDonarAux(pfecha):
    """
    Funcionamiento: Evalúa si una persona puede donar sangre según su fecha de nacimiento.
    Entrada: pfecha (str) con fecha de nacimiento en formato dd/mm/aaaa.
    Salida: str con mensaje de elegibilidad o "Fecha inválida".
    """
    resultado = analizarEdadDonar(pfecha)
    if resultado == False:
        return "Fecha inválida"
    elif resultado >=18:
        return "Dado su fecha de nacimiento usted ya puede ser donador"
    else:
        return "Dado su fecha de nacimiento usted aún no puede ser donador"

def imprimirLugarNacimiento(pcedula):
    """
    Funcionamiento: Construye un mensaje con lugares de donación según la provincia de nacimiento.
    Entrada: pcedula (str) con cédula en formato #-####-####.
    Salida: str con mensaje de lugares de donación.
    """
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
    """
    Funcionamiento: Valida el peso y devuelve un mensaje apropiado.
    Entrada: ppeso (str) o valor convertible a entero.
    Salida: str con mensaje de validación de peso.
    """
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
    """
    Funcionamiento: Genera un mensaje de compatibilidad de donación e información del tipo de sangre.
    Entrada: ptipo (str) con tipo de sangre válido.
    Salida: str con mensaje de compatibilidad e información adicional.
    """
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
    """
    Funcionamiento: Sugiere un video si el tipo de sangre es A+ o A-.
    Entrada: ptipo (str) con tipo de sangre.
    Salida: str con recomendación de video o cadena vacía.
    """
    if ptipo == "A+" or ptipo == "A-":
        return ("Le recomendamos ver el video de:\n"
                "Particularidades de la sangre tipo A: "
                "Responde diferente al estrés según la ciencia.")
    return ""

def insertarDonadorAux(pmatrizD,pdatos):
    """
    Funcionamiento: Inserta un donador en la matriz y guarda el archivo si se inserta.
    Entrada: pmatrizD (list), pdatos (list) con datos del donador.
    Salida: bool True si inserta, False si la cédula ya existe.
    """
    inserto= insertarDonador(pmatrizD,pdatos)
    if inserto == False:
        return False
    guardarArchivo(pmatrizD)
    return True

def insertarDonadorMostrar(pmatrizD,pcedula,pnombre,pfecha,psangre,psexo,ppeso,ptelefono,pcorreo):
    """
    Funcionamiento: Valida datos de entrada y prepara el registro de donador.
    Entrada: pmatrizD (list), pcedula (str), pnombre (str), pfecha (str), psangre (str), psexo (str), ppeso (str), ptelefono (str), pcorreo (str).
    Salida: list con datos del donador si se inserta, o str con mensaje de error.
    """
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
    """
    Funcionamiento: Valida los datos para actualizar un donador.
    Entrada: pnombre (str), ptelefono (str), pfecha (str), psangre (str), ppeso (str).
    Salida: list con datos si son válidos, o str con mensaje de error.
    """
    if pnombre=="":
        return "Debe ingresar un nombre valido."
    if validarTelefono(ptelefono)==False:
        return "El teléfono debe tener el formato ####-#### y comenzar con 2,4,6,7,8 o 9."
    if validarFecha(pfecha)==False:
        return "La fecha debe tener el formato dd/mm/yyyy y ser válida."
    if psangre not in mostrarTiposSangre():
        return "El tipo de sangre debe ser O+, O-, A+, A-, B+, B-, AB+ o AB-."
    if validarPeso(ppeso)==False:
        return "El peso debe ser mayor o igual a 50 kg y menor o igual a 120 kg."
    return [pnombre,ptelefono,pfecha,psangre,ppeso]
        
def actualizarDonadorMostrar(matrizDonadores,pcedula,pnombre,ptelefono,pfecha,psangre,ppeso):
    """
    Funcionamiento: Valida cédula, busca al donador y actualiza sus datos.
    Entrada: matrizDonadores (list), pcedula (str), pnombre (str), ptelefono (str), pfecha (str), psangre (str), ppeso (str).
    Salida: True si se actualiza, o str con mensaje de error.
    """
    if validarCedula(pcedula)==False:
        return "Debe ingresar una cédula válida"
    posicion = buscarCedula(matrizDonadores,pcedula)
    if posicion == -1:
        return "La persona con el número de cédula: "+pcedula+" no está registrado en la base de datos del Banco de Sangre aún."
    datos=actualizarDonadorAux(pnombre,ptelefono,pfecha,psangre,ppeso)
    if type(datos)==str:
        return datos
    actualizarDonador(matrizDonadores,posicion,datos)
    guardarArchivo(matrizDonadores)
    return True
    
def eliminarDonadorAux(matrizDonadores,pcedula,pjustificacion):
    """
    Funcionamiento: Valida la existencia del donador y la justificación de eliminación.
    Entrada: matrizDonadores (list), pcedula (str), pjustificacion (str).
    Salida: True si la validación es correcta, o str con mensaje de error.
    """
    if validarCedula(pcedula)==False:
        return "Debe ingresar una cédula válida"
    posicion = buscarCedula(matrizDonadores,pcedula)
    if posicion == -1:
        return "La persona con el número de cédula: "+pcedula+" no está registrado en la base de datos del Banco de Sangre aún."
    if pjustificacion=="":
        return "Debe ingresar una justificación"
    return True

def eliminarDonadorMostrar(matrizDonadores,pcedula,pjustificacion,pconfirmar):
    """
    Funcionamiento: Verifica la eliminación y borra el donador si se confirma.
    Entrada: matrizDonadores (list), pcedula (str), pjustificacion (str), pconfirmar (bool).
    Salida: str con resultado de la operación o mensaje de cancelación.
    """
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
    """
    Funcionamiento: Valida y agrega un lugar de donación a la provincia indicada.
    Entrada: plugaresDonar (dict), pprovincia (str), plugar (str).
    Salida: str con mensaje de éxito o error.
    """
    if pprovincia not in mostrarProvincias():
        return "Debe seleccionar una provincia válida"
    if plugar.strip()=="":
        return "Debe ingresar un lugar válido"
    insertar= insertarLugar(plugaresDonar,pprovincia,plugar)
    if insertar == False:
        return "El lugar ya está registrado en esa provincia."
    return "Lugar agregado correctamente."

def generarDonadoresAux(pmatrizD,pcantidad):
    """
    Funcionamiento: Genera donadores aleatorios hasta alcanzar la cantidad deseada y guarda el archivo.
    Entrada: pmatrizD (list), pcantidad (int).
    Salida: str con mensaje de resultados de generación.
    """
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

def opcionReporteProvincia(pprovincia):
    """
    Funcionamiento: Genera un reporte de donadores por provincia seleccionada.
    Entrada: pprovincia (str) con el nombre de la provincia.
    Salida: str con confirmación del reporte, "Provincia inválida." o False.
    """
    provincias=mostrarProvincias()
    numeroProvincia=0
    for provincia in provincias:
        if provincias[provincia]==pprovincia:
            numeroProvincia = provincia
    if numeroProvincia==0:
        return "Provincia inválida."
    matrizDonadores = cargarArchivo()
    reporte=generarReporteDonadoresProvincia(matrizDonadores,numeroProvincia)
    if reporte:
        return "Reporte creado satisfactoriamente"
    else:
        return False

def reporteRangoEdad(pedadInicial,pedadFinal):
    """
    Funcionamiento: Valida el rango de edad y genera un reporte según el rango.
    Entrada: pedadInicial (str), pedadFinal (str).
    Salida: str con confirmación del reporte, mensaje de error o False.
    """
    try:
        edadInicial = int(pedadInicial)
    except:
        return "Debe ingresar una edad inicial válida."
    if edadInicial < 18 or edadInicial > 65:
        return "La edad inicial debe estar entre 18 y 65 años."
    if pedadFinal=="":
        edadFinal=edadInicial
    else:
        try:
            edadFinal=int(pedadFinal)
        except:
            return "Debe ingresar una edad final válida."
        if edadFinal < 18 or edadFinal > 65:
            return "La edad final debe estar entre 18 y 65 años."
        if edadFinal < edadInicial:
            return "La edad final no puede ser menor que la inicial."
        matrizDonadores = cargarArchivo()
        reporte=generarReporteRangoEdad(matrizDonadores,edadInicial,edadFinal)
        if reporte:
            return "Reporte creado satisfactoriamente"
        else:
            return False

def reporteListaDonadores():
    """
    Funcionamiento: Genera un reporte con el listado de todos los donadores.
    Entrada: Ninguna.
    Salida: str con confirmación si el reporte se creó, o mensaje de fallo.
    """
    matrizDonadores = cargarArchivo()
    reporte=generarReporteListaDonadores(matrizDonadores)
    if reporte:
        return "Reporte creado satisfactoriamente"
    else:
        return "Reporte no creado."

def reporteDonar(ptipo):
    """
    Funcionamiento: Genera un reporte de donadores que pueden donar según su tipo de sangre.
    Entrada: ptipo (str) con tipo de sangre.
    Salida: str con confirmación del reporte, mensaje de error o "Reporte no creado.".
    """
    matrizDonadores = cargarArchivo()
    if ptipo not in tiposSangre:
        return "Debe ingresar un tipo de sangre válido."
    reporte=generarReportePuedeDonar(matrizDonadores,ptipo)
    if reporte:
        return "Reporte creado satisfactoriamente."
    else:
        return "Reporte no creado."

def reporteRecibeDe(ptipo):
    """
    Funcionamiento: Genera un reporte de donadores que reciben de un tipo de sangre.
    Entrada: ptipo (str) con tipo de sangre.
    Salida: str con confirmación del reporte, mensaje de error o False.
    """
    matrizDonadores = cargarArchivo()
    if ptipo not in tiposSangre:
        return "Debe ingresar un tipo de sangre válido."
    reporte=generarReporteRecibeDe(matrizDonadores,ptipo)
    if reporte:
        return "Reporte creado satisfactoriamente."
    else:
        return False

def reporteMujeresO():
    """
    Funcionamiento: Genera un reporte de mujeres donantes de tipo O.
    Entrada: Ninguna.
    Salida: str con confirmación del reporte o False.
    """
    matrizDonadores = cargarArchivo()
    reporte=generarReporteMujeresDonantes(matrizDonadores)
    if reporte:
        return "Reporte creado satisfactoriamente."
    else:
        return False
    
def reporteNoActivo():
    """
    Funcionamiento: Genera un reporte de donadores no activos.
    Entrada: Ninguna.
    Salida: str con confirmación del reporte o mensaje de fallo.
    """
    matrizDonadores = cargarArchivo()
    reporte= generarReporteNoActivo(matrizDonadores)
    if reporte:
        return "Reporte creado satisfactoriamente"
    else:
        return "Reporte no creado."

def reporteLugares():
    """
    Funcionamiento: Genera un reporte de lugares de donación.
    Entrada: Ninguna.
    Salida: str con confirmación del reporte o mensaje de fallo.
    """
    matrizDonadores = cargarArchivo()
    reporte=generarReporteLugaresDonacion(matrizDonadores)
    if reporte:
        return "Reporte creado satisfactoriamente."
    else:
        return "Reporte no creado."

def reporteTipoProvincia(ptipo,pprovincia):
    """
    Funcionamiento: Genera un reporte de donadores por tipo de sangre y provincia.
    Entrada: ptipo (str), pprovincia (str).
    Salida: str con confirmación del reporte, mensaje de error o False.
    """
    if ptipo not in tiposSangre:
        return "Debe ingresar un tipo de sangre válido."
    provincias=mostrarProvincias()
    numeroProvincia=0
    for provincia in provincias:
        if provincias[provincia]==pprovincia:
            numeroProvincia=provincia
    if numeroProvincia==0:
        return "Provincia inválida. Intente nuevamente."
    matrizDonadores=cargarArchivo()
    reporte=generarReporteTipoProvincia(matrizDonadores,ptipo,numeroProvincia)
    if reporte:
        return "Reporte creado satisfactoriamente."
    else:
        return False