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

def actualizarDonadorAux(pnombre,ptelefono,pfecha,psangre,ppeso):
    while True:
        if validarNombre(pnombre)==False:
            print("El nombre debe contener al menos 2 caracteres.")
            return False
        if validarTelefono(ptelefono)==False:
            print("El teléfono debe tener el formato ####-#### y comenzar con 2,4,6,7,8 o 9.")
            return False
        if validarFecha(pfecha)==False:
            print("La fecha debe tener el formato dd/mm/yyyy y ser válida.")
            return False
        if validarTipoSangre(psangre)==False:
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