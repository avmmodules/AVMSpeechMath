'''
    Description:
    Perform voice operations in Spanish with Python.

    Author: AlejandroV
    Version: 0.0.5
'''
import AVMSpeechMath as sm

def calculate(eq):
    ''' Get result '''
    print(sm.getResult(eq))

# basic operations
calculate("Cuánto es dos más dos") # prints 'El resultado es 4'
calculate("Cuánto es 100 menos 74") # prints 'El resultado es 26'
calculate("Cuánto es cinco por 4000") # prints 'El resultado es 20,000'
calculate("Cuánto es treinta entre seis") # prints 'El resultado es 5'

# complex operations
calculate("Cuánto es dos elevado a la 7") # prints 'El resultado es 128'
calculate("Raiz de cien") # prints 'El resultado es 10'
calculate("(1+2+3+4)/2") # prints 'El resultado es 5'