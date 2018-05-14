##############################
# created by Bilal Haroon
# purpose: get all whatsapp contacts
# bharoon@acceducate.com
##############################


# html parser
from bs4 import BeautifulSoup

group_names = []
numbers = []

f = open('test.html', 'r', encoding='utf8')

# parse the file
source = BeautifulSoup(f.read(), "html5lib")

# get the names
def get_names():
    
    names = source.find_all("div", {"class": "_3Bxar"})

    #   itirate through all the names
    for name in names:
        
        # get all the children
        children = name.findChildren()
    
        # iterate through all the children
        for child in children:
            # if child is a name
            if child.get('class') == ['_1qP8m']:
                    
                    group_names.append(child.text)
                    print(child.text)
    return group_names


# get the numbers
def get_numbers():
    phone_numbers = source.find_all("div", {"class":"_25Ooe"})

    for number in phone_numbers:
        
        # get all the chidren
        child = number.findChild()
        
        # if child is a phone number i.e +1 (123) 456-789
        if child.text[0] == '+':
            numbers.append(child.text)
            print(child.text)
    return numbers


def main():
    get_names()
    print("=====================================================")
    get_numbers()
    
            
    

if __name__ == '__main__':
    main()