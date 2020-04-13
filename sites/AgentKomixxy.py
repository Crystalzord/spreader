import logging

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from sites.FormalAgenttInterface import FormalAgenttInterface
from utils import DriverManager

logger = logging.getLogger(__name__)


class AgentKomixxy(FormalAgenttInterface):
    def register_account(self, email: str):
        raise NotImplementedError

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