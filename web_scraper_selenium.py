#@author: jordanlardieri
#this code is for the purpose of demonstration
##always consult a website's terms of use before scraping

#For this demo, I was interested in a website that contained information stored in tables across hundreds of pages
#The website was java based so a selenium web crawler was an appropriate solution

#import libraries
import pandas as pd
from selenium import webdriver

#this will initiate the the website crawl, the webpage will pop up
#to note, if get a message that the ChromeDriver is outdated :
##check for current Chrome version by going to help -> about in Chrome browser
##upgrade driver http://chromedriver.chromium.org/downloads and replace chromedriver

driver = webdriver.Chrome()
driver.get('insert_website_here')

#if the website requires credentials :
username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")

#send keys to log in
username.send_keys("insert_username_here")
password.send_keys("insert_password_here")

#store scraped data, here I was interested in storing 2 separate lists
information = []
information_all = []

while True:
    #below is found by inspecting the website using developer tools
    driver.implicity_wait(30)
    #indentify the table
    #to learn more about how the data is structured for display, in this case, the data was contained in a table - right click on the table in developer and access the element name
    table = driver.find_element_by_id('preblockBody')
    job_elems = table.find_elements_by_xpath("//*[@id='preblockBody']/table[*]/tbody/tr[*]/td[*]/a")
    job_elems2 = table.find_elements_by_xpath("//*[contains(@class,'pbListingTable')]")
    for value in job_elems:
        print(value.text)
        information.append(value.text)
    for value in job_elems2:
        print(value2.text)
        information_all.append(value2.text)

    try:
        #go to the next page by clicking the 'Next' button, loop through all available pages
        driver.find_element_by_partial_link_text('Next').click()
    except:
        break

driver.quit()

#The output is a list containing each data point from the table as a line item, I did some data cleaning in Python as well as excel to produce the final output
