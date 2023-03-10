# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTotalproductscart():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_totalproductscart(self):
    # Test name: total_product_cart
    # Step # | name | target | value
    # 1 | open | /ro/ | 
    self.driver.get("http://34.118.122.203/ro/")
    # 2 | setWindowSize | 1536x835 | 
    self.driver.set_window_size(1536, 835)
    # 3 | click | css=.featured-products:nth-child(2) .js-product:nth-child(3) img |
    time.sleep(5)
    self.driver.find_element(By.CSS_SELECTOR, ".featured-products:nth-child(2) .js-product:nth-child(3) img").click()
    # 4 | click | css=.bootstrap-touchspin-up | 
    self.driver.find_element(By.CSS_SELECTOR, ".bootstrap-touchspin-up").click()
    product_title = self.driver.find_element(By.CLASS_NAME, 'h1').get_attribute('innerText')
    # 5 | click | css=.bootstrap-touchspin-up | 
    self.driver.find_element(By.CSS_SELECTOR, ".bootstrap-touchspin-up").click()
    # 6 | click | css=.bootstrap-touchspin-up | 
    self.driver.find_element(By.CSS_SELECTOR, ".bootstrap-touchspin-up").click()
    # 7 | click | css=.bootstrap-touchspin-up | 
    self.driver.find_element(By.CSS_SELECTOR, ".bootstrap-touchspin-up").click()
    # 8 | click | css=.add-to-cart | 
    self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
    # 9 | click | css=.cart-content-btn > .btn-secondary |
    time.sleep(5)
    self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-secondary").click()
    # 10 | click | css=.logo | 
    self.driver.find_element(By.CSS_SELECTOR, ".logo").click()
    # 11 | click | css=.featured-products:nth-child(2) .js-product:nth-child(2) img | 
    self.driver.find_element(By.CSS_SELECTOR, ".featured-products:nth-child(2) .js-product:nth-child(2) img").click()
    # 12 | click | css=.touchspin-up | 
    self.driver.find_element(By.CSS_SELECTOR, ".touchspin-up").click()
    # 13 | click | css=.touchspin-up | 
    self.driver.find_element(By.CSS_SELECTOR, ".touchspin-up").click()
    # 14 | click | css=.touchspin-up | 
    self.driver.find_element(By.CSS_SELECTOR, ".touchspin-up").click()
    # 15 | click | css=.touchspin-up | 
    self.driver.find_element(By.CSS_SELECTOR, ".touchspin-up").click()
    # 16 | click | css=.add-to-cart | 
    self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
    # 17 | click | css=.cart-content-btn > .btn-primary |
    time.sleep(8)
    self.driver.find_element(By.CSS_SELECTOR, '.cart-content-btn > .btn-primary').click()
    element = WebDriverWait(self.driver, 15).until(lambda d: d.find_element(By.CSS_SELECTOR, '.text-sm-center > .btn '))

    # 18 | click | css=.text-sm-center > .btn | 
    self.driver.find_element(By.CSS_SELECTOR, ".text-sm-center > .btn").click()
    assert product_title.lower() in self.driver.page_source.lower()
    assert 'Page not found' not in self.driver.page_source

if __name__ == '__main__':
    pytest.main()