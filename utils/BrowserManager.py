from configparser import ConfigParser

from selenium import webdriver


def init_driver() -> webdriver:
    config = ConfigParser()
    config.read('config.ini')
    driver = webdriver.Chrome(config['GENERAL']['DriverPath'])
    driver.maximize_window()
    return driver


def open_new_tab(driver: webdriver, url: str):
    driver.execute_script('window.open("' + url + '","_blank");')


# TODO: make it more generic (switch to tab with title instead)
def switch_to_newest_tab(driver: webdriver):
    driver.switch_to.window(driver.window_handles[-1])


def bypass_captcha(driver: webdriver, xpath_locator: str, locator_value: str):
    driver.switch_to.frame(driver.find_element_by_xpath(xpath_locator))
    driver.find_element_by_class_name(locator_value).click()
