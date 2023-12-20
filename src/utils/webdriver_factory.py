# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class WebdriverFactory():

    def create_driver(self,browser='chrome'):
        if browser.lower() == 'chrome':
            return self.create_chrome_driver()
        
        raise Exception(f'Browser {browser} not available')
    
    
    def create_chrome_driver(self):
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        driver.set_window_size(1920,1080)
        return driver

