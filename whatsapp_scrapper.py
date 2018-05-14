##############################
# created by Bilal Haroon
# 
# purpose: write all whatsapp contactcts to html file
# 
# bharoon@acceducate.com
##############################



# allows you to controll chrome
from selenium import webdriver
# html parser
from bs4 import BeautifulSoup

# allows program to stop for a certain amount of time
from time import sleep

driver = webdriver.Chrome()

# get whatsapp
driver.get("https://web.whatsapp.com/")


# sleep so user can scan barcode
sleep(15)

def parse():

    # parse html
    # source = BeautifulSoup(driver.page_source)


    # get all contacts
    #contacts = source.find_all("span", class_="_1wjpf")

    # for contact in contacts:
        # print(contact.prettify())
        
    f = open("test.html", "a", encoding='utf8')
        # f.write(str(contact) + "\n<br>")
    f.write(str(driver.page_source))
    f.close()
    # return contacts

# scroll down to get new contents
# driver.execute_script("window.scrollBy(0, 15);") 

def wait():
    print("3")
    sleep(1)
    print("2")
    sleep(1)
    print("1")
    print("\n GO!")

    

def main():
    
    while 1:
        
        try:
            parse()
            wait()
        
        except KeyboardInterrupt:
            break

    
    

if __name__ == '__main__':
    main()