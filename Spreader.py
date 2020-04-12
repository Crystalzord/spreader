from configparser import ConfigParser

from emails.EmailSnailPro import EmailSnailPro
from sites.AgentJbzd import AgentJbzd
from utils import DriverManager

# Read config.ini
config = ConfigParser()
config.read('config.ini')
email_provider_url = config['GENERAL']['EmailProvider']
target_site_url = config['GENERAL']['TargetSite']

driver = DriverManager.init_driver()
print(driver)

email_agent = EmailSnailPro(driver, email_provider_url)
temp_email = email_agent.get_temp_email()
print(temp_email)

site_agent = AgentJbzd(driver, target_site_url)
site_agent.register_account(temp_email)
