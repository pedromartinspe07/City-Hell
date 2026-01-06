import speech_recognition as sr
import os

r = sr.Recognizer()
mic = sr.Microphone()

while True:
    with mic as source:
        print("Ouvindo...")
        audio = r.listen(source)

    try:
        texto = r.recognize_google(audio, language="pt-BR")
        print("Você:", texto)

        if "abrir navegador" in texto:
            os.system("firefox &")

        if "desligar sistema" in texto:
            os.system("shutdown now")

    except:
        pass