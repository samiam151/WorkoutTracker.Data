from bs4 import BeautifulSoup
import requests, json

def parse_ul(data, ul):
    if ul is None:
        return ul

    a_tag = ul.find("a")
    if (a_tag): 
        data[a_tag.text] = []

    all_uls = ul.find("ul")
    if len(all_uls) > 0:
        for _ul in all_uls:
            return parse_ul(data, _ul)

    return parse_ul(data, ul.find("ul"))


# Get main HTML
html = requests.get("https://exrx.net/Lists/Directory/")
soup = BeautifulSoup(html.text, "html5lib")
mainHtml = soup.find(id="mainShell").find("article")

# 
baseRow = mainHtml.find("div", attrs={"class", "container"}).find("div", attrs={"class", "row"}).find("div", attrs={"class", "col-sm-12"}).find("div", attrs={"class", "row"})
sm6_sections = baseRow.find_all("div", attrs={"class", "col-sm-6"}, recursive=False)

for section in sm6_sections:
    data = {}
    section_uls = section.find_all("ul", recursive=False)
   
    for section_ul in section_uls:
        print(parse_ul(data, section_ul))



if __name__ == "__main__":
    print(data)