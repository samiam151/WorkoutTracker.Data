from bs4 import BeautifulSoup
import requests
import helpers

# Get main HTML
html = requests.get("https://exrx.net/Lists/ExList/HipsWt#Abductors")
soup = BeautifulSoup(html.text, "html5lib")
mainHtml = soup.find(id="mainShell").find("article")

# Break down containers
returnData = {}

numDataContainers = 0
numTitleContainers = 0

containers = mainHtml.findAll("div", attrs={"class": "container"}, recusive = False)
for index, container in enumerate(containers):
    # print(container)
    if (helpers.isDataContainer(container, index)):
        numDataContainers = numDataContainers + 1
        helpers.processDataContainer(container, returnData)

    elif (helpers.isTitleContainer(container, index)):
        numTitleContainers = numTitleContainers + 1
        helpers.processTitltContainer(container, returnData)
    else:
        pass

if __name__ == "__main__":
    print('Data: {0}'.format(numDataContainers))
    print('Title: {0}'.format(numTitleContainers))