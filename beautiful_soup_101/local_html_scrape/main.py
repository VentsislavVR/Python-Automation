from bs4 import BeautifulSoup

with open("emag_front_page.html", "r") as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, "lxml")
    tags = soup.find("h2")

    print(tags)
