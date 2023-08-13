import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyjokes
import time

from config import *
from queries.browserQueries import openWebsite

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
        if "wikipedia" in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        # fun bonus
        elif 'thank you' in query:
            speak('your welcome !')
        elif "stop listening" in query:
            speak("How many seconds would you like me to stop listening")
            answer = takeCommand().lower()
            answer = int(answer)
            time.sleep(answer)
            speak('Listening again...')
        # websites
        elif 'open youtube' in query:
            speak("Here you go")
            openWebsite(youtube)
        elif 'open stack overflow' in query:
            speak("Happy coding")
            openWebsite(stackoverflow)
        elif 'open github' in query:
            speak("Opening github")
            openWebsite(github)
        elif 'tell me a joke' in query:
            speak("Let me see")
            joke = pyjokes.get_joke()
            speak(joke)
        else: 
            pass