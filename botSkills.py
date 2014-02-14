import botconfig
import follow
import tell
import lastep

def initializeShellCommands():
    follow.initialize()
    tell.initialize()
    lastep.initialize()

def shellInterpreter(x):
    nick = x[1:x.find("!")]
    x = x[x[1:].find(":") + 2:]
    message = x[:len(x)-2].split(" ")
    y=[]
    if message[0] == ".follow":
        y = [(follow.follow(nick, message[1:len(message)]))]
    elif message[0] == ".listfollow":
        y = [(follow.listfollow(nick, message[1:len(message)]))]
    elif message[0] == ".unfollow":
        y = [(follow.unfollow(nick, message[1:len(message)]))]
    elif message[0] == ".tell":
        y = [(tell.tell(nick, message[1:len(message)]))]
    elif message[0] == ".lastep":
        y = [(lastep.lastep(nick, message[1:len(message)]))]
    y = y + follow.userActivity(nick)
    y = y + tell.userActivity(nick)
    y = y + lastep.userActivity(nick)    
    return y
    
    
    
