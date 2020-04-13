from configparser import ConfigParser

from emails.EmailSnailPro import EmailSnailPro
from sites.AgentJbzd import AgentJbzd
from utils import BrowserManager
from utils import Logger

if __name__ == '__main__' and __package__ is None:
    Logger.setup_logger()

    # Read config.ini
    config = ConfigParser()
    config.read('config.ini')
    email_provider_url = config['GENERAL']['EmailProvider']
    target_site_url = config['GENERAL']['TargetSite']

    driver = BrowserManager.init_driver()

    email_agent = EmailSnailPro(driver, email_provider_url)
    temp_email = email_agent.get_temp_email()

    site_agent = AgentJbzd(driver, target_site_url)
    site_agent.register_account(temp_email)
