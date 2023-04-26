import say
import name
import jokes
import googfind
import stock_data

def process(said):
    print("Processing the string input")
    say.say(said)
    #name.nname(said)
    jokes.jokes(said)
    googfind.googfind(said)
    stock_data.stock_data(said)