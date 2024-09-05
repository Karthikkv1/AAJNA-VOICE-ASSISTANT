from random import randint
import pyttsx3 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def guess():
    start=1
    end=1000
    value=randint(start,end)
    print("The computer choose a number between",start,"and",end)
    guess=None
    while guess != value:
        text=input("Guess the number:")
        guess=int(text)
        if guess < value:
            speak("The number is higher")
        elif guess > value:
            speak("The number is lower")    
    speak("Congratulations! you won")