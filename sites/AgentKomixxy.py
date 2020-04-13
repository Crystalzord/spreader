import logging

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from sites.FormalAgenttInterface import FormalAgenttInterface
from utils import BrowserManager

logger = logging.getLogger(__name__)


class AgentKomixxy(FormalAgenttInterface):

    def __init__(self, driver: webdriver, url: str):
        self.url = url
        self.driver = driver
        logger.info("Created Komixxy object with url: {} and driver: {} ".format(self.url, self.driver))

    def register_account(self, email: str):
        BrowserManager.open_new_tab(self.driver, self.url)
        BrowserManager.switch_to_newest_tab(self.driver)
        # TODO: fill form

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