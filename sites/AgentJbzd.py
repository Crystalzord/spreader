import logging

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from sites.FormalAgenttInterface import FormalAgenttInterface
from utils import DriverManager

logger = logging.getLogger(__name__)


class AgentJbzd(FormalAgenttInterface):

    def __init__(self, driver: webdriver, url: str):
        self.url = url
        self.driver = driver
        logger.info("Created Jbzd object with url: {} and driver: {} ".format(self.url, self.driver))

    def register_account(self, email: str):
        DriverManager.open_tab(self.driver, self.url)
        DriverManager.switch_to_tab(self.driver)

        # click "Akceptuję" button on jbzd page
        try:
            WebDriverWait(self.driver, 20).until(
                ec.element_to_be_clickable((By.XPATH, '//a[@class="banner_continue--3gvVl"]'))).click()
        except NoSuchElementException:
            logger.info("Cookie alert not present on {}".format(self.url))

        self.driver.find_element_by_xpath('//div[@class="tab"]/span[contains(text(), "Załóż konto")]').click()

        # TODO: login and password generator
        self.driver.find_element_by_id("login").send_keys("NiceRomanJack")
        self.driver.find_element_by_id("email").send_keys(email)
        self.driver.find_element_by_id("password").send_keys("Password123!")
        self.driver.find_element_by_id("password_confirmation").send_keys("Password123!")

        DriverManager.bypass_captcha(self.driver, "//iframe[starts-with(@name,'a-')]", "recaptcha-checkbox-border")

        # Go back from iframe
        self.driver.switch_to.default_content()

    def login(self):
        raise NotImplementedError

    def logout(self):
        raise NotImplementedError

    def create_post(self):
        raise NotImplementedError

    def create_comment(self):
        raise NotImplementedError

    def like_post(self):
        raise NotImplementedError

    def like_comment(self):
        raise NotImplementedError

    def dislike_comment(self):
        raise NotImplementedError
