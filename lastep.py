import botconfig
import nyaaSe

def initialize():
    pass

def lastep(nick, options):
    term = ''
    for option in options:
        term += option + ' '
    episodes = nyaaSe.getNyaaSe({'term': term})
    lastNum = 0
    lastRes = 0
    lastName = ''
    lastLink = ''
    for episode in episodes:
        if episode['episode'] == lastNum:
            if episode['resolution'] >= lastRes:
                lastRes = episode['resolution']
                lastLink = episode['link']
        elif episode['episode'] > lastNum:
                lastNum = episode['episode']
                lastRes = episode['resolution']
                lastLink = episode['link']
    if not lastNum == 0:
        response = nick + ': The last episode of "' + term.rstrip() + '" is ' + str(lastNum) + ': ' + lastLink
    else:
        response = nick + ': No valid result found!'
    return [botconfig.channel,response]

def userActivity(nick):
    return []
