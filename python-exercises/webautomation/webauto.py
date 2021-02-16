from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.msn.com/fr-fr?AR=6")

searchbox = driver.find_element_by_xpath('//*[@id="q"]').send_keys('python')
searchButton = driver.find_element_by_xpath('//*[@id="sb_form_go"]').click()
