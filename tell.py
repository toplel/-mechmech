import botconfig
import time
import os
import pickle

database = []

def initialize():
    try:
        f = open(os.getcwd() + '/tell.database', 'rb')
        database = pickle.load(f)
        f.close()
    except:
        print("Could not load the database!!!")

def saveDatabase():
    try:
        f = open(os.getcwd() + '/tell.database', 'wb')
        pickle.dump(database, f)
        f.close()
    except:
        print("Could not save the database!!!")

def tell(nick, options):
    m = time.strftime("[%H:%M]") + " <" + nick + "> tell"
    for o in options:
        m += " " + o
    database.append([options[0], m, time.time()])
    saveDatabase()
    return [botconfig.channel, "I'll pass that on when " + options[0] + " is around, " + nick + "."]

def userActivity(nick):
    m = []
    if not database == []:
        for x in database:
            if x[0] == nick:
                m.append([botconfig.channel,x[1]])
                database.remove(x)
            elif (time.time() - x[2]) > botconfig.tell_timeout:
                database.remove(x)
        print(str(database))
    saveDatabase()
    return m
