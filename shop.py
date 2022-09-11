import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()

'''Отображение страницы товара'''

# #1
# driver.get("http://practice.automationtesting.in")
# driver.implicitly_wait(5)
# #2
# my_account_menu = driver.find_element_by_id("menu-item-50").click()
# email = driver.find_element_by_id("username")
# email.send_keys("kalebor80@gmail.com")
# password = driver.find_element_by_id("password")
# password.send_keys("Abrakadabra1980!!!")
# login = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
#     (By.CSS_SELECTOR, "p>input[name='login']")) ).click()
# #3
# shop = driver.find_element_by_id("menu-item-40").click()
# #4
# book_html_5_forms = driver.find_element_by_css_selector("li.post-181>:nth-child(2)").click()
# #5
# book_title = WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element(
#     (By.CSS_SELECTOR, "div.summary.entry-summary > h1"), "HTML5 Forms"))

'''Количество товаров в категории'''

# #1
# driver.get("http://practice.automationtesting.in")
# driver.implicitly_wait(5)
# #2
# my_account_menu = driver.find_element_by_id("menu-item-50").click()
# email = driver.find_element_by_id("username")
# email.send_keys("kalebor80@gmail.com")
# password = driver.find_element_by_id("password")
# password.send_keys("Abrakadabra1980!!!")
# login = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "p>input[name='login']")) ).click()
# #3
# shop = driver.find_element_by_id("menu-item-40").click()
# #4
# html = driver.find_element_by_css_selector("li.cat-item.cat-item-19>a").click()
# #5
# quantity_of_goods = driver.find_elements_by_class_name("type-product")
# if len(quantity_of_goods)==3:
#     print("Отображается",str(len(quantity_of_goods)),"товара")

'''Сортировка товара'''

