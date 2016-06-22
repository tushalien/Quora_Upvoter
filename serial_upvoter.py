#!/usr/bin/python
import os
import time
import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from ConfigParser import SafeConfigParser

# Reading configuration file  
parser = SafeConfigParser()
parser.read('config.ini')
parameters = {} 								

for pairs in parser.sections():			# Parse the configuration file 
	for name, value in parser.items(pairs):
		parameters[name] = value

# Automating your browser 
chromedriver  = parameters["path"]
os.environ["webdriver.chrome.driver"] = chromedriver

#Uncomment this block if you don't want images to load(makes the procss a little bit faster)
'''
chromeOptions = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images":2}
chromeOptions.add_experimental_option("prefs",prefs)
browser = webdriver.Chrome(chromedriver, chrome_options=chromeOptions)
'''

browser = webdriver.Chrome(chromedriver)
browser.set_window_size(1120, 550)
browser.get("http://www.quora.com")		# Quora home page 
time.sleep(3)								

# Logging into Quora 
form = browser.find_element_by_class_name('regular_login')
email = form.find_element_by_name("email")
password = form.find_element_by_name("password")
email.send_keys(parameters["email_id"])
try:
	pass_word = parameters["pass_word"]
except:
	pass_word = getpass.getpass()				# If you want to enter password on terminal
password.send_keys(pass_word)
password.send_keys(Keys.RETURN)
time.sleep(2)									

# Fetching answers page of t6he user
answers_url = "https://www.quora.com/" + parameters["username"] + "/answers"		
browser.get(answers_url)									

 #Upvoting answers one by one from top to bottom 
counter=0
while True:
	try:
		elem=browser.find_element_by_xpath("//*[@action_click='AnswerUpvote']")
		counter=counter+1
		elem.click()
		time.sleep(4)
	except:
		break

print str(counter) +" answers upvoted.."


