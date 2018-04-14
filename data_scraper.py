from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import grailed_objects
import time
import sys
import sqlite3

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

        #OpenDB
        conn = sqlite3.connect('listings.db')
        curs = conn.cursor()
        curs.execute('CREATE TABLE IF NOT EXISTS soldItems (time text, designer text, size text, title text, price integer)')
            
        #Create listing objects from each item
        for item in items:
            info = item.text.split("\n")
            if 5==len(info):
                time = info[0]
                designer = info[1]
                size = info[2]
                title = info[3]
                price = info[4][1:]
                print(price)

            #Add row to database
            row = (time,designer,size,title,int(price.replace(',','')))
            curs.execute('INSERT INTO soldItems VALUES (?,?,?,?,?)',row)

        #Commit and close DB
        conn.commit()
        conn.close()

    except:
        print("Unexpected error:", sys.exc_info()[0])
        driver.quit()
    else:
        driver.quit()

       

