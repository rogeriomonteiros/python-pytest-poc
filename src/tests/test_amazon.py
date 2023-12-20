import pytest 
from utils.hook import Hook
import os
        
class TestAmazon(Hook):

    @pytest.fixture()
    def setup(self):
        self.driver.get('http://www.amazon.com.br')

    def test_amazon(self):
        print(self.config['userNameContractor'])

    def test_google(self):
        self.driver.get('http://www.google.com.br')
