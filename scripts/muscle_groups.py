from bs4 import BeautifulSoup
import requests, json
from utils import getDepth, assembleTree


# Get main HTML
html = requests.get("https://exrx.net/Lists/Directory/")
soup = BeautifulSoup(html.text, "html5lib")
mainHtml = soup.find(id="mainShell").find("article")

baseRow = mainHtml.find("div", attrs={"class", "container"}).find("div", attrs={"class", "row"}).find("div", attrs={"class", "col-sm-12"}).find("div", attrs={"class", "row"})
sm6_sections = baseRow.find_all("div", attrs={"class", "col-sm-6"}, recursive=False)
data = []

for section in sm6_sections:
    section_uls = section.find_all("ul", recursive=False)
   
    for section_ul in section_uls:
        for child in section_ul.recursiveChildGenerator():
            name = getattr(child, "name", None)
            
            if name is not None:
                pass
            elif not child.isspace(): # leaf node, don't print spaces
                depth = getDepth(child)
                data.append({
                    "name": child.strip(),
                    "depth": depth
                })

jsonData = assembleTree(data)

if __name__ == "__main__":
    f = open("data.json", "w")
    f.write(json.dumps(data, indent=4))
    f.close()

    f = open("full-data.json", "w")
    f.write(json.dumps(jsonData, indent=4))
    f.close()