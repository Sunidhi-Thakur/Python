import pyttsx3
from datetime import datetime
import speech_recognition as sr


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("Good Morning Sunidhi")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sunidhi")
    else:
        speak("Good Evening Sunidhi")
    
    speak("I am Kanchana. Your Voice Assistant")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")


    except Exception as e:
        print(e)

        print("Say that Again please...")
        return "None"

    return query


if __name__ == "__main__":
    wishMe()
    takeCommand()