# #1
# driver.get("http://practice.automationtesting.in")
# driver.implicitly_wait(5)
# #2
# my_account_menu = driver.find_element_by_id("menu-item-50").click()
# email = driver.find_element_by_id("username")
# email.send_keys("kalebor80@gmail.com")
# password = driver.find_element_by_id("password")
# password.send_keys("Abrakadabra1980!!!")
# login = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
#     (By.CSS_SELECTOR, "p>input[name='login']")) ).click()
# #3
# shop = driver.find_element_by_id("menu-item-40").click()
# #4
# sort_by = driver.find_element_by_class_name("orderby")
# sort_by_value = sort_by.get_attribute("value")
# if sort_by_value=="menu_order":
#     print("Выбран вариант сортировки Default Sorting")
# #5
# sort_by_new = Select(sort_by)
# sort_by_new.select_by_value("price-desc")
# #6
# sort_by = driver.find_element_by_class_name("orderby")
# #7
# sort_by_value = sort_by.get_attribute("value")
# if sort_by_value=="price-desc":
#     print("Выбран вариант сортировки Sort by price: high to low")
#
# '''Отображение, скидка товара'''
#
# #1
# driver.get("http://practice.automationtesting.in")
# driver.implicitly_wait(5)
# #2
# my_account_menu = driver.find_element_by_id("menu-item-50").click()
# email = driver.find_element_by_id("username")
# email.send_keys("kalebor80@gmail.com")
# password = driver.find_element_by_id("password")
# password.send_keys("Abrakadabra1980!!!")
# login = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
#     (By.CSS_SELECTOR, "p>input[name='login']")) ).click()
# #3
# shop = driver.find_element_by_id("menu-item-40").click()
# #4
# book_android = driver.find_element_by_css_selector("li.post-169 > a.button").click()
# #5
# old_price = driver.find_element_by_css_selector("del>.woocommerce-Price-amount")
# old_price_text = old_price.text
# assert old_price_text=="₹600.00"
# #6
# new_price = driver.find_element_by_css_selector("ins>.woocommerce-Price-amount")
# new_price_text = new_price.text
# assert new_price_text=="₹450.00"
# #7
# WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
#     (By.CSS_SELECTOR, "div.images>a>img"))).click()
# #8
# WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
#     (By.CSS_SELECTOR, "a.pp_close"))).click()
#
# '''Проверка цены в корзине'''
#
# #1
# driver.get("http://practice.automationtesting.in")
# driver.implicitly_wait(5)
# #2
# shop = driver.find_element_by_id("menu-item-40").click()
# #3
# add_to_basket = driver.find_element_by_css_selector("li.post-182>:nth-child(2)").click()
# time.sleep(3)
# #4
# item = driver.find_element_by_css_selector("#wpmenucartli > a > span.cartcontents")
# item_text = item.text
# assert item_text=="1 Item"
# price = driver.find_element_by_css_selector("#wpmenucartli > a > span.amount")
# price_text = price.text
# assert price_text=="₹180.00"
# #5
# basket = driver.find_element_by_css_selector("a.wpmenucart-contents").click()
# #6
# subtotal = WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element(
#     (By.CSS_SELECTOR, "tr.cart-subtotal > td > span"), "₹180.00"))
# #7
# total = WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element(
#     (By.CSS_SELECTOR, "tr.order-total > td > strong > span"), "₹183.60"))
#
# '''Работа в корзине'''
#
# #1
# driver.get("http://practice.automationtesting.in")
# driver.implicitly_wait(5)
# #2
# shop = driver.find_element_by_id("menu-item-40").click()
# #3
# driver.execute_script("window.scrollBy(0, 300);")
# add_to_basket = driver.find_element_by_css_selector("li.post-182>:nth-child(2)").click()
# time.sleep(5)
# add_to_basket_2 = driver.find_element_by_css_selector("li.post-180 > a.button").click()
# #4
# basket_btn = driver.find_element_by_css_selector("a.wpmenucart-contents").click()
# #5
# time.sleep(5)
# del_book = driver.find_element_by_css_selector("tr:nth-child(1) > td.product-remove > a").click()
# #6
# undo = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
#     (By.CSS_SELECTOR, "div.woocommerce-message>a"))).click()
# #7
# clear = driver.find_element_by_css_selector("tr:nth-child(2) > td.product-quantity > div > input").clear()
# quantity = driver.find_element_by_css_selector("tr:nth-child(2) > td.product-quantity > div > input")
# quantity.send_keys("3")
# #8
# update = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
#     (By.CSS_SELECTOR, "td > input.button"))).click()
# #9
# time.sleep(3)
# quantity_value = driver.find_element_by_css_selector("tr:nth-child(2) > td.product-quantity > div > input")
# quantity_value_new = quantity_value.get_attribute("value")
# assert quantity_value_new=="3"
# #10
# time.sleep(3)
# apply_coupon = driver.find_element_by_css_selector("div > input.button").click()
# #11
# error = WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element(
#     (By.CSS_SELECTOR, "ul.woocommerce-error > li"), "Please enter a coupon code."))
#
# '''Покупка товара'''
#
# #1
# driver.get("http://practice.automationtesting.in")
# driver.implicitly_wait(5)
# #2
# shop = driver.find_element_by_id("menu-item-40").click()
# driver.execute_script("window.scrollBy(0, 300);")
# #3
# add_to_basket = driver.find_element_by_css_selector("li.post-182>:nth-child(2)").click()
# time.sleep(3)
# #4
# basket = driver.find_element_by_css_selector("li > a.wpmenucart-contents").click()
# #5
# proceed = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
#     (By.CSS_SELECTOR, "div.wc-proceed-to-checkout>a"))).click()
# #6
# first_name = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
#     (By.ID, "billing_first_name")))
# first_name.send_keys("Demo")
# last_name = driver.find_element_by_id("billing_last_name").send_keys("User")
# email = driver.find_element_by_id("billing_email").send_keys("demo.user@gmail.com")
# phone = driver.find_element_by_id("billing_phone").send_keys("+79111234567")
# country = driver.find_element_by_id("s2id_billing_country").click()
# country_search = driver.find_element_by_id("s2id_autogen1_search").send_keys("russia")
# country_click = driver.find_element_by_id("select2-results-1").click()
# street = driver.find_element_by_css_selector("input#billing_address_1").send_keys("Невский пр. д.1")
# town = driver.find_element_by_css_selector("input#billing_city").send_keys("Санкт-Петербург")
# state = driver.find_element_by_css_selector("input#billing_state").send_keys("Санкт-Петербург")
# postcode = driver.find_element_by_css_selector("input#billing_postcode").send_keys("199000")
# #7
# driver.execute_script("window.scrollBy(0, 600);")
# time.sleep(3)
# check_payments = driver.find_element_by_id("payment_method_cheque").click()
# #8
# place_order = driver.find_element_by_id("place_order").click()
# #9
# message = WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element(
#     (By.CSS_SELECTOR, "p.woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
# #10
# payment_method = WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element(
#     (By.CSS_SELECTOR, "li.method > strong"), "Check Payments"))