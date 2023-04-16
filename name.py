import glob
from gtts import gTTS
import os

def nname(said):
    name=str(said.split(" "))
    x=glob.glob('your*')
    y=' '.join(x)
    if((name.find(y)+1)!=0 or (name.find("name")+1)!=0 or (name.find("call")+1)!=0 or (name.find("speaking")+1)!=0):
        text="My Name is Mr.Baahu What help do you need??"#we will give voice output here with gTTS
        tts = gTTS(text=text, lang='en')
        tts.save("output.mp3")
        os.system("mpg123 output.mp3")
        os.remove("output.mp3")
        print("My Name is Mr.Baahu!!What help do you need??")
    else:
        pass
    