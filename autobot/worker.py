import selenium
#this library has all sorts of web interaction stuff both for Java and python
from selenium import webdriver
#webdriver is what lets us do stuff
import time
#this is imported and used to wait for the websites to be done 
import personal_information as p
#using a personal moduele to be store personal information with it being easily taken

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
#so this here goes and completes the login process
time.sleep(6)
#now the time let's it all load in the way it needs to
#there has been inconsistent loading times when it comes to loading in linkedin after signing in so for now time  is gonna work

driver.get('https://www.linkedin.com/jobs/search/?currentJobId=3226173731&keywords=data%20analyst&refresh=true')
#so from here we are on the page listings of data analyst positions 

#from here I would like to click apply and open the results into a seperate tab

#ahh yes back again to the selenium docs to open my results in a new tab

time.sleep(5)
"""
OHHHHHHHHHHHHH hold on it instantly wants to input after loading the page bit that won't work

give it some time
"""


#it just occured to me that clicking it might naturaully open up a new tab

fbutton = driver.find_element('xpath','//*[@id="ember290"]')
#okay so it does in fact open up in a brand new tab but then all of the code will be on just this one tab.....
#but like what has happened here is that my selenium bot, Imma call him Mathew

"""
So Mathew logs me in and takes me to the page that I want to go he then clicks into the 
first job listing on the entry. From there Mathew is kinda stuck on a new tab
with not really a way to get back
I haven't seen what Mathew does if I tell him to click through the first apply button
"""
