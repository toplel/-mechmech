import botconfig
import urllib.request as ureq

dataBase = {}

def initialize():
    global dataBase
    try:
        f = open(botconfig.nyaaDataPath + "list.dat", "rb")
        dataBase = pickle.load(f)
        f.close()
    except:

def parse_params(Params)
    Params.split
def shell_follow(User, Params):
    global dataBase
    

def getNyaaSe(params):
    reqUrl =  "http://www.nyaa.se/?page=rss&term=" + params["term"]
    if "cats" in params:
        reqUrl += "&cats=" + nyaaCatsConvert(params["cats"])
    else:
        reqUrl += "&cats=1_37"
    if "minage" in params:  reqUrl += "&minage=" + params["minage"]
    if "maxage" in params:  reqUrl += "&maxage=" + params["maxage"]
    if "minsize" in params: reqUrl += "&minsize=" + params["minsize"]
    if "maxsize" in params: reqUrl += "&maxsize=" + params["maxsize"]
    if "filter" in params:
        reqUrl += "&filter=" + params["filter"]
    else:
        reqUrl += "&filter=2"
    searchRes = str(ureq.urlopen(reqUrl).read(), botconfig.charset)
    items = []
    while "<item>" in searchRes:
        itemStart = searchRes.find("<item>")
        itemEnd = 7 + searchRes.find("</item>")
        items.append(searchRes[itemStart:itemEnd])
        print(searchRes[itemStart:itemEnd])
        searchRes = searchRes[itemEnd:]

def nyaaRSSItemParser(itemString):
    pass
    
    
def nyaaCatsConvert(categoryName):
    return "0_0"
    
