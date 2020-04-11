import configparser
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import accounts.Jbzd as jbzd


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
    print("Generated email is: " + generated_email)  # TODO: Add logger here

    # TODO: create a function for opening a new tab with one parameter 'hostname' to make it more generic
    #
    # open jbzd homepage in a new tab and switch to this tab
    jbzd_hostname = jbzd.Jbzd.hostname
    driver.execute_script('window.open("' + jbzd_hostname +'","_blank");')
    driver.switch_to.window(driver.window_handles[-1])

    # TODO: add some better architecture for closing welcoming/adblock popups on each page
    #
    # click "Akceptuję" button on jbzd page
    #

    try:
        WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH, '//a[@class="banner_continue--3gvVl"]'))).click()
    except NoSuchElementException:
        print("Alert not present")  # TODO: Add logger here


    # TODO: create a function for opening registration page with one parameter 'sign in xpath' or add function
    #  "go_to_registration" for every supported hostname
    #
    # go to a registration page of jbzd

    driver.find_element_by_xpath('//div[@class="tab"]/span[contains(text(), "Załóż konto")]').click()

    # TODO: create a file with common login data if possible e.g. logins or password - change the hardcoded variables below!
    #
    # fill registration form

    driver.find_element_by_id("login").send_keys("NiceRomanJack")
    driver.find_element_by_id("email").send_keys(generated_email)
    driver.find_element_by_id("password").send_keys("Password123!")
    driver.find_element_by_id("password_confirmation").send_keys("Password123!")

    # TODO: create a function for by-passing captcha with two parameters: 1) locator's type 2) locator's value
    #
    # by-pass captcha

    driver.switch_to.frame(driver.find_element_by_xpath("//iframe[starts-with(@name,'a-')]"))
    driver.find_element_by_class_name("recaptcha-checkbox-border").click()

    # TODO: create a function for going back to previous iframe
    #
    # Go back from iframe
    # driver.switch_to.default_content()
