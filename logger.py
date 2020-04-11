import sys
import base64

from python_rucaptcha import ReCaptchaV2
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from config import config

class Method:
    login = None
    password = None
    driver = None

    def __init__(self):
        options = webdriver.ChromeOptions()
        if not config.DEBUG:
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--headless")

        self.driver = webdriver.Chrome(options=options)

    def wait(self, selector=config.DEFAULT_SELECTOR):
        delay = 3  # seconds
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
            print("Page is ready!")

        except TimeoutException:
            print("Loading took too much time!")

    def open_browser(self):
        self.driver.get(config.PAGE_URL)

    def send_data(self):
        self.driver.find_element(By.NAME, 'username').send_keys(self.login)
        self.driver.find_element(By.NAME, 'password').send_keys(self.password)

    def button_accept(self):
        self.driver.find_element_by_class_name("btn").click()
        self.wait()

    def reC_bypass(self):
        user_answer = ReCaptchaV2.ReCaptchaV2(rucaptcha_key=config.RUCAPTCHA_KEY).captcha_handler(site_key=config.SITE_KEY,
                                                                                                page_url=config.PAGE_URL)
        if not user_answer['error']:
            print(user_answer['captchaSolve'])
            print(user_answer['taskId'])
        elif user_answer['error']:
            print(user_answer['errorBody']['text'])
            print(user_answer['errorBody']['id'])

        name = 'captchaSolve'
        self.driver.execute_script(f'document.getElementById("g-recaptcha-response").innerHTML="{user_answer[name]}";')

    def open_snatch(self):
        self.driver.get(config.SNATCH_URL)
        self.wait()

    def snatching(self):

        #в bs-component ищем все list-group-item-heading mt-2 и берем из каждой 2ую list-group-item-heading mt-2
        ids = self.driver.find_elements_by_xpath('//*[@href]')

        for ii in ids:
            print(ii.get_attribute('href'))

        #TODO Куда-то все скачать

def main():
    method = Method()
    method.open_browser()
    method.send_data()
    method.reC_bypass()
    method.button_accept()
    method.open_snatch()
    method.snatching()
    print("Done")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        Method.login = [base64.b64decode(sys.argv[1]).decode('utf-8')]
        Method.password = [base64.b64decode(sys.argv[2]).decode('utf-8')]
        print('')
    else:
        print("No login/pass")
        exit(0)
    main()
