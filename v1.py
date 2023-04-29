from processes import process
import speech_recognition as sr
import time
import pyttsx3


r = sr.Recognizer()


with sr.Microphone() as source:
    print("Speak now...")
    audio = r.listen(source, timeout=5, phrase_time_limit=5)#taking voice input
    try:
        print("Processing the voice input")
        said=r.recognize_google(audio)#converting audio input to text1
        said=str(said)
    except:
        print("please try again")

try:
    print("You said: " + said)
    process(said)#we pass the i/p string to process it
    
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
