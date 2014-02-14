import botconfig
import time

database = []

def tell(nick, options):
    m = time.strftime("[%H:%M]") + " <" + nick + "> tell"
    for o in options:
        m += " " + o
    database.append([options[0], m, time.time()])
    return "I'll pass that on when " + options[0] + " is around, " + nick + "."

def userActivity(nick):
    m = []
    if not database == []:
        for x in database:
            if x[0] == nick:
                m.append(x[1])
                database.remove(x)
            elif (time.time() - x[2]) > botconfig.tell_timeout:
                database.remove(x)
        print(str(database))
    return m
