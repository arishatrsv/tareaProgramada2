#Elaborado por: Arina Tarasova, Hilary Aguilar
#Fecha de creación: 12/05/2026 01:30 pm
#Última modificación:
#Versión: 3.14.3

#Importación de librerias
import pickle
import re

def mostrarTiposSangre():
    tipos = ("O+","O-","A+","A-","B+","B-","AB+","AB-")
    return tipos
def crearDiccionarioLugares():
    diccionarioLugares = {1:["Banco Nacional de Sangre","Hospital México"],
    2:["Hospital San Rafael"],
    3:["Hospital Max Peralta"],
    4:["Hospital San Vicente de Paúl"],
    5:["Hospital La Anexión"],
    6:["Hospital Monseñor Sanabria"],
    7:["Hospital Tony Facio"]}
    return diccionarioLugares

def guardarArchivo(pmatriz):
    archivo=open("donadores.txt","wb")
    pickle.dump(pmatriz,archivo)
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

def insertarDonador(pmatriz,pdonador):
    pmatriz.append(pdonador)
    return pmatriz

def buscarCedula(pmatriz,pcedula):
    for i in range(len(pmatriz)):
        if pmatriz[i][1]==pcedula:
            return i
    else:
        return -1

def actualizarPeso(pmatriz,pcedula,pnuevoPeso):
    posicion=buscarCedula(pmatriz,pcedula)
    if not posicion == -1:
        pmatriz[posicion][5]=pnuevoPeso
        return pmatriz
    return []

def validarTelefono(ptelefono):
    if re.match(r"^[246789]{1}\d{3}-\d{4}$",ptelefono):
        return True
    else:
        return False
    
from datetime import datetime

def buscarCedula(pdonadores,pcedula):
    """Funcionamiento: Busca una cédula dentro de la matriz.
    Entradas:
    pmatriz (list)
    pcedula (str)
    Salidas: True o False
    """
    for donador in pdonadores:
        cedula = donador[1]
        if cedula == pcedula:
            return True
        return False
    
def insertarDonador(pdonadores,pdatos):
    cedula = pdatos[1]
    existe = buscarCedula(pdonadores,cedula)
    if existe == True:
        return False
    pdonadores.append(pdatos)
    return True

def obtenerProvincias(pcedula):
    provincia = int(pcedula[0])
    return provincia

def validarCedula(pcedula):
    if re.match(r"^[1-9]-\d{4}-\d{4}$",pcedula): #Valida que el formato de cedula sea #-####-#### 
        return True
    return False

def validarFecha(pfecha):
    try:
        datetime.strptime(pfecha,"%d/%m/%Y") #Verifica que el str es una fecha con el formato correcto
        return True
    except:
        return False

#def validarCorreo():
#def validarTelefono():
#def validarPeso():  

