#Elaborado por: Arina Tarasova, Hilary Aguilar
#Fecha de creación: 12/05/2026 01:30 pm
#Última modificación:
#Versión: 3.14.3

#Importación de librerias
import re
from datetime import datetime
import pickle

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