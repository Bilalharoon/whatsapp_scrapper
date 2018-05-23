##############################
# created by Bilal Haroon
# 
# purpose: write all whatsapp contacts to html file
# 
# email: bharoon@acceducate.com
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


# wait so user can scan barcode
try:
    input("Press Enter to continue...")
except EOFError:
    print("something went wrong...")
except KeyboardInterrupt:
    print("good bye")

def parse():
        
    f = open("test.html", "a", encoding='utf8')
    f.write(str(driver.page_source))
    f.close()




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