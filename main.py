import speech_recognition as sr
import pyttsx3
import pyaudio
import wave

# Initialize speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()

# Define wake word and responses
wake_word = "AAJNA"
responses = {
    "hello": "Hello there! How can I help you today?",
    "how are you": "I'm doing well, thank you for asking.",
    "what is your name": "My name is AAJNA.",
    "tell me a joke": "Sure, here's a joke: Why did the chicken cross the road? To get to the other side!",
}

# Function to listen for speech and return recognized text
def listen_for_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Main loop
while True:
    text = listen_for_speech()

    if text and wake_word in text.lower():
        user_query = text.replace(wake_word, "").strip()
        print("User query:", user_query)

        if user_query in responses:
            speak(responses[user_query])
        else:
            speak("I don't have information about that yet. Please try another question.")