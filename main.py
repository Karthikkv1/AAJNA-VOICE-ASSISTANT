import pyttsx3    #Python text to speech module
import speech_recognition as sr
import datetime
import os
import random
import wikipedia
import webbrowser #To open websites
import pyjokes
import subprocess
import time
import pyautogui
import psutil
import winshell #To make recycle bin empty
from camera import *
# from cpu import *
import sys
import socket
import imdb
from news import news   #Including external news.py
from password import password #or from password import *
from calender import *
from rock_paper_scissor import *
from guess_the_number import *
from countdown_timer import *


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takeCommand(): #Take command from user
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...............")
        r.pause_threshold=1
        audio=r.listen(source,timeout=1,phrase_time_limit=10)
        try:
            print("Recognizing........")
            query = r.recognize_google(audio,language='en-In') #setted lanuage as english indian
            print(f"User Said:{query}\n")
        except Exception as e:
            speak("Enable to recognize your voice...............")
            return"None"
        return query


def username():
    speak("What should i call you sir?")
    uname=takeCommand()
    speak("Welcome Mister" + uname)
    speak("How can i help you,sir?")

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("I am your virtual assistant AAJNA")     


def cpu():
    usage=str(psutil.cpu_percent())
    speak("CPU is at" + usage)
    battery=str(psutil.sensors_battery())
    speak("CPU is at" + battery)
    
def movie():
    moviesdb = imdb.IMDb()
    speak("Please tell me the movie name sir")
    text = takeCommand()
    movies=moviesdb.search_movie(text)
    speak("Searching for" + text)
    if len(movies==0):
        speak("No results found")                   
    else:
        speak("I found these: ")
        for movie in movies:
            title = movie["title"]
            year=movie["year"]
            speak(f"{title}-{year}")
            info=movie.getID()
            movie=moviesdb.get_movie(info)
            rating=movie["rating"]
            plot=movie['plot outline']
            if year<int(datetime.datetime.now().strftime("%Y")):
                speak(f'{title} was released in {year} has IMDB ratings of {rating}.The plot summary of movie is {plot}')
                break
            else:
                speak(f'{title} will release in {year} has IMDB ratings of {rating}.The plot summary of movie is {plot}')
                break



if __name__=='__main__':
    wishMe()
    username()
    while True:
        order=takeCommand().lower()

        if 'how are you ' in order:
            speak("I am fine , Thank You")
            speak("How are you sir?")

        elif 'fine' in order or 'good' in order:
            speak("It's good to know that you are fine. ") 

        elif 'who i am' in order:
            speak('If you can talk then surely you are as human.')

        elif 'love' in order:
            speak('It is the 7th sense that destroy all other senses')

        elif 'who are you' in order:
            speak('I am your virtual assistant AAJNA.')

        elif 'I love you' in order:
            speak('Oh my god , thank you . I love you too. Anything i can help you with?')

        elif 'can i call you aajna' in order or 'will you be any valentine' in order:
            speak("I'm not sure about that,maybe you should give me some more time.")

        elif 'what is your name' in order:
            speak('I am given name as aajna from my developer karthik')

        elif 'open notepad' in order:
            npath="C:\\Program Files\\Git\\usr\\bin\\notepad\\notepad.txt"
            os.startfile(npath)
        
        elif 'play music' in order or 'paly songs' in order:
            music_dir="E:\\Songs\\New Folder"
            songs=os.listdir(music_dir)
            rd=random.choice(songs)
            os.startfile(os.path.join(music_dir,rd))

        elif 'wikipedia' in order:
            speak('Searching.....')
            order=order.replace("wikipedia","")
            results=wikipedia.summary(order,sentences=2)
            speak("According to wikipedia")
            speak(results)
        

        elif 'open google' in order:
            speak("here you go to google sir\n")
            webbrowser.open("google.com")

        elif 'open myntra' in order:
            speak("here you go to myntra sir. Happy Shopping \n")
            webbrowser.open("myntra.com")    


        elif 'open youtube' in order:
            speak("here you go to youtube sir.")
            webbrowser.open("youtube.com") 

        elif 'open amazon' in order:
            speak("here you go to amazon sir. Happy Shopping \n")
            webbrowser.open("amazon.in")

            
        elif 'open stackoverflow' in order:
            speak("here you go to Stack overflow. Happy Coding")
            webbrowser.open("stackoverflow.com")       

        elif "where is" in order:
            order=order.replace("where is","")
            location=order
            speak("Locating.................")
            speak(location)
            webbrowser.open("https://www.google.co.in/maps/place/"+location+"")


        elif "write a note" in order:
            speak("what should i write,sir?")
            note=takeCommand()
            file=open('jarvis.txt','w')
            speak("Sir, Should I include date and time as well?")
            sn=takeCommand()
            if 'yes' in sn or 'sure' in sn or 'yeah' in sn:
                strTime=datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(note)
                speak("Done Sir!")
            else:
                file.write(note)
                speak("Done Sir!")
    

        elif 'show note' in order:
            speak("Showing notes")
            file=open("jarvis.txt","r")
            print(file.read())
            speak(file.read(6))

        elif 'joke' in order:
            speak(pyjokes.get_joke(language="en",category="neutral"))

        elif 'the time' in order:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"well, the time is {strTime}")   

        elif 'shutdown' in order or 'turn off' in order:
            speak('Hold on a second sir! your system is on its way to shutdown')
            speak('Make sure all of your applications are closed')
            time.sleep(5)
            subprocess.call(['shutdown','/s'])    

        
        elif 'restart' in order:
            subprocess.call(['shutdown','/r'])

        elif 'hibernate' in order:
            speak('Hibernating............')
            subprocess.call(['shutdown','/h'])

        elif 'log off' in order or 'sign out' in order:
            speak('make sure all of your applications are closed before signing out sir')
            time.sleep(5)
            subprocess.call(['shutdown','/i'])


        elif 'switch window' in order:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.keyUp('alt')

        elif 'take a screenshot' in order or 'screenshot this' in order:
            speak('Sir,please tell me the name for this file.')
            name=takeCommand().lower()
            speak("Please hold the screen")
            time.sleep(3)
            img=pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("Screenshot captured sir!")

        elif 'cpu status' in order:
            cpu()                   

        elif 'empty recycle bin' in order:
            winshell.recycle_bin().empty(confirm=False,show_progress=False, sound=True)

        elif 'camera' in order:        
            cam()

        elif 'exit' in order or 'quit' in order:
            speak("Thank you for using me sir,have a good day")
            sys.exit()

        elif 'ip' in order:
            host=socket.gethostname()
            ip=socket.gethostbyname(host)
            speak("Your IP address is" + ip)

        elif 'bmi' in order:
            speak("Please tell your height in centimeters")
            height= takeCommand()
            speak("Please tell your weight in kilograms")
            weight=takeCommand()
            height=float(height)/100
            BMI=float(weight)/(height*height)
            speak("Your body mass index is" + str(BMI)) 
            if (BMI>0):
                if (BMI<=16):
                    speak("You are severly underweight")
                elif (BMI<=18.5):
                    speak("You are underweight")
                elif (BMI<=25):
                    speak("You are healthy")
                elif(BMI<=30):
                    speak("You are overweight")
                else:
                    speak("You are severly overweight")                       
            else:
                speak("Enter valid details")


        elif 'movie' in order:
            movie()

        elif 'news' in order:
            news()    

        elif 'password' in order:
            password()   

        elif 'calender' in order:
            show()  
        
        elif 'rock' in order:
            rock()


        elif 'guess' in order:
            guess()

        elif 'count' in order:
            count()        




