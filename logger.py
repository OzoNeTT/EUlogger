from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
from python_rucaptcha import ReCaptchaV2
import local as conf

assert conf.RUCAPTCHA_KEY
assert conf.SITE_KEY
assert conf.PAGE_URL

class Method:
    login = None
    password = None
    driver = None
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_browser(self):
        self.driver.get(conf.PAGE_URL)

    def send_data(self):
        self.driver.find_element(By.NAME, 'username').send_keys(self.login)
        self.driver.find_element(By.NAME, 'password').send_keys(self.password)

    def button_accept(self):
        self.driver.find_element_by_class_name("btn").click()

    def reC_bypass(self):
        user_answer = ReCaptchaV2.ReCaptchaV2(rucaptcha_key=conf.RUCAPTCHA_KEY).captcha_handler(site_key=conf.SITE_KEY,
                                                                                           page_url=conf.PAGE_URL)
        if not user_answer['error']:
            print(user_answer['captchaSolve'])
            print(user_answer['taskId'])
        elif user_answer['error']:
            print(user_answer['errorBody']['text'])
            print(user_answer['errorBody']['id'])

        name = 'captchaSolve'
        self.driver.execute_script(f'document.getElementById("g-recaptcha-response").innerHTML="{user_answer[name]}";')


def main():

    method = Method()
    method.open_browser()
    method.send_data()
    method.reC_bypass()
    method.button_accept()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        Method.password = sys.argv.pop()
        Method.login = sys.argv.pop()
    else:
        print("No login/pass")
        exit(0)
    main()