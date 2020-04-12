import logging
from configparser import ConfigParser

from emails.EmailSnailPro import EmailSnailPro
from sites.AgentJbzd import AgentJbzd
from utils import DriverManager


def setup_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    fh = logging.FileHandler('spreader-log.txt')
    fh.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)

    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s')

    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)


if __name__ == '__main__' and __package__ is None:
    setup_logger()

    # Read config.ini
    config = ConfigParser()
    config.read('config.ini')
    email_provider_url = config['GENERAL']['EmailProvider']
    target_site_url = config['GENERAL']['TargetSite']

    driver = DriverManager.init_driver()

    email_agent = EmailSnailPro(driver, email_provider_url)
    temp_email = email_agent.get_temp_email()

    site_agent = AgentJbzd(driver, target_site_url)
    site_agent.register_account(temp_email)
