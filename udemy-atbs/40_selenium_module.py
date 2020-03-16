#! usr/bin/env python3
"""
Using Selenium to control, extract and parse web browsing.
"""
from selenium import webdriver

# generate a browser.object called 'browser'
browser = webdriver.Firefox()

"""
'Geckodriver' is required for Firefox. Follow following steps:
1. Download 'geckodrive' for Firefox, there are different drivers for 
Chrome, Edge, Safari.
2. Extract the package using `tar xzf 'package-name`
3. Make 'geckodriver' executable using `sudo chmod +x geckodriver`
4. Move 'geckodriver' to /usr/bin/geckodriver
"""

# use method(get) to open a web page using
browser.get("https://automatetheboringstuff.com")

# copy the css selector of Chapter 12 Link
# and use method(find_element_by_ ) to find the element
chap12_selector = browser.find_element_by_css_selector(
    ".main > ul:nth-child(16) > li:nth-child(13) > a:nth-child(1)")

# to stimulate the clicking use method(click)
chap12_selector.click()

"""
How to use Selenium to provide text entry into search field of amazon.in
"""
# get amazon browser object
amazon_browser = browser.get("https://amazon.in")

# use method(find_element_by_ ) to get the amazon search element
amazon_search = browser.find_element_by_css_selector("#twotabsearchtextbox")

# use method(send_keys) to provide input to the search field
amazon_search.send_keys('Redmi Mobile Phone')

# use method(submit()) to submit our query
amazon_search.submit()
browser.find_element_by_css_selector("#twotabsearchtextbox").submit()

"""
Using selenium to read and display the contents of a webpage.
Read amazon product page
"""

# reading from amazon product page
read_browser = browser.get("https://www.amazon.in/Redmi-Note-Neptune-Blue-Storage/dp/B07X1KT6LD")

# def read element for price
amazon_read = browser.find_element_by_css_selector("#priceblock_ourprice")

# every web element has text member variable field
print(amazon_read.text)

# def read element for technical description
redmi_note8_table = browser.find_element_by_css_selector("div.column:nth-child(1) > div:nth-child(1)")
print(redmi_note8_table.text)
