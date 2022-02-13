######################################
#
#   Script for scraping StuDocu webpage
#     from https://www.studocu.com/en-us/document/western-governors-university/advanced-pathopharmacological-foundations/d027-study-guide-to-assist-with-the-class/19312435?shared=1&sid=01644724574
#
#               by
#
#          Daniel Augustine
#
#
#
#   This script goes to the StuDocu site, 
#   and scrapes the pdf document webpage
#   as a project requested by my mom 
#
#
#
#   Note: I ran into so trouble trying to access the vaules in <div id="pf15"...> and onwards
#         so I have two separate loops that scrapes the pdf document from different number of pages:
#           one loop scrapes the first 20 pages and another loop that scrapes the last 12 pages
######################################




from bs4 import BeautifulSoup as soup
from selenium import webdriver
import docx
from docx.enum.section import WD_SECTION
import time
from selenium.webdriver.common.keys import Keys


doc = docx.Document()  #create word document object
#url to grab
my_url = 'https://www.studocu.com/en-us/document/western-governors-university/advanced-pathopharmacological-foundations/d027-study-guide-to-assist-with-the-class/19312435?shared=1&sid=01644724574'

driver = webdriver.Firefox()  #open firefox
driver.get(my_url)  #request url


def get_content(container_list):
    for i in container_list:
        #print(i.text)
        doc.add_paragraph(i.text)
    doc.save('C:/Users/danie/Desktop/WebScrapping/DocumentScraper/D027_Study_Guide.docx')

#scroll down the page
time.sleep(3)
element = driver.find_element_by_id('document-wrapper')  #clicks on the middle of the page
cnt = 0
#scroll down 29 pages to load pages needed to scrape
while cnt < 29:
    element.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)
    page = driver.page_source
    page_soup = soup(page, "html.parser", multi_valued_attributes=None)
    cnt+=1

container = page_soup.findAll('div', {'class':'pf w0 h0'})

#scrape the first 20 pages
for i in range(19):
    content_container =  container[i].find('div',{'class':'page-content'}).find('div',{'style':'display:block'}).findAll('div')
    get_content(content_container)


#scrape the last 12 pages
count = 20
while count < 32:

    #catches any error brought up and skip it while this is running
    try:
        content_container = container[count].find('div',{'class':'page-content'}).find('div',{'style':'display:block'}).findAll('div')
    except:
        print('skipped an error')
    get_content(content_container)
    count+=1
