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

class TestAddtocartminusunprodus():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_addtocartminusunprodus(self):
    # Test name: add_to_cart_minus_un_produs
    # Step # | name | target | value
    # 1 | open | /ro/ | 
    self.driver.get("http://34.118.122.203/ro/")
    # 2 | setWindowSize | 1536x835 |
    self.driver.set_window_size(1536, 835)
    # 3 | click | css=.logo |
    time.sleep(5)
    self.driver.find_element(By.CSS_SELECTOR, ".logo").click()
    # 4 | click | css=.featured-products:nth-child(2) .js-product:nth-child(1) img | 
    self.driver.find_element(By.CSS_SELECTOR, ".featured-products:nth-child(2) .js-product:nth-child(1) img").click()
    product_title = self.driver.find_element(By.CLASS_NAME, 'h1').get_attribute('innerText')
    # 5 | click | css=.touchspin-down | 
    self.driver.find_element(By.CSS_SELECTOR, ".touchspin-down").click()
    # 6 | click | id=quantity_wanted | 
    self.driver.find_element(By.ID, "quantity_wanted").click()
    # 7 | click | css=.touchspin-down | 
    self.driver.find_element(By.CSS_SELECTOR, ".touchspin-down").click()
    # 8 | click | id=quantity_wanted | 
    self.driver.find_element(By.ID, "quantity_wanted").click()
    # 9 | type | id=quantity_wanted | 4
    self.driver.find_element(By.ID, "quantity_wanted").send_keys("4")
    # 10 | click | css=.add-to-cart | 
    self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
    # 11 | click | css=.cart-content-btn > .btn-secondary |
    time.sleep(5)
    self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-secondary").click()
    # 12 | click | css=.header .hidden-sm-down | 
    self.driver.find_element(By.CSS_SELECTOR, ".header .hidden-sm-down").click()
    # 13 | click | name=product-quantity-spin | 
    self.driver.find_element(By.NAME, "product-quantity-spin").click()
    # 14 | type | name=product-quantity-spin | 3
    self.driver.find_element(By.NAME, "product-quantity-spin").send_keys("3")
    element = WebDriverWait(self.driver, 15).until(lambda d: d.find_element(By.CSS_SELECTOR, '.text-sm-center > .btn'))
    # 15 | click | css=.text-sm-center > .btn | 
    self.driver.find_element(By.CSS_SELECTOR, ".text-sm-center > .btn").click()
    assert product_title.lower() in self.driver.page_source.lower()

if __name__ == '__main__':
    pytest.main()
  
