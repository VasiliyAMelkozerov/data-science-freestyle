import selenium
#this library has all sorts of web interaction stuff both for Java and python
from selenium import webdriver
import time
import personal_information as p
#this will be left commented out until I have a working model

driver = webdriver.Chrome()
#this takes us to our target website
driver.get('https://www.linkedin.com')

time.sleep(1)
#we wait until the page is fully loaded to start inputting

email = driver.find_element('xpath','//*[@id="session_key"]')
#inputting in the email field
email.send_keys(p.email)

password = driver.find_element('xpath', '//*[@id="session_password"]')
#input to the password feild 
password.send_keys(p.password)

login = driver.find_element('xpath','/html/body/main/section[1]/div/div/form/button')
login.click()

time.sleep(10)

jobs = driver.find_element('xpath','/html/body')
#its giving me an error and not clicking to where I want to go
#alternatively what I can also do is go directly to the link after signing in
#instead of having to go and do it the clicky clank way
jobs.click()

time.sleep(1)