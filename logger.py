from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.common.exceptions import NoSuchElementException

# Setup settings
def setUp(self):
   self.setUpProfile()
   self.setUpOptions()
   self.setUpCapabilities()
   self.setUpProxy()
   self.driver = webdriver.Firefox(options=self.options, capabilities=self.capabilities, firefox_profile=self.profile)

def setUpOptions(self):
   self.options = webdriver.FirefoxOptions()
   self.options.headless = self.headless


def main():

    #open browser
    driver = webdriver.Chrome()
    driver.get("http://students.bmstu.ru")
    #send login and pass
    driver.find_element(By.NAME, 'username').send_keys("FFFFFF")
    driver.find_element(By.NAME, 'password').send_keys("PPPPPP")

    #TODO And here we go, reCaptcha bybass

    #press button
    driver.find_element_by_class_name("btna").click()


if __name__ == "__main__":
    main()