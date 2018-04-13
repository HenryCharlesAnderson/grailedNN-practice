from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import grailed_objects
import time
import pickle
import sys

#Unwind an infinitely scrolling page
def infinite_scroll(driver, limit):
    scrollToBottomScript = "window.scrollTo(0, document.body.scrollHeight);var height=document.body.scrollHeight;return height;"
    height = driver.execute_script(scrollToBottomScript)
    prevHeight = 0
    while(prevHeight!=height and limit != 0):#set limit to -1 for largest possible runtime...?
        limit = limit-1
        time.sleep(1)
        prevHeight = height
        height = driver.execute_script(scrollToBottomScript)     

if __name__=="__main__":
    driver = webdriver.Firefox()

    try:
        driver.get("https://www.grailed.com/sold")

        #Load 6 pages
        infinite_scroll(driver,5)

        #Get all the item overviews
        items = driver.find_elements_by_class_name("feed-item")
        print(len(items),'listings')

        listings = []

        #Create listing objects from each item
        for item in items:
            info = item.text.split("\n")
            if 5==len(info):
                time = info[0]
                designer = info[1]
                size = info[2]
                title = info[3]
                price = info[4][1:]

            date = item.find_element_by_class_name("listing-age").text

            listings.append(grailed_objects.Listing(time,designer,size,title,price,date))

        #Save scraped data
        f = open("listings.pkl", "wb")
        pickle.dump(listings,f)
        f.close()
    except:
        print("Unexpected error:", sys.exc_info()[0])
    else:
        driver.quit()

       

