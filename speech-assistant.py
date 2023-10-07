import speech_recognition as sr
import webbrowser
import os
import random
import pyttsx3
import pygame
import time
from time import ctime

r = sr.Recognizer()

# Initialize pyttsx3 globally
engine = pyttsx3.init()

# Initialize pygame
pygame.mixer.init()


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            alexa_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            alexa_speak('Sorry, I did not get that')
        except sr.RequestError:
            alexa_speak('Sorry, my speech service is not available')
        return voice_data


def alexa_speak(audio_string):
    engine.say(audio_string)
    engine.runAndWait()
    print(audio_string)


def respond(voice_data):
    if 'what is your name' in voice_data:
        alexa_speak('My name is Alexa')
    if 'what time is it' in voice_data:
        alexa_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('what do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        alexa_speak('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('what is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        alexa_speak('Here is the location of ' + location)
    if 'exit' in voice_data:
        exit()


time.sleep(1)
alexa_speak('How can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
