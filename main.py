import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser

from config import *

# setup
auraEngine = pyttsx3.init('sapi5')
voices = auraEngine.getProperty('voices')
auraEngine.setProperty('voice', voices[1].id)


def speak(audio):
    auraEngine.say(audio)
    auraEngine.runAndWait()

def startup():
    timeofday = int(datetime.datetime.now().hour)
    if timeofday>=0 and timeofday<12:
        speak("Good Morning !")
    
    elif timeofday>=12 and timeofday<18:
        speak("Good Afternoon !")
    
    else:
        speak("Good Evening !")

    speak(f"I am {assistantName}, how can I help you?")

def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-IE')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
     
    return query

if __name__ == "__main__":
    startup()
    
    active = True
    while active:
        query = takeCommand().lower()

        # basic query searching
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            speak(results)
        # fun bonus
        elif 'thank you' in query:
            speak('your welcome !')

        # websites
        elif 'open youtube' in query:
            speak("Here you go")
            webbrowser.open('https://www.youtube.com')
        elif 'open stack overflow' in query:
            speak("Happy coding")
            webbrowser.open('https://www.stackoverflow.com')
