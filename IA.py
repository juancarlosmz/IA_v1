import pyttsx3 
import datetime
import speech_recognition as sr
import webbrowser as wb
import wikipedia
r = sr.Recognizer()
engine = pyttsx3.init()
audio = ''
global query
global source
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Hable ahora")
        audio = r.listen(source)
        query = r.recognize_google(audio, language='en-in')
        print('Buscando:',query)
        speak('Buscando:')
        speak(query)
    try:
        print(query)
        wishme(query)
    except Exception as e:
        print(e)
        speak("Repítelo por favor")
def tesxt(audio):
    engine.say(audio)
    engine.runAndWait()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%T:%M:%S")
    speak(Time)

def date(): 
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)

def wishme(query):
    
    speak("Procesando")
    print("Estas buscando: ")
    print(query)
    if 'time' in query:
        time()
    try:
        print("__name__ validando: ")
        print(__name__)
        if __name__ == "__main__":
            engine.say("Espera ")
            while True:
                print("---")
                query = query.lower()
                print(query)
                print('---')
                if 'busca' in query:
                    if 'youtube' in query:
                        chromepath = 'C:/Program Files/Google/Chrome/Application/Chrome.exe %s'
                        speak('Abriendo youtube')
                        wb.get(chromepath).open_new_tab('https://www.youtube.com')
                    if 'google' in query:
                        speak("Buscando en Google...")
                        query = query.replace("busca","")
                        query = query.replace("google","")
                        chromepath = 'C:/Program Files/Google/Chrome/Application/Chrome.exe %s'
                        wb.get(chromepath).open_new_tab('https://www.google.com/search?q='+query)
                    elif 'wikipedia' in query:
                        speak("Buscando en Wikipedia...")
                        query = query.replace("busca","")
                        query = query.replace("wikipedia","")
                        print(query)
                        result = wikipedia.summary(query, sentences=2)
                        print(result)
                        speak(result)
                elif 'offline' in query:
                    print("esto es :", query)
                engine.runAndWait()
                takeCommand()
    except:
        print("Saliendo")
        speak('Saliendo')
    else:
        print("no funciona")

with sr.Microphone() as source:
    print("Hable ahora")
    audio = r.listen(source)
    query = r.recognize_google(audio, language='en-in')
    print('Buscando:',query)
    speak('Buscando:')
    speak(query)
try:
    print(query)
    wishme(query)
except:
    print("No se reconoce su voz 1")
    takeCommand()
