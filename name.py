import glob
from gtts import gTTS
import os

def nname(said):
    
    ''''
    name=str(said.split(" "))
    x=glob.glob('your*')
    y=' '.join(x)
    if((name.find(y)+1)!=0 or (name.find("name")+1)!=0 or (name.find("call")+1)!=0 or (name.find("speaking")+1)!=0):'''
    if said in ("tell me your name","what is your name","hey whats your name","I dont think we have been introduced yet", "whats your name","can I get your name","hey remind me of your name","hi who are you","whats your name","what can I call you","what would your name be","what are you named","what do you call yourself","can I have your name"):
        text="i do not have a name I was made by students for a mini project I am a software"#we will give voice output here with gTTS
        tts = gTTS(text=text, lang='en')
        tts.save("output.mp3")
        os.system("mpg123 output.mp3")
        os.remove("output.mp3")
        print("i do not have a name I was made by students for a mini project I am a software")
