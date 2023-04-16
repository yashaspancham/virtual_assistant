from gtts import gTTS
import os

# Set the text to be spoken
text = "Hello, how are you today?"

## Create a gTTS object and save the audio to a file
tts = gTTS(text=text, lang='en')
tts.save("output.mp3")

# Play the audio file
os.system("mpg123 output.mp3")

# Delete the audio file
os.remove("output.mp3")
