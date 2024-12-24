# USe any python module and write a programe

import pyttsx3

# This is a simple python program to convert text to speech using pyttsx3 module
# pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.

engine = pyttsx3.init()
engine.say(" hell, This is ayuhs and this is my first program to convert text to speech using pyttsx3 module")
engine.runAndWait()

