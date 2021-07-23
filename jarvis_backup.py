import speech_recognition as sr
from time import ctime
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
import pyttsx3
import pyaudio
import audioop

r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def jarvis_speak(audio):
    engine.say(audio)
    engine.runAndWait()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            jarvis_speak(ask)
        text = r.listen(source)
        voice_data2 = ""
        del voice_data2
        try:
            voice_data2 = r.recognize_google(text)
        except sr.UnknownValueError:
            jarvis_speak("Sorry, I did not get that")
            return "none"
        except sr.RequestError as e:
            jarvis_speak("Sorry, My Speech service is down now")
            return "none"
        except sr.Microphone as me:
            jarvis_speak("Say it again")
            return "none"

        return voice_data2.lower()


def jarvis_respond(voice_data_rspnd):
    url = ""
    location = ""
    search = ""
    greet = ""
    greetings = ""

    del url
    del location
    del search
    del greetings
    del greet

    if there_exists(["hey", "hi", "hello", "hai"]):
        greetings = ["hey, how can I help you " + "vijay", "hey, what's up? " + "vijay",
                     "I'm listening " + "vijay", "how can I help you? " + "vijay",
                     "hello " + "vijay"]
        greet = greetings[random.randint(0, len(greetings) - 1)]
        jarvis_speak(greet)
    if there_exists(["who are you", "what is your name", "what's your name", "tell me your name"]):
        jarvis_speak("My name is loki, I'm your assistant ")
    if there_exists(["what time is it", "what is the time now", "current time", "time please", "what's the time now"]):
        jarvis_speak(ctime())
    if there_exists(["google it", "search in google", "find in google", "open google", "check in google"]):
        search = record_audio('what should i search on google')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        jarvis_speak("here is what i found for " + search)

    if there_exists(["check my facebook", "open my facebook", "open faceboook"]):
        url = 'https://facebook.com'
        webbrowser.get().open(url)
        jarvis_speak("opening facebook")

    if there_exists(["check my instagram", "open my instagram", "open instagram"]):
        url = 'https://instagram.com'
        webbrowser.get().open(url)
        jarvis_speak("opening instagram")

    if there_exists(["check my twitter", "open my twitter", "open twitter"]):
        url = 'https://twitter.com/home'
        webbrowser.get().open(url)
        jarvis_speak("opening twitter")

    if there_exists(["find the location", "open maps"]):
        location = record_audio("what is the location")
        url = "https://google.nl/maps/place/" + location + "/&amp;"
        webbrowser.get().open(url)
        jarvis_speak("here is the location for " + location)
        rmsTemp = 0
        chunk = 1024
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=chunk)
        stream.read(chunk)

    if there_exists(["exit", "goodbye", "quit", "bye jarvis"]):
        jarvis_speak("going offline")
        exit()

    if there_exists(["wake up loki", "loki", "hey loki", "hi loki", "loki are you there?"]):
        jarvis_speak("hello Vijay, How can i help you!")


# def jarvis_speak(audio_string):

def jarvis_speak2(audio_string):
    tts = gTTS(text=audio_string, lang='en', slow=False)
    rndm = str(random.randint(1, 10000000))
    audio_file = 'jarvis-audio' + rndm + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    # engine.say(audio_file)
    print(audio_string)
    os.remove(audio_file)
    del audio_file
    del audio_string


def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True


time.sleep(1)
# jarvis_speak('Hi, I am Jarvis. How can i help you today')
while 1:
    voice_data = record_audio()
    jarvis_respond(voice_data)
