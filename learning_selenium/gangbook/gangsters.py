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
signin_btn = driver.find_element_by_xpath('//*[text()="Sign in"]')

email_input.send_keys('test@user.com')
password_input.send_keys('123456')
sign_in_btn.click()

#Search

search_input_selector = '[name="hometown"]'
wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, search_input_selector)))
search_input_bar = driver.find_element_by_css_selector(search_input_selector)
search_input_bar.send_keys('Gdynia')
gangster_list = driver.find_elements_by_css_selector('strong')
for x in range(len(gangster_list)):
    if gangster_list[x].text == 'Valentijn':
        gangster_list[x].click()
        break

#Show choosen gangster data
valentijn = driver.find_element_by_xpath('//*[contains(text(),"Valentijn")]')
valentijn.click()
#xpath w konsoli $x('//node[@property="value"]')
#xpath w konsoli $x('//node[contains(@property, "val")]')
#css selector w konsoli $($$)('node[property=value]')    wszystkie nody dajemy w ''
#css selector w konsoli $($$)('node[property*=val]')

#Book

book_gangster_btn = driver.find_element_by_css_selector('button')
book_gangster_btn.click()
send_btn = driver.find_element_by_css_selector('button')
send_btn.click()

#Check booking

see_summary_btn = driver.find_element_by_xpath('//button[text()="See a summary of your orders"]')
see_summary_btn.click()
assert len(driver.find_elements_by_xpath('//*[text()="hdat2@arizona.edu"]')) > 0, \
           'no orders pending for valentijn'


time.sleep(3)
driver.quit()


