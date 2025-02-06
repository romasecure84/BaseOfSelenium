from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://books.toscrape.com/'

options = webdriver.ChromeOptions()
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)

driver.get(url)
list_items = driver.find_elements(By.XPATH, '//li')
print(len(list_items))
first_item = list_items[0]
print(first_item.text)

prices = driver.find_elements(By.XPATH, '//p[@class="price_color"]')
for price in prices:
    print(price.text)

body = driver.find_element(By.XPATH, '//body[@id="default"]')
print(body.text)

alert = driver.find_element(By.XPATH, '//div[@role="alert"]')
print(alert.text)

next_button = driver.find_element(By.XPATH, '//a[text()="next"]')
print(next_button.get_attribute('href'))

img_src = driver.find_element(By.XPATH, '//article[@class="product_pod"]/div/a/img').get_attribute('src')
print(img_src)

first_book = driver.find_element(By.XPATH, '//article[@class="product_pod"]')
# first_book_div = first_book.find_element(By.XPATH, './div').get_attribute('class')
# print(first_book_div)
parent_of_first = first_book.find_element(By.XPATH, './..')
print(parent_of_first.tag_name)

following_sibling_element = parent_of_first.find_element(By.XPATH, './following-sibling::li[1]')
second_book_name = following_sibling_element.find_element(By.XPATH, './article/div/a/img').get_attribute('alt')
print(second_book_name)

book_name = driver.find_element(By.XPATH, '//article[@class="product_pod"]/../following-sibling::li[19]/article/div/a/img').get_attribute('alt')
print(book_name)