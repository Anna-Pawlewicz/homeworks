#  find and print all blackmail gangsters from Gdańsk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('http://gangbook.pydqz1.is-academy.pl/')
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 15)

#Log in

email_input = driver.find_elements_by_css_selector('[name="username"]')[0]
password_input = driver.find_elements_by_css_selector('[name="password"]')[0]
sign_in_btn = driver.find_element_by_css_selector('button')

email_input.send_keys('ania@user.com')
password_input.send_keys('123456')
sign_in_btn.click()

#Search

search_input_selector = '[name="hometown"]'
wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, search_input_selector)))
search_input_bar = driver.find_element_by_css_selector(search_input_selector)
search_input_bar.send_keys('Gdańsk')

#filter blackmail

blackmail_btn = driver.find_element_by_css_selector('button#blackmail')
blackmail_btn.click()

#list number of smugglers

blackmail_list = driver.find_elements_by_css_selector('strong')
print('total number of blackmails in Gdańsk: ' + str(len(blackmail_list)))


time.sleep(3)
driver.quit()
