'''
    Description:
    Perform voice operations in Spanish with Python.

    Author: AlejandroV
    Version: 0.0.3
    Video: youtube.com/avmmodules
'''
from math import *

def getEquation(equation):
    '''
        Replace words (without accents) for mathematical signs.
    '''
    obj = {"cuanto es":"", "mas":"+", "menos":"-", "entre":"/", "por ":"* ", "x":"*", "abre parentesis":"(", "cierra parentesis":")", "negativo":"-", "elevado a la":"**", "a porcentaje":"", "y":"", "la":"", "el":"", "raiz de":"", ",":""}
    objKeys = list(obj.keys())
    objValues = list(obj.values())

    for i in range(len(objKeys)):
        if objKeys[i] in equation:
            equation = equation.replace(objKeys[i], objValues[i])
    return equation.strip()

def transformNumbers(equation):
    '''
        If the voice gets numbers with letters instead of numbers, we replace them here.
    '''
    nums = {"cero": "0", "uno": "1", "dos": "2", "tres": "3", "cuatro": "4", "cinco": "5", "seis": "6", "siete": "7", "ocho": "8", "nueve": "9", "diez": "10", "once": "11", "doce": "12", "trece": "13", "catorce": "14", "quince": "15","dieciseis": "16", "diecisiete": "17", "dieciocho": "18", "diecinueve": "19","veinte": "20", "treinta": "30", "cuarenta": "40", "cincuenta": "50", "sesenta": "60", "setenta": "70", "ochenta": "80", "noventa": "90", "cien": "100", "mil": "1000", "millon": "1000000", "billon": "1000000000", "trillon": "1000000000000", "cuatrillon": "1000000000000000", "quintillon": "1000000000000000000", "sextillon": "1000000000000000000000"}
    numsKeys = list(nums.keys())
    numsValues = list(nums.values())
    
    eqSplit = equation.split()
    
    for i in range(len(eqSplit)):
        for j in range(len(numsKeys)):
            if eqSplit[i] == numsKeys[j]:
                eqSplit[i] = eqSplit[i].replace(eqSplit[i], numsValues[j])
                break
    return ("".join(eqSplit))
    
def getResult(equation):
    '''
        Get result calling other functions.
    '''
    eq = transformNumbers(getEquation(equation))
    
    try:
        if "raiz de" in equation:
            a = float(eq)
            ev = eval('sqrt(a)', {'__builtins__': None}, {'a': a, 'sqrt': sqrt})

        elif "a porcentaje" in equation:
            ev = "{:.1%}".format(float(eq))

        else:
            ev = eval(eq)
        
        return "El resultado es  {:,d}".format(int(ev))
    except:
        return "Unable to evaluate equation"