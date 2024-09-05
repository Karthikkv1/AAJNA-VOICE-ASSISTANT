import random
import pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def rock():
    you = int(input("Please enter your choice:- \n 1-Rock \n2-Paper \n3-Scissor"))
    shapes ={1:'rock',2:'paper',3:'scissor'}
    if you not in shapes:
        print("Please enter a valid number")
        exit()
    comp=random.randint(1,3)
    print("you choose",you)
    print("computer choose",comp)
    if(you==1)and (comp==3) or (you==2) and (comp==1) or (you==3) and (comp==2):
        speak("Congratulations you won!")
    elif(you==comp):
        speak("Match tied")
    else:
        speak("You loose")            