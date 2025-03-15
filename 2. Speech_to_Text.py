# pip install pyaudio
# pip install SpeechRecognition

import speech_recognition as sr
def speech_text():
    r = sr.Recognizer() # To convert voice, Recognoizer is a class in speech_recognition
    m = sr.Microphone() # To read voice, Microphone is a class in speech_recognition

    while True: # it is read the voice when we speak continuously
        with sr.Microphone() as source:  # assigning the read voice to a variable source
            print("Speak................")
            audio = r.listen(source, timeout=10)   # listen is a function
            try:
                text = r.recognize_google(audio) # recognize_google is an API provided by google, can use google cloud also but it wont give much accuracy
                if text.lower() == 'stop':
                    break
                print("You Said : ",text)
            except:
                print("Did not hear anything")

speech_text()

# f=open('file_path', 'r')
# with open as abc => it is similar to above code