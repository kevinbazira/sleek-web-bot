# Project Name: SleekWebBot
# Author: Kevin Bazira
# Descripttion: SleekWebBot is an internet robot that visits a website and clicks on a specified web element.
# How it works: Requests User Input, 
#	Function visit_web(): Opens Browser, Loads URL, Waits for some time, Finds Element, Clicks Element, Waits for some time, Closes Browser 
#	Function repeat_visit_web(): Loops previous steps based on the number of times specified by user input 
#	Keeps Printing Log messages on key steps
# Requirements: Python and Selenium 
# More IDEAS you could add to SleekWebBot: Error Handling, Job Completion Report, Alert/Notification after completion via email or sms, etc

import os,time
from selenium import webdriver # Import the Selenium Webdriver


urlToVisit = raw_input("What website URL would you like to visit? : ") # Capture Website url to visit
secondsWaitBrowserPageLoad = raw_input("How many seconds will it take the browser to fully load the page requested? : ") # Seconds to wait while browser loads page
elemToClick = raw_input("Enter class of element to be clicked : ") # Website element to click
secondsWaitCloseBrowser = raw_input("In how many seconds after element has been clicked should the browser be closed? : ") # Seconds to wait before closing browser. (You could make these random)
noOfVisitsToBeDone = raw_input("How many times should the process of visiting this website be repeated? : ") # No. of times to revisit specified website
noOfVisitsCompleted = 0 # The initial value of noOfVisitsCompleted, with global scope


def visit_web():
	browser = webdriver.Firefox() # Get local session of firefox
	print "Browser Launched..." # Log message on browser opened
	browser.implicitly_wait(int(secondsWaitBrowserPageLoad)) # Wait 30 seconds when doing a find_element in browser before carrying on
	browser.get(urlToVisit) # Load App page
	print "URL Loaded..." # Log message on URL opened
	elem = browser.find_element_by_class_name(elemToClick) # Locate element on Website using class name
	elem.click() # Click specified element on Website
	print "Element Clicked..." # Log message on element clicked
	time.sleep(int(secondsWaitCloseBrowser)) # Wait 5 seconds after clicking element before carrying on
	os.system("TASKKILL /F /IM firefox.exe")  # Close Browser
	print "Browser Closed..." # Log message on browser closed
	global noOfVisitsCompleted # Using global keyword to signify that assignment is done at a global scope
	print "Visit No. %d Completed "% int(noOfVisitsCompleted) # Log message on visit stop

	
def repeat_visit_web():
	for i in xrange(int(noOfVisitsToBeDone)): # Number of times to revisit web
		global noOfVisitsCompleted # Using global keyword to signify that assignment is done at a global scope
		noOfVisitsCompleted = i+1 # xrange returns 0 index based numbers so to make them realistic for humans we add 1
		print "Visit No. %d Started "% int(noOfVisitsCompleted) # Log message on visit start
		visit_web() # Call the visit_web function to visit specified website

		
repeat_visit_web() # The initial call that starts the program