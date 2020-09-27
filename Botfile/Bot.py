from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from Botfile.KeyChain import userName, password
import time, os

class Bot:
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument('user-data-dir='os.path.join(os.getcwd(),'chrome-data'))
        self.chrome_options.add_argument('profile-directory=Default')
        self.chrome_options.add_argument('--disable-setuid-sandbox')
        self.chrome_options.add_argument('-no-sandbox')

        #Chrome driver is placed in project root folder
        self.driver = webdriver.Chrome(os.path.join(os.getcwd(),'chromedriver'),options=self.chrome_options)

    def homePage(self):
        """Open home page"""
        self.driver.get('https://www.instagram.com')

    def login(self):
        """Login to webapp with credentials supplied in KeyChain.py"""

        if self.driver.current_url != 'https://www.instagram.com':
            self.homePage()
            time.sleep(4)

        self.driver.find_element_by_name("username").send_keys(userName)
        self.driver.find_element_by_name("password").send_keys(password+Keys.ENTER)
        print("Enter OTP send to registered mobile number")
        print("sleeping for 6 sec...")
        time.sleep(6) # Save browser
        notNowElement = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
        notNowElement.click()
        print("sleeping for 3 sec...)
        time.sleep(3) # Disable notification
        notNowNotificationElement = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
        notNowNotificationElement.click()
