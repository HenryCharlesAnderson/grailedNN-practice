from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import grailed_objects
import time
import sys
import sqlite3

#Unwind an infinitely scrolling page
def infinite_scroll(driver, limit=1):
    scrollToBottomScript = "window.scrollTo(0, document.body.scrollHeight);var height=document.body.scrollHeight;return height;"
    height = driver.execute_script("var height=document.body.scrollHeight;return height;")
    prevHeight = 0
    while(prevHeight!=height and limit > 0):
        limit = limit-1
        time.sleep(1)
        prevHeight = height
        height = driver.execute_script(scrollToBottomScript)     

def scrape_grailed(driver=webdriver.Firefox(), pages=6, url='https://www.grailed.com/sold'):
    try:#lazy try so that the driver gets closed no matter what

        driver.get(url)

        #Load n pages
        infinite_scroll(driver,pages)

        #Get all the item overviews
        items = driver.find_elements_by_class_name('feed-item')

        #Open DB
        conn = sqlite3.connect('listings.db')
        curs = conn.cursor()
        curs.execute('''CREATE TABLE IF NOT EXISTS soldItems 
        (url text primary key, time text, designer text, size text, title text, price integer)''')
            
        #Create db row from each item
        for item in items:
            info = item.text.split("\n")
            if 5==len(info):
                time = info[0]
                designer = info[1]
                size = info[2]
                title = info[3]
                price = info[4][1:]
            
            url = item.find_element_by_tag_name('a').get_attribute('href')

            #Add row to database
            row = (url,time,designer,size,title,int(price.replace(',','')))
            curs.execute('INSERT INTO soldItems VALUES (?,?,?,?,?,?)',row)

        #Commit and close DB
        conn.commit()
        conn.close()
    except:
        print("Unexpected error:", sys.exc_info()[0])
        driver.quit()
    else:
        driver.quit()


if __name__=="__main__":
    
        scrape_grailed()
    

