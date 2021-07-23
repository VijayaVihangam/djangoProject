import subprocess
import webbrowser
from datetime import datetime
import os
import time
import random
import pyjokes
import speech_recognition as sr
recognizer = sr.Recognizer()
mic = sr.Microphone()
d = '/Applications'


def record_voice(ask=False):
    text =''
    try:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            voice = recognizer.listen(source,timeout=9,phrase_time_limit=9)
            text = recognizer.recognize_google(voice)
            print(text.lower())

    except sr.UnknownValueError:
        say("Sorry, I did not get that")
        return 'None'
    return text.lower()


def say(text):
    subprocess.call(['say', text])


def assistant_process(human_voice):

    if human_voice in('hi','loki','hey loki','hello','hai','hello loki'):
        greetings = ["hey, how can I help you " + "vijay", "hey, what's up? " + "vijay",
                     "I'm listening " + "vijay", "how can I help you? " + "vijay",
                     "hello " + "vijay"]
        greet = greetings[random.randint(0, len(greetings) - 1)]
        say(greet)

    elif human_voice in("who are you","what is your name"):
        say('I am Loki your assistant')
        
    elif human_voice in ("what time is it", "what is the time now", "current time", "time please", "what's the time now"):
        say(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    elif human_voice in("google it", "search in google", "find in google", "open google", "check in google"):
        say('what should i search on google')
        search = record_voice()
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        say("here is what i found for " + search)

    elif human_voice in("check my facebook", "open my facebook", "open facebook","my facebook"):
        url = 'https://facebook.com'
        webbrowser.get().open(url)
        say("opening facebook")

    elif human_voice in("check my instagram", "open my instagram", "open instagram","my instagram"):
        url = 'https://instagram.com'
        webbrowser.get().open(url)
        say("opening instagram")

    elif human_voice in("check my twitter", "open my twitter", "open twitter","my twitter"):
        url = 'https://twitter.com/home'
        webbrowser.get().open(url)
        say("opening twitter")

    elif human_voice in("find the location", "open maps","search for location","search location","location please","location"):
        say("what is the location")
        location = record_voice()
        url = "https://google.nl/maps/place/" + location + "/&amp;"
        webbrowser.get().open(url)
        say("here is the location for " + location)

    elif human_voice in("trello","open trello",'trailer'):
        app = 'Trello'
        os.system('open ' + d + '/%s.app' % app.replace(' ', '\ '))
        say('opening Trello')

    elif human_voice in("spotify","open spotify","play music","music"):
        app = 'Spotify'
        os.system('open ' + d + '/%s.app' % app.replace(' ', '\ '))
        say('opening Spotify')

    elif human_voice in ("webex", "open webex", "webex","meeting","check my meetings"):
        app = 'Webex'
        os.system('open ' + d + '/%s.app' % app.replace(' ', '\ '))
        say('opening Webex')

    elif human_voice in ("vlc", "open vlc", 'vlc'):
        app = 'VLC'
        os.system('open ' + d + '/%s.app' % app.replace(' ', '\ '))
        say('opening VLC')

    elif human_voice in ("outlook", "open outlook", 'check email','open email','email','open mail','send mail'):
        app = 'Microsoft Outlook'
        os.system('open ' + d + '/%s.app' % app.replace(' ', '\ '))
        say('opening Email')

    elif human_voice in ("joke", "tell me a joke", "pyjoke","joke please","fun","make me laugh"):
        joke = pyjokes.get_joke(language="en", category="neutral")
        print(joke)
        say(joke)

    elif human_voice in("exit","goodbye","close","bye"):
        say('going offline')
        exit()


time.sleep(1)
while True:
    human_voice_1 = record_voice()
    assistant_process(human_voice_1)
    #say(human_voice_1)
