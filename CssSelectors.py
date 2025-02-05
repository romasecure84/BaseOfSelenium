from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://books.toscrape.com/'

options = webdriver.ChromeOptions()
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)

driver.get(url)
list_items = driver.find_elements(By.CSS_SELECTOR, 'li')

list_item = driver.find_element(By.CSS_SELECTOR, 'li').text

prices = driver.find_elements(By.CSS_SELECTOR, 'p.price_color')
for price in prices:
    print(price.text)
price = driver.find_element(By.CSS_SELECTOR, 'p.price_color')
print(price.text)

body = driver.find_element(By.CSS_SELECTOR, 'body#default')
print(body.text)

body_ = driver.find_element(By.ID, 'default')
print(body_.text)

alert = driver.find_element(By.CSS_SELECTOR, 'div[role="alert"]')
print(alert.text)

img_src = driver.find_element(By.CSS_SELECTOR, 'article.product_pod div a img').get_attribute('src')
print(img_src)

the_first_book = driver.find_element(By.CSS_SELECTOR, 'article.product_pod').text
print(the_first_book)

warning_div = driver.find_element(By.CSS_SELECTOR, 'div.alert-warning').get_attribute('role')
print(warning_div)

full_book_name = driver.find_element(By.CSS_SELECTOR, 'article.product_pod img').get_attribute('alt')
print(full_book_name)