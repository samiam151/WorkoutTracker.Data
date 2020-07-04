from bs4 import BeautifulSoup
import requests

html = requests.get("https://exrx.net/Lists/Directory/")
soup = BeautifulSoup(html.text, "html5lib")
mainHtml = soup.find(id="mainShell").find("article")

baseRow = mainHtml.find("div", attrs={"class", "container"}).find("div", attrs={"class", "row"}).find("div", attrs={"class", "col-sm-12"}).find("div", attrs={"class", "row"})

for child in baseRow.recursiveChildGenerator():
     name = getattr(child, "name", None)
     if name is not None:
         print(name)
     elif not child.isspace(): # leaf node, don't print spaces
         print("END: {0}".format(child))