def parse_tree(data, element):
    if not hasattr(element, "contents") or element is None:
        return
    
    data.append(element.name)
    return parse_tree(data, element.contents[0])

def getDepth(child):
    numUls = -1
    for parent in child.parents:
        parent_name = getattr(parent, "name", None)
        if parent_name == "ul":
            numUls = numUls + 1
    return numUls

def findParent(data, category, baseDepth=0):
    depth = category['depth']
    parents = [datum for datum in data if datum['depth'] == (depth - 1)]
    this_parent = None
    for parent in parents:
        index = data.index(parent)
        while(index < len(data) and depth != baseDepth):
            entry = data[index]
            if (category['name'] == entry['name']):
                this_parent = parent
                break
            index += 1
    return this_parent

def assembleTree(data):
    lastLevel = 0
    jsonData = {}

    for category in data:
        depth = category['depth']
        if (depth == 0):
            jsonData[category['name']] = []
        if (depth == 1):
            parent = findParent(data, category)
            if (parent['name'] not in list(jsonData.keys())):
                jsonData[parent['name']] = []
            
            jsonData[parent['name']].append(category)
            # print(parent)

        if (depth == 2):
            parent = findParent(data, category, 1)
            if (parent['name'] not in list(jsonData.keys())):
                jsonData[parent['name']] = []
            
            jsonData[parent['name']].append(category)

        lastLevel = category['depth']
    
    return jsonData