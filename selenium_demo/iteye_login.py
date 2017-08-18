# encoding=utf-8
__author__ = 'houqinzhi'

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver


def login_iteye_by_selenium():
    url = "http://www.iteye.com/login"
    user = "kevinflynn"
    password = "maoshan2011215858"
    browser = webdriver.Chrome(executable_path="/Users/didi/Bin/chromedriver")
    browser.get(url)
    usename = browser.find_element_by_xpath('//*[@id="user_name"]')
    pwd = browser.find_element_by_xpath('//*[@id="password"]')
    usename.send_keys(user)
    pwd.send_keys(password)
    login = WebDriverWait(browser, 5).until(
        expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="button"]')))
    login.click()
    import time
    time.sleep(5)
    browser.get("http://www.iteye.com/blogs")
    # time.sleep(100)
    print browser.get_cookies()

if __name__ == '__main__':
    login_iteye_by_selenium()

