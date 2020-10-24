import  pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
engine=pyttsx3.init('Sapi5')

voices=engine.getproperty('voices')
#print(voices[0].id)
engine.setproperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def WishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0  and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening!")
        speak("I am Jarvis sir.please tell how may I help you")
def takeCommand():
    #It takes microphone input from user and returns string output
    r=sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening--------")
        sr.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing----------")
        query=r.recognize_google(audio,language-'en-in')
        print(f"User said:{query}\n")
    except exception as e:
        #print(e)
        print("Say that again please......")
        return "None"
    return query
    if __name__ == "__main__":
        wishMe()
        while true:
            query=takeCommand().lower()
            #Logic for executing tasks based on query
    if 'wikipedia'in query:
        speak('searching wikipedia....')
        query=query.replace("wikipedia"," ")
        results = wikipedia.summary(query,sentences=2)
        speak("according to wikipedia")
        print(results)
        speak(results)
    elif'open You tube'in query:
        webbrowser.open("Youtube.com")
    elif'open google'in query:
        webbrowser.open("Google.com")
    elif'the time'in query:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"sir,the time is{strtime}")
    elif'open code'in query:
        codepath = target
        os.startfile(codepath)

