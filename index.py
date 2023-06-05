# pip install SpeechRecognition
# pip install pyttsx3
import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
tts = pyttsx3.init()

#Set a volume
tts.setProperty('volume',10.0)

while True:
#Stream instance using the microphone as source:
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)#this is to make it stop freezing
        audio = recognizer.listen(source)
#transcribe the audio from the live stream:
    try:
        text = recognizer.recognize_google(audio)
        print("Riz: " + text)
        #Play the speech
        tts.say(text)
        tts.runAndWait()
    except:
        print("Bad Audio")

