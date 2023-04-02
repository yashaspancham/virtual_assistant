import pyttsx3
print("hello")
def say(said):
    say=[]
    say=(said.split(" "))

    if(say[0]=="say"):
        say.pop(0)
        y=' '.join(say)
        engine = pyttsx3.init()
        engine.say(y)
        engine.runAndWait()
    else:
        pass