# Speech Recognition

# - How to convert text to speech
# - How to convert speech to text

# pip install pyttsx3

import pyttsx3

# create object
txt_sp = pyttsx3.init()   # init is a class inside the pyttsx3 package

voices = txt_sp.getProperty('voices')     # To change the male voice to female
txt_sp.setProperty('voice',voices[1].id)

# creating object for classes
text = input("Enter the text : ")

# say, runAndWait are functions
txt_sp.say(text)
txt_sp.runAndWait() # To wait until the speech gets converted into speech

