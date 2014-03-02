import botconfig
import urllib.request as ureq
import re
from datetime import datetime

dataBase = {}

def initialize():
    global dataBase
    try:
        f = open(botconfig.nyaaDataPath + 'list.dat', 'rb')
        dataBase = pickle.load(f)
        f.close()
    except:
        pass
    
def parse_params(Params):
    Params.split()
def shell_follow(User, Params):
    global dataBase
    

def getNyaaSe(params):
    reqUrl =  'http://www.nyaa.se/?page=rss&term=' + params['term']
    if 'cats' in params:
        reqUrl += '&cats=' + nyaaCatsConvert(params['cats'])
    else:
        reqUrl += '&cats=1_37'
    if 'minage' in params:  reqUrl += '&minage=' + params['minage']
    if 'maxage' in params:  reqUrl += '&maxage=' + params['maxage']
    if 'minsize' in params: reqUrl += '&minsize=' + params['minsize']
    if 'maxsize' in params: reqUrl += '&maxsize=' + params['maxsize']
    if 'filter' in params:
        reqUrl += '&filter=' + params['filter']
    else:
        reqUrl += '&filter=2'
    try:
        searchRes = str(ureq.urlopen(reqUrl).read(), botconfig.charset)
    except:
        searchRes = ""
    items = []
    while '<item>' in searchRes:
        itemStart = searchRes.find('<item>')
        itemEnd = 7 + searchRes.find('</item>')
        candidate = nyaaRSSItemParser(searchRes[itemStart:itemEnd])
        items.append(candidate)
        searchRes = searchRes[itemEnd:]
    return items
        
        

def nyaaRSSItemParser(itemString):
    elStart = itemString.find('[') + 1 #parse the uploader name
    elEnd = itemString.find(']')
    uploader = itemString[elStart:elEnd]
    elStart = itemString.find('<title>') + 7 #parse the actual file name
    elEnd = itemString.find('</title>')
    fileName = itemString[elStart:elEnd]
    try:
        epNumber = int(re.findall('-[\s_]\d+', fileName)[0][2:])#get the episode number
    except:
        epNumber = 0
    if '[720p]' in fileName: #get the resolution
        resolution = 720
    elif '[1280*720]' in fileName:
        resolution = 720
    elif '[1080p]' in fileName:
        resolution = 1080
    elif '[1920*1080]' in fileName:
        resolution = 1080
    elif '[480p]' in fileName:
        resolution = 480
    elif '[848*480]' in fileName:
        resolution = 480
    else:
        resolution = 0
    fileType = fileName[len(fileName) - 3:]#get the filetype
    elStart = itemString.find('<link>') + 6 #get the link
    elEnd = itemString.find('</link>')
    downloadLink = re.sub("#38;", "", itemString[elStart:elEnd])
    elStart = itemString.find('<pubDate>') + 9 #get the publication date
    elEnd = itemString.find('</pubDate>')
    pubDate = int(datetime.strptime(itemString[elStart:elEnd],'%a, %d %b %Y %H:%M:%S %z').timestamp())
    return {'name': fileName,
            'uploader': uploader,
            'episode': epNumber,
            'resolution': resolution,
            'extension': fileType,
            'link': downloadLink,
            'timestamp': pubDate}
    
    
def nyaaCatsConvert(categoryName):
    return '0_0'

def lastep(params):
    episodes = getNyaaSe(params)
    lastNum = 0
    lastRes = 0
    lastEpisode = {}
    for episode in episodes:
        if episode['episode'] == lastNum:
            if episode['resolution'] > lastRes:
                lastRes = episode['resolution']
                lastEpisode = episode
        elif episode['episode'] > lastNum:
                lastNum = episode['episode']
                lastRes = episode['resolution']
                lastEpisode = episode
    return lastEpisode

def parseNyaaCommands(options): #PLACEHOLDER
    term = ''
    for option in options:
        term += option + ' '
    return {'term': term.rstrip()}
    
