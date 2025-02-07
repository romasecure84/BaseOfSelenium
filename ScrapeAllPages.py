from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import openpyxl

quote_dict = {'quote':[], 'author':[], 'tags':[]}

def login(the_driver):
    login_button = the_driver.find_element(By.XPATH, '//a[text()="Login"]')
    login_button.click()

    username_shield = the_driver.find_element(By.ID, 'username')
    username_shield.send_keys('userName')

    password_shield = the_driver.find_element(By.ID, 'password')
    password_shield.send_keys('password')

    login_button_submit = the_driver.find_element(By.XPATH, '//input[@type="submit"]')
    login_button_submit.click()

def scrape_page(the_driver):
    quotes = the_driver.find_elements(By.CLASS_NAME, 'quote')

    for element in quotes:
        quote = element.find_element(By.CLASS_NAME, 'text').text
        quote_dict['quote'].append(quote)

        author = element.find_element(By.CLASS_NAME, 'author').text
        quote_dict['author'].append(author)

        tag_container = element.find_element(By.CLASS_NAME, 'tags')
        a_tags = tag_container.find_elements(By.CSS_SELECTOR, 'a')
        tags = ''
        for i, a_tag in enumerate(a_tags):
            if i == len(a_tags) - 1:
                tag = a_tag.text
            else:
                tag = a_tag.text + ", "
            tags += tag
        quote_dict['tags'].append(tags)

url = 'https://quotes.toscrape.com/js/'

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options = options)
driver.get(url)

login(driver)

while True:
    scrape_page(driver)

    try:
        next_button = driver.find_element(By.CSS_SELECTOR,'li.next a')
        next_button.click()
    except:
        break


df = pd.DataFrame(quote_dict)
df.to_excel('quotes.xlsx')
