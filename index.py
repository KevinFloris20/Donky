# pip install SpeechRecognition
import speech_recognition as sr

recognizer = sr.Recognizer()

while True:
#Stream instance using the microphone as source:
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)#this is to make it stop freezing
        audio = recognizer.listen(source)
#transcribe the audio from the live stream:
    try:
        text = recognizer.recognize_google(audio)
        print("Riz: " + text)
    except:
        print("Bad Audio")