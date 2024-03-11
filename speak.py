<<<<<<< HEAD
# pip install pyttsx3

import pyttsx3
def speak(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-70)
    engine.say(text)
    engine.runAndWait()

||||||| parent of 1ed050c (Initial commit)
# pip install pyttsx3

import pyttsx3
def speak(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-70)
    engine.say(text)
    engine.runAndWait()

=======
# pip install pyttsx3

import pyttsx3
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')  
    rate = engine.getProperty('rate')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', rate-70)
    engine.say(text)
    engine.runAndWait()

>>>>>>> 1ed050c (Initial commit)
