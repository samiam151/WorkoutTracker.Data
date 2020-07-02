def isTitleContainer(container, index = 0):
    h2 = container.find("h2")
    return h2 is not None

def isDataContainer(container, index = 0):
    uls = container.find_all("ul")    
    return uls != []

def processDataContainer(container, dataDict):
    pass

def processTitltContainer(container, dataDict):
    pass