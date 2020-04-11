from selenium import webdriver
from selenium.webdriver.common.by import By

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