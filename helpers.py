def isTitleContainer(container, index = 0):
    h2 = container.find("h2")
    return h2 is None

def isDataContainer(container, index = 0):
    uls = container.find_all("ul")        
    return uls == []