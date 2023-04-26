import pyjokes
from gtts import gTTS
import os

def jokes(said):
    if said in ("tell me a good joke","make me laugh","tell me a joke","joke about something"):
        jokes=pyjokes.get_joke()
        
        print(f'The joke is: {jokes}')
        tts = gTTS(text=jokes, lang='en')#giving the voice output
        tts.save("output.mp3")
        os.system("mpg123 output.mp3")
        os.remove("output.mp3")#deledting the mp3 file
