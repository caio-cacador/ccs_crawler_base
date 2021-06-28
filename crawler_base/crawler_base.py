from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CHROME = 'chrome'
FIREFOX = 'firefox'

BROWSER_LIST = [CHROME, FIREFOX]


class CrawlerBase:

    def __init__(self, browser_name: str, driver_path: str, show_browser: bool = True, page_load_timeout: int = 30,
                 option_arguments: List[str] = None):
        self.driver, options = None, None

        if browser_name not in BROWSER_LIST:
            raise ValueError('The browser name is incorrect or do not have support!')

        if browser_name == CHROME:
            from selenium.webdriver import ChromeOptions
            options = ChromeOptions()
        elif browser_name == FIREFOX:
            from selenium.webdriver import FirefoxOptions
            options = FirefoxOptions

        if options and show_browser:
            options.add_argument('--window-size=1920,1080')
            for argument in option_arguments:
                options.add_argument(argument)

        if browser_name == CHROME:
            from selenium.webdriver import Chrome
            self.driver = Chrome(executable_path=driver_path, options=options)
        elif browser_name == FIREFOX:
            from selenium.webdriver import Firefox
            self.driver = Firefox(executable_path=driver_path, options=options)

        self.driver.set_page_load_timeout(page_load_timeout)

    def get_element_by(self, by: By, str_: str, element=None):
        element = element if element else self.driver
        return WebDriverWait(element, 30).until(EC.presence_of_element_located((by, str_)))

    def get_elements_by(self, by: By, str_: str, element=None):
        element = element if element else self.driver
        return WebDriverWait(element, 30).until(EC.presence_of_all_elements_located((by, str_)))
