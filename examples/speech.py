'''
    Description:
    Perform voice operations in Spanish with Python.

    Author: AlejandroV
    Version: 0.0.3
    Video: youtube.com/avmmodules
'''
import AVMSpeechMath as sm
import speech_recognition as sr
import pyttsx3

# initialize
r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    '''
        here, virtual assistant can say something
    '''
    engine.say(text)
    engine.runAndWait()

try:
    with sr.Microphone() as source:
        print("Escuchando:")
        audio = r.listen(source)
        equation = r.recognize_google(audio, language='es-ES').lower()
        # deletes accents
        equation = equation.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
        print(equation)
        
        res = sm.getResult(equation)
        speak(res)

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")

except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))