import speech_recognition as sr
import pocketsphinx
import os

#Initializing the recognizer
r = sr.Recognizer()

def listen():
    while(1):
        try:
            #using microphone as source of input
            with sr.Microphone() as source:

                #prepar recognizer
                r.adjust_for_ambient_noise(source, duration=0.2)
                
                print("say something!!")
                
                #taking audio input
                audio = r.listen(source)
                print("He thought you said something..." + r.recognize_sphinx(audio))

                #using google to process audio
                myText = r.recognize_google(audio)
                return myText
                
        except sr.UnknownValueError:
            print("Google's speech recognition could not understand the audio.")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service, Reason: {0}".format(e))

def output_text(text):
    f = open("output.txt", "a")
    f.write(text)
    f.write("\n")
    f.close()
    return

while(1):
    text = listen()
    output_text(text)

    print("wrote text")