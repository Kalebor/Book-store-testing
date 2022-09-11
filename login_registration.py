import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()

'''Registration'''

#1
driver.get("http://practice.automationtesting.in")
driver.implicitly_wait(5)
#2
my_account_menu = driver.find_element_by_id("menu-item-50").click()
#3
email = driver.find_element_by_id("reg_email")
email.send_keys("kalebor80@gmail.com")
#4
password = driver.find_element_by_id("reg_password")
password.send_keys("Abrakadabra1980!!!")
#5
register = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "p>input[name='register']")) ).click()

'''Login'''

#1
driver.get("http://practice.automationtesting.in")
driver.implicitly_wait(5)
#2
my_account_menu = driver.find_element_by_id("menu-item-50").click()
#3
email = driver.find_element_by_id("username")
email.send_keys("kalebor80@gmail.com")
#4
password = driver.find_element_by_id("password")
password.send_keys("Abrakadabra1980!!!")
#5
login = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "p>input[name='login']")) ).click()
#6
logout = WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element(
    (By.CSS_SELECTOR, "li.woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--customer-logout > a"), "Logout"))