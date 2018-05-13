##############################
# created by Bilal Haroon
# 
# purpose: get all whatsapp contacts
# 
# bharoon@acceducate.com
##############################


# html parser
from bs4 import BeautifulSoup


def main():
    f = open('test.html', 'r', encoding='utf8')

    # parse the file
    source = BeautifulSoup(f.read(), "html5lib")

    # get the names and phone numbers
    names = source.find_all("div", {"class": "_3Bxar"})
    phone_numbers = source.find_all("div", {"class":"_25Ooe"})

    group_names = []
    numbers = []
    counter = 0
    
    for name in names:
        children = name.findChildren()
    
        for child in children:
            if child.get('class') == ['_1qP8m']:
                if child.text is None:
                    print("\n")
                else:               
                    group_names.append(child.text)
                    print(child.text)

    for number in phone_numbers:
        
        child = number.findChild()
        
        if child.text[0] == '+':
            numbers.append(child.text)
            print(child.text)
            
    

if __name__ == '__main__':
    main()