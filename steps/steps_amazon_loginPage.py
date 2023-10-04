from selenium.webdriver.chrome import webdriver
from selenium import webdriver

class Amazon_login_validations:
    def __init__(self):
        pass

    def launch_crbrowser(self,url):
        driver = webdriver.Chrome()
        yield driver
        driver.quit()

        driver.get(url)
        return driver







