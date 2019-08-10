import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say Something")
    audio = r.listen(source)

try:
    print("You Said ", r.recognize_google(audio))
except:
    print("Sorry, could not understand")
