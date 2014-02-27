import urllib.request as ureq
import botconfig
import nyaaSe

def initialize():
    pass #PLACEHOLDER

def follow(nick, options):
    return[botconfig.channel,(nick + str(options))] #PLACEHOLDER

def listfollow(nick, options):
    return[nick,(nick + str(options))] #PLACEHOLDER

def unfollow(nick, options):
    return[botconfig.channel,(nick + str(options))] #PLACEHOLDER

def userActivity(nick):
    return [] #PLACEHOLDER


