from bs4 import BeautifulSoup
import requests
from helpers import isDataContainer

# Get main HTML
html = requests.get("https://exrx.net/Lists/ExList/HipsWt#Abductors")
soup = BeautifulSoup(html.text, "html5lib")
mainHtml = soup.find(id="mainShell").find("article")

# Break down containers
returnData = {}

numDataContainers = 0
numTitleContainers = 0

containers = mainHtml.findAll("div", attrs={"class": "container"}, recusive = False)
for container in containers:
    # print(container)
    if (isDataContainer(container)):
        numDataContainers = numDataContainers + 1
    else:
        numTitleContainers = numDataContainers + 1

if __name__ == "__main__":
    print('Data: {0}'.format(numDataContainers))
    print('Title: {0}'.format(numTitleContainers))