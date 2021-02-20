from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://automatetheboringstuff.com')

elem = browser.find_element_by_css_selector('.main > div:nth-child(1) > ul:nth-child(21) > li:nth-child(1) > a:nth-child(1)')

print(elem)
elem.click()

elems = browser.find_element_by_css_selector('p')
len(elems)

searchElem = browser.find_element_by_css_selector('.search-field')
searchElem.send_keys('zophie')
searchElem.submit()

browser.back()
browser.forward()
browser.refresh()
browser.quit()

#Getting Text 
newElem = browser.find_element_by_css_selector('.entry-content > p:nth-child(4)')
print(newElem.text)

#Getting the entire text
entElem = browser.find_element_by_css_selector('html')
print(entElem.text)

#READ THE REST OF CHAPTER 11