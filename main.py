
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import requests
from ecapture import ecapture as ec

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am heisenberg, your Voice Assistant Sir. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('suhail3519qureshi@gmail.com', '99279763')
    server.sendmail('suhail3519qureshi@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open college website' in query:
            webbrowser.open("http://jamiahamdard.edu/")

        elif 'open covid cases' in query:
            webbrowser.open("https://www.covid19india.org/")

        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com/")

        elif 'open Amazon' in query:
            webbrowser.open("https://www.amazon.in/")

        elif 'open twitter' in query:
            webbrowser.open("https://twitter.com/")

        elif 'open icloud' in query:
            webbrowser.open("https://www.icloud.com/")

        elif 'open Goverment jobs in india' in query:
            webbrowser.open("sarkari-naukri.in")

        elif 'today news' in query:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India')
            time.sleep(6)

        elif " Open camera" in query or "take a photo" in query:
            ec.capture(0,"robo camera","img.jpg")
            speak("Opening Camera")

        elif 'play music' in query:
            music_dir = 'D:\MUSIC Shagan'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")


        elif 'email to suhail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "suhail3519qureshi@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry  . I am not able to send this email")

        elif "log off" in query or "shutdown" in query:
            speak("Ok , your pc will log off in 10 seconds make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])