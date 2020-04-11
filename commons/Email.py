# This class is responsible for creating a temporary email.
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class Email(object):

    def __init__(self, driver, email_provider):
        self.driver = driver
        self.email_provider = email_provider

    def get_new_email(self) -> str:
        self.driver.get(self.email_provider)
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, '//*[@id="btnChange"]'))).click()
        generated_email = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, '//div[contains(text(), "@stempmail.com")]')))
        return generated_email.text
