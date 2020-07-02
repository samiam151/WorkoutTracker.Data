from bs4 import BeautifulSoup
import requests
# import helpers

# Get main HTML
html = requests.get("https://exrx.net/Lists/Directory/")
soup = BeautifulSoup(html.text, "html5lib")
mainHtml = soup.find(id="mainShell").find("article")

# 
baseRow = mainHtml.find("div", attrs={"class", "container"}).find("div", attrs={"class", "row"}).find("div", attrs={"class", "col-sm-12"}).find("div", attrs={"class", "row"})
sm6_sections = baseRow.find_all("div", attrs={"class", "col-sm-6"}, recursive=False)

for section in sm6_sections:
    section_ul = section.find("ul", recursive=False)
    section_title = section_ul
    print(section_ul.contents)

if __name__ == "__main__":
    for section in sm6_sections:
        # print(type(section)) 
        pass