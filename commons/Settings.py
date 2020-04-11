import configparser
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def init():
    # --- READ CONFIG FILE ---
    # https://docs.python.org/3/library/configparser.html
    config = configparser.ConfigParser()
    config.read('config.ini')

    global browser_driver
    browser_driver = config['GENERAL']['BrowserChromeDriverPath']

    global email_provider
    email_provider = config['GENERAL']['EmailProvider']

    global driver
    driver = webdriver.Chrome(browser_driver)
    driver.maximize_window()
    driver.get(email_provider)
    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, '//*[@id="btnChange"]'))).click()
    generated_email = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, 'ipTempMail'))).get_attribute('value')
    print(generated_email)
