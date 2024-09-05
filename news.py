from  GoogleNews import GoogleNews
import pandas as pd
import pyttsx3    #Python text to speech module


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def news():
    news = GoogleNews(period='1d')     #Period=1day
    news.search("India")
    result=news.result()
    data=pd.DataFrame.from_dict(result)
    data=data.drop(column=["img"])
    data.head()
    

    for i in result:
        speak(i["title"])
