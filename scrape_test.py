from bs4 import BeautifulSoup

f = open('test.html', 'r', encoding='utf8')

source = BeautifulSoup(f.read(), "html5lib")

divs = source.find_all("div", {"class": "_3Bxar"})

contacts = []
counter = 0
for div in divs:
    children = div.findChildren()
    
    for child in children:
        if child.get('class') == ['_1qP8m']:
            print(child.text)
            counter+=1
            print(counter)
            

