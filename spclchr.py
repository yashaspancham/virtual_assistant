
spcl=dict()
i=0
spcl={"exclamation":"!",
    "at":"@",
    "hash":"#",
    "mod":"%",
    "exponent":"^",
    "ampersand":"&",
    "star":"*",
    "parenthesis":"()",
    "hyphen":"-",
    "underscore":"_",
    "plus":"+",
    "equals":"=",
    "flower":"{}",
    "square":"[]",
    "back slash":"\ ",
    "pipeline":"|",
    "colon":":",
    "semicolon":";",
    "double quote":'""',
    "single quote":"''",
    "less than":"<",
    "greater than":">",
    "comma":",",
    "dot":".",
    "slash":"/",
    "question mark":"?",
    "back quote":"`",
    "tilde":"~",
    "zero":"0",
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9",
}
print(spcl)
while i==0:
    print("Enter the input:\n")
    inp=said
    if inp=="stop":
        i=1
    else:
        key=spcl.get(inp)
        print(key)
    
    
