import getCats 

def presentCats():
    return getCats.getCats().keys()

def getCatUrl(cat):
    return getCats.getCats()[cat]

def getConfs(url):
    return getCats.getConfs(url) 
