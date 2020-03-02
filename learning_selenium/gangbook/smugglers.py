# print number of gangsters and number of smugglers
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('http://gangbook.pydqz1.is-academy.pl/')
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 15)

#Log in

email_input = driver.find_element_by_xpath('//*[text()="Sign in"]/..//*[@name="username"]')
password_input = driver.find_element_by_xpath('//*[text()="Sign in"]/..//*[@name="password"]')
signin_btn = driver.find_element_by_xpath('//*[text()="Sign in"]')

email_input.send_keys('ania@user.com')
password_input.send_keys('123456')
signin_btn.click()

#List number of gangsters

gangster_list = driver.find_elements_by_css_selector('strong')
print('total number of gangsters: ' + str(len(gangster_list)))

#filter smugglers

smugglers_btn = driver.find_element_by_css_selector('button#smuggling')
smugglers_btn.click()

#list number of smugglers

smugglers_list = driver.find_elements_by_css_selector('strong')
print('total number of smugglers: ' + str(len(smugglers_list)))


time.sleep(3)
driver.quit()