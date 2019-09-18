import speech_recognition as sr
recognizer_instance = sr.Recognizer() # Crea una istanza del recognizer

wav = sr.AudioFile("E:\\05.wav") # formati riconosciuti: .aiff .flac .wav

with wav as source:
    recognizer_instance.pause_threshold = 1
    audio = recognizer_instance.listen(source)
    print("Ok! sto ora elaborando il messaggio!")
try:
    text = recognizer_instance.recognize_google(audio, language="it-IT")
    print("Google ha capito: \n", text)
except Exception as e:
    print(e)