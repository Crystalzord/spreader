from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from emails.FormalEmailInterface import FormalEmailInterface


class EmailSnailPro(FormalEmailInterface):

    def __init__(self, driver: webdriver, url: str):
        self.url = url
        self.driver = driver
        print("Created EmailSnailPro object with url: {} and driver: {} ".format(self.url, self.driver))

    def get_temp_email(self):
        self.driver.get(self.url)
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, '//*[@id="btnChange"]'))).click()
        generated_email = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.ID, 'ipTempMail'))).get_attribute('value')
        print("Generated email is: " + generated_email)  # TODO: Add logger here
        return generated_email

    def get_activation_link(self) -> str:
        raise NotImplementedError
