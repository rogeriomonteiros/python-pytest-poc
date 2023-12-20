
from dotenv import dotenv_values
from utils.webdriver_factory import WebdriverFactory 

class Hook():

    @classmethod
    def setup_class(cls):
        cls.config=dotenv_values('.env')
        cls.driver = WebdriverFactory().create_driver(cls.config['browser'])

    @classmethod
    def teardown_class(cls):
        # pass
        cls.driver.quit()

    def setup_method(self):
        print('geglio')

    def teardown_method(self):
        pass
    
        
        