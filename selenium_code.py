from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://automatetheboringstuff.com')

elem = browser.find_element_by_css_selector('')

elem
elem.click()

elems = browser.find_element_by_css_selector('p')
len(elems)