import urllib.request as ureq
import botconfig
import nyaaSe
import time
import os
import pickle

database = []

def initialize():
    try:
        f = open(os.getcwd() + '/follow.database', 'rb')
        database = pickle.load(f)
        f.close()
    except:
        print("Could not load the database!!!")

def saveDatabase():
    try:
        f = open(os.getcwd() + '/follow.database', 'wb')
        pickle.dump(database, f)
        f.close()
    except:
        print("Could not save the database!!!")

def follow(nick, options):
    database.append({'nick': nick,
                     'options': options,
                     'episode': nyaaSe.lastep(nyaaSe.parseNyaaCommands(options)),
                     'timestamp': time.time()})
    saveDatabase()
    return [botconfig.channel, "I'll notify you when there are new episodes for " + '"' + nyaaSe.parseNyaaCommands(options)['term'] + '", ' + nick + '.']

def listfollow(nick, options):
    return [nick,(nick + str(options))] #PLACEHOLDER

def unfollow(nick, options):
    return [botconfig.channel,(nick + str(options))] #PLACEHOLDER

def userActivity(nick):
    m = []
    if not database == []:
        for x in database:
            if x['nick'] == nick and x['timestamp'] < time.time() - botconfig.cooldown:
                oldEpisode = x['episode']
                options = x['options']
                newEpisode = nyaaSe.lastep(nyaaSe.parseNyaaCommands(options))
                database.remove(x)
                database.append({'nick': nick,
                                 'options': options,
                                 'episode': newEpisode,
                                 'timestamp': time.time()})
                saveDatabase()
                if oldEpisode['episode'] < newEpisode['episode']:
                    m.append([nick, 'There is a new episode for "' + nyaaSe.parseNyaaCommands(options)['term'] + '"! Download it here: ' + newEpisode['link']])
    return m


