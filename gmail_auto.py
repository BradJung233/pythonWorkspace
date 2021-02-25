from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Chrome()
url = 'https://google.com'
driver.get(url)
driver.maximize_window()
action = ActionChains(driver)


driver.find_element_by_css_selector('#gb_70').click()
action.send_keys('holycrol').perform()
driver.find_element_by_css_selector('.VfPpkd-RLmnJb').click()
time.sleep(2)
driver.find_element_by_css_selector('.whsOnd.zHQkBf').send_keys('gh362936')
driver.find_element_by_css_selector('.VfPpkd-RLmnJb').click()
