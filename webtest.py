from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import time



#Talk to local chrome.  Assumes chromedriver downloaded from https://sites.google.com/a/chromium.org/chromedriver/downloads
#driver = webdriver.Chrome('/Users/nik/try/chromedriver')

#Talk to Selenium server.  Assumes selenium from docker ala. https://hub.docker.com/r/selenium/standalone-chrome-debug/ and
#https://github.com/SeleniumHQ/docker-selenium
# Can watch via VNC to localhost: (docker ps to find local port)   (password is "secret")
driver = webdriver.Remote(command_executor='http://127.0.0.1:32770/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)

driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
time.sleep(5)                   # Sleep 5 seconds to give chance to see.
driver.close()
