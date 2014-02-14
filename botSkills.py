import botconfig
import urllib.request as ureq

def dealWithIt(x):
    return "Dealing with it."

def getNyaaSe(params):
    reqUrl =  "http://www.nyaa.se/?page=rss&term=" + params["term"]
    if "cats" in params:    reqUrl += "&cats=" + nyaaCatsConvert(params["cats"])
    if "minage" in params:  reqUrl += "&minage=" + params["minage"]
    if "maxage" in params:  reqUrl += "&maxage=" + params["maxage"]
    if "minsize" in params: reqUrl += "&minsize=" + params["minsize"]
    if "maxsize" in params: reqUrl += "&maxsize=" + params["maxsize"]
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
    
