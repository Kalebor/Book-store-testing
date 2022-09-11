import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()

#1
driver.get("http://practice.automationtesting.in")
driver.implicitly_wait(5)
#2
driver.execute_script("window.scrollBy(0,600);")
#3
selenium_ruby = driver.find_element_by_css_selector("li.post-160 a.woocommerce-LoopProduct-link h3").click()
#4
reviews = driver.find_element_by_css_selector("li.reviews_tab").click()
#5
stars = driver.find_element_by_css_selector("a.star-5").click()
#6
review = driver.find_element_by_id("comment")
review.send_keys("Nice book!")
#7
name = driver.find_element_by_id("author")
name.send_keys("Demo User")
#8
email = driver.find_element_by_id("email")
email.send_keys("demo.user@gmail.com")
#9
submit = driver.find_element_by_css_selector("#submit.submit").click()