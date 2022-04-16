# Areli Tirado
# Brixton Automation Framework
# 04/15/22

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class BrixtonAutomation(unittest.TestCase):
    URL="https://www.brixton.com/"

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get(self.URL)
        self.buttons = self.driver.find_elements(By.CLASS_NAME, 'button--primary') 

    def test_number_buttons(self):
        assert len(self.buttons) == 7
    
    def test_shop_men_button_text(self):
        for button in self.buttons:
            if(button.text == 'Shop Men'):
                assert button.text == 'Shop Men'
    
    def test_shop_men_button_url(self):
        for button in self.buttons:
            if(button.text == 'Shop Men'):
                assert button.is_enabled() == True

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
