from bs4 import BeautifulSoup
import requests, json

def parse_tree(data, element):
    if not hasattr(element, "contents") or element is None:
        return
    
    data.append(element.name)
    return parse_tree(data, element.contents[0])



# Get main HTML
html = requests.get("https://exrx.net/Lists/Directory/")
soup = BeautifulSoup(html.text, "html5lib")
mainHtml = soup.find(id="mainShell").find("article")

baseRow = mainHtml.find("div", attrs={"class", "container"}).find("div", attrs={"class", "row"}).find("div", attrs={"class", "col-sm-12"}).find("div", attrs={"class", "row"})
sm6_sections = baseRow.find_all("div", attrs={"class", "col-sm-6"}, recursive=False)

for section in sm6_sections:
    data = []
    section_uls = section.find_all("ul", recursive=False)
   
    for section_ul in section_uls:
        for child in section_ul.recursiveChildGenerator():
            name = getattr(child, "name", None)
            if name is not None:
                print(name)
            elif not child.isspace(): # leaf node, don't print spaces
                print("END: {0}".format(child))
        print("----------------------")


if __name__ == "__main__":
    print(data)