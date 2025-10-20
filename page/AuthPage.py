from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class AuthPage:

    def __init__(self, driver: WebDriver)-> None:
        self.url = "https://trello.com/login"
        self.driver = driver

    def go(self):
        self.driver