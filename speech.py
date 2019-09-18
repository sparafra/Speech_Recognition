import speech_recognition as sr
import win32com.client as wincl

# referenze libreria: https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst#speech-recognition-library-reference
speak = wincl.Dispatch("SAPI.SpVoice")

recognizer_instance = sr.Recognizer() # Crea una istanza del recognizer

while True:

    with sr.Microphone() as source:
        recognizer_instance.adjust_for_ambient_noise(source)

        print("Sono in ascolto... parla pure!")
        audio = recognizer_instance.listen(source)
        print("Ok! sto ora elaborando il messaggio!")
    try:
        text = recognizer_instance.recognize_google(audio, language="it-IT")
        text = text.lower()
        MiAttivo = "jarvis" in text
        if MiAttivo:
            print("Google ha capito: \n", text)
            text = text.replace("jarvis", "")
            speak.Speak(text)
        else:
            print("Non ti ho capito: \n", text)
            speak.Speak("Scusami, ma non ho capito bene")
    except Exception as e:
        print(e)