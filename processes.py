import saying
import name
import jokes
import googfind
import stock_data
import os
from gtts import gTTS
import re

def process(said):
    k=0
    print("Processing the string input")
    os.system("mpg123 voice_read.mp3")
    temp=said
    say=[]
    say=(temp.split(" "))
    if(say[0]=="say"):
        saying.saying(said)
        k=1
    if said in ("tell me your name", "what is your name","hey whats your name","I dont think we have been introduced yet", "whats your name","can I get your name","hey remind me of your name","hi who are you","whats your name","what can I call you","what would your name be","what are you named","what do you call yourself","can I have your name"):
        name.nname(said)
        k=1
    if said in ("tell me a good joke","make me laugh","tell me a joke","joke about something"):
        jokes.jokes(said)
        k=1
    if say[0]=="Google":
        googfind.googfind(said)
        k=1
    if said in ("tell me about a stock","can you tell me about a stock"," can you tell me about the stock","tell me about a stock"):
        stock_data.stock_data(said)
        k=1
    if k==0:
        text="sorry I do not know how to do that nor do I understand it"
        tts=gTTS(text=text,lang="en")
        tts.save("output.mp3")
        os.system("mpg123 error-126627.mp3")
        os.system("mpg123 output.mp3")
        os.remove("output.mp3")