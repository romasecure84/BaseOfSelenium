from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

author_dict = {'author':[], 'born':[], 'born_location':[]}

url = 'https://quotes.toscrape.com/'

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options = options)
driver.get(url)

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
        author = element.find_element(By.CLASS_NAME, 'author').text
        if author not in author_dict['author']:
            author_dict['author'].append(author)
            author_about_button = element.find_element(By.CSS_SELECTOR, 'a')
            author_about_button.click()
            author_dict['born'].append(the_driver.find_element(By.CLASS_NAME, 'author-born-date').text)
            author_dict['born_location'].append(the_driver.find_element(By.CLASS_NAME, 'author-born-location').text)
            driver.back()

login(driver)
while True:
    scrape_page(driver)

    try:
        next_button = driver.find_element(By.CSS_SELECTOR,'li.next a')
        next_button.click()
    except:
        break

df = pd.DataFrame(author_dict)
df.to_excel('authors2.xlsx')