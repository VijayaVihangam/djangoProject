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
import subprocess

import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()


def record_audio():
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        transcript = r.recognize_google(audio)
        print(transcript)


def say(text):
    subprocess.call(['say', text])


# say("Good Morning vijay, How can i help you")

d = '/Applications'
app = 'Spotify'
os.system('open ' + d + '/%s.app' % app.replace(' ', '\ '))
say('opening Spotify')

app = 'Trello'
os.system('open ' + d + '/%s.app' % app.replace(' ', '\ '))
say('opening Trello')

app = 'Webex'
os.system('open ' + d + '/%s.app' % app.replace(' ', '\ '))
say('opening Webex')

app = 'VLC'
os.system('open ' + d + '/%s.app' % app.replace(' ', '\ '))
say('opening VLC')

app = 'Microsoft Outlook'
os.system('open ' + d + '/%s.app' % app.replace(' ', '\ '))
say('opening Microsoft Outlook')


def there_exists(params):
    for param in params:
        if param in voice_data:
            return True


if there_exists(["check my instagram", "open my instagram", "open instagram"]):
    url = 'https://instagram.com'
    webbrowser.get().open(url)
    say("opening instagram")

records = []
apps = os.listdir(d)
for app in apps:
    record = {}
    record['voice_command'] = 'open ' + app.split('.app')[0]
    record['sys_command'] = 'open ' + d + '/%s' % app.replace(' ', '\ ')
    records.append(record)


if __name__ == '__main__':
    while 1:
        voice_data = record_audio()
        say(voice_data)
