import botconfig
import nyaaSe

def initialize():
    pass

def lastep(nick, options):
    episode = nyaaSe.lastep(nyaaSe.parseNyaaCommands(options))
    if episode == {}:
        response = nick + ': No valid result found!'
    else:
        response = nick + ': The last episode of "' + nyaaSe.parseNyaaCommands(options)['term'] + '" is ' + str(episode['episode']) + ': ' + episode['link']
    return [botconfig.channel,response]

def userActivity(nick):
    return []
