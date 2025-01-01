# pip install  pyjokes

import pyjokes

joke = pyjokes.get_joke()
print(joke)

#pip install pyttsx3

import pyttsx3

engine = pyttsx3.init()
engine.say("Im python")
engine.runAndWait()
