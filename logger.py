from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
from time import sleep
from python_rucaptcha import ReCaptchaV2

RUCAPTCHA_KEY = "a72b9e772c84e07f91d4858ab8e4892a"
SITE_KEY = "6Ldyzg4UAAAAACoMkMqxUJbsHuGBjir1Ds3_bFJx"
PAGE_URL = "https://students.bmstu.ru/"

class Method:
    login = None
    password = None
    driver = None
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_browser(self):
        self.driver.get("http://students.bmstu.ru")

    def send_data(self):
        self.driver.find_element(By.NAME, 'username').send_keys(self.login)
        self.driver.find_element(By.NAME, 'password').send_keys(self.password)

    def button_accept(self):
        self.driver.find_element_by_class_name("btn").click()

    def reC_bypass(self):
        user_answer = ReCaptchaV2.ReCaptchaV2(rucaptcha_key=RUCAPTCHA_KEY).captcha_handler(site_key=SITE_KEY,
                                                                                           page_url=PAGE_URL)
        if not user_answer['error']:
            print(user_answer['captchaSolve'])
            print(user_answer['taskId'])
        elif user_answer['error']:
            print(user_answer['errorBody']['text'])
            print(user_answer['errorBody']['id'])


def main():

    Method.__init__()
    Method.open_browser()



if __name__ == "__main__":
    if len(sys.argv) > 1:
        Method.password = sys.argv.pop()
        Method.login = sys.argv.pop()
    else:
        print("No login/pass")
        exit(0)
    main()