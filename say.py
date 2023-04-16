from gtts import gTTS
import os

def say(said):
    say=[]
    say=(said.split(" "))

    if(say[0]=="say"):
        say.pop(0)
        y=' '.join(say)
        tts=gTTS(text=y,lang="en")
        tts.save("output.mp3")
        os.system("mpg123 output.mp3")
        os.remove("output.mp3")
        exit(0)
    else:
        pass
