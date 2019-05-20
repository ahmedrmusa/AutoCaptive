# Auto-Captive Accept
# Script runs on startup to connect company wifi and auto accept splash page
# and save two seconds of precious coffee time.
# by Ahmed Musa.

from selenium import webdriver
from wireless import Wireless

#connects to (wifi)
Wireless().connect(ssid='wifiname', password='password')

#force opens captive
driver = webdriver.Safari() #Can be any browser
driver.get("http://captive.apple.com/") #Windows : ("http://www.msftconnecttest.com/redirect/")

#clicks "Accept" and Yeets awayyy
driver.find_element_by_name("Submit").click() # -name/class/xpath("insert button element")
driver.implicitly_wait(5) #seconds
driver.quit()


# Leanned to use Selenium webdriver and Automator App.